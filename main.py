import os
import re

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

print('Bot is running... 🏃‍♂️')

class DeconstructedMessage:
    def __init__(self, time, train, station, direction):
        self.time = time
        self.train = train
        self.station = station
        self.direction = direction
        

uBahnLines = ['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'U9']
sBahnLines = ['S1', 'S2', 'S3', 'S5', 'S7', 'S8' 'S9', 'S25', 'S26', 'S41', 'S42', 'S45', 'S46', 'S75', 'S47', 'S85']

messages = []
@bot.message_handler(func=lambda msg: True)
def get_info(message):
    

    



bot.infinity_polling()