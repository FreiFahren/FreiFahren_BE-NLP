import json
import pickle
import os
import random
import string

data = []
RAW_DATA_PATH = 'messages_and_times.json'

with open(RAW_DATA_PATH, 'r') as f:
    messages = json.load(f)

# Iteration through messages
for message in messages:

    print()

    print('Message:', message['message'])

    current_station = input('Enter the current STATION for this message (or quit): ')
    if current_station.lower() == 'quit':
        break

    if current_station.lower() == 'none' or current_station.lower() == '':
        current_station = None

    print()

    line = input('Enter the SUBWAY/TRAIN LINE for this message: ')

    if line.lower() == 'none' or line.lower() == '':
        line = None

    print()

    direction = input('Enter the DIRECTION for this message: ')

    if direction.lower() == 'none' or direction.lower() == '':
        direction = None

    data.append((message['message'], current_station, line, direction))

# Generate a random filename
filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# Ensure the directory exists
os.makedirs('labeled_data', exist_ok=True)

# Save the data

with open(os.path.join('labeled_data', filename + '.py'), 'wb') as f:
    pickle.dump(data, f)

#  Load the data:
#
#  import pickle
#  with open(f'labeled_data/{filename}.py', 'rb') as f:
#      loaded_data = pickle.load(f)
