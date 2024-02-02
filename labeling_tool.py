import json
import pickle
import os

# The purpose of this script is to label the data in messages_and_times.json / RAW_DATA_PATH
# Run in console and follow the prompts. If you quit, the data will be saved in labeled_data/ as a pickle file.
#
# To load the data, use the following code:
# import pickle
# with open(f'labeled_data/{filename}.py', 'rb') as f:
#     loaded_data = pickle.load(f)
#
# TODO: Add a way to load the data and continue labeling, so we don't start from at the beginning every time.

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

# Ensure the directory exists
os.makedirs('labeled_data', exist_ok=True)

# Check if there is any existing labeled data
existing_files = os.listdir('labeled_data')

# Save the data
filename = 'labeled_data.py'

with open(os.path.join('labeled_data', filename), 'ab') as f:
    pickle.dump((data), f)
print('Data saved to labeled_data/' + filename)
