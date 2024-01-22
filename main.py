import os
import re
from fuzzywuzzy import process
import telebot
import json

class TicketInspector:
    def __init__(self, time, train, station, direction):
        #self.time = time
        self.train = train
        self.station = station
        self.direction = direction
        

ubahn_lines = ['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9']
sbahn_lines = ['S1', 'S2', 'S3', 'S5', 'S7', 'S8' 'S9', 'S25', 'S26', 'S41', 'S42', 'S45', 'S46', 'S75', 'S47', 'S85']

def find_line(text, lines):
    # remove all whitespaces from the text
    text = text.replace(' ', '')
    for line in lines:
        if line.lower() in text.lower():
            return line
    return None

# get station_data from json file
with open('data.json', 'r') as f:
    stations_data = json.load(f)

def format_text(text):
    # Replace all '-' with whitespaces and convert to lowercase
    text = text.lower().replace('-', ' ')
    # Remove all isolated 's' and 'u' 
    text = re.sub(r'\b(s|u)\b', '', text)
    return text

def find_station(text, threshold=46):
    text = format_text(text)
    all_stations = []

    # Add all stations and synonyms to the list
    for station_type in stations_data.values():
        for station, synonyms in station_type.items():
            all_stations.append(station.lower())
            all_stations.extend([syn.lower() for syn in synonyms])

    best_match, score = process.extractOne(text, all_stations)
    if score >= threshold:
        # Find the station that matches the best match
        for station_type in stations_data.values():
            for station, synonyms in station_type.items():
                if best_match in [station.lower()] + [syn.lower() for syn in synonyms]:
                    return station
    return None

def find_direction(text):
    text = format_text(text)

    direction_keywords = ['nach', 'richtung', 'bis', 'zu', 'to', 'towards']
    for keyword in direction_keywords:
        if keyword in text:
            # check if a station is mentioned after the keyword
            if find_station(text.split(keyword)[1]):
                found_direction = find_station(text.split(keyword)[1])
                # remove the station from the text
                text = text.replace(found_direction, '')
                return found_direction, text


if __name__ == "__main__":
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    bot = telebot.TeleBot(BOT_TOKEN)

    print('Bot is running... 🏃‍♂️')

    @bot.message_handler(func=lambda msg: True)
    def get_info(message):
        text = message.text
        found_line = find_line(text, ubahn_lines + sbahn_lines)
        result = find_direction(text)
        found_direction = result[0]
        text_without_direction = result[1]
        found_station = find_station(text_without_direction)
        if found_line or found_station or found_direction:
            print(f'Found station: {found_station}')
            print(f'Found line: {found_line}')
            # create a TicketInspector object
            ticket_inspector = TicketInspector(time=None, train=found_line, station=found_station, direction=found_direction)
            print(ticket_inspector.__dict__)
        else:
            print('No valuable information found')
            return

    bot.infinity_polling()