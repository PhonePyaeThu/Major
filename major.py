import json
import os
import time
import datetime
# Load the JSON file
with open('durov.json', 'r') as file:
    data = json.load(file)

print("This script is modified by Bhone Pyae Thu")
print("Join my group: https://t.me/+yl_GWf4azeNmODA9 ")
print("example : 2 3 17 18")
'''
puzzle_input = input("Enter puzzle code: ")

# Get the current date
current_date = datetime.datetime.now()

# Format the date in a specific format, e.g., YYYY-MM-DD
formatted_date = current_date.strftime("%Y-%m-%d")

puzzle_list = [int(num) for num in puzzle_input.split()]
data['puzzle'] = puzzle_list
data['date'] = formatted_date
with open("durov.json", "w") as file:
    json.dump(data, file, separators=(',', ':'))
    
    
# Save the modified data back to the JSON file
with open('durov.json', 'w') as file:
    json.dump(data, file, indent=4)
'''
def load_data():
    try:
        with open('durov.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('durov.json', 'w') as file:
        # Use separators to minimize space and avoid indenting
        json.dump(data, file, separators=(',', ':'))

def main():
    # Load existing data from the file
    data = load_data()
    
    # Take input from the user
    input_date = input("Enter the date (YYYY-MM-DD): ")
    puzzle_input = input("Enter puzzle code : ")
    puzzle_list = [int(num) for num in puzzle_input.split()]
    
    # Update the data dictionary with the new entries
    data['date'] = input_date
    data['puzzle'] = puzzle_list
    
    # Save the updated data back to the file
    save_data(data)
    
if __name__ == '__main__':
    main()

print("Major puzzle code successfully added!")
time.sleep(1)
print("This script is modified by Bhone Pyae Thu")
time.sleep(1)
os.system('clear')
os.system('python3 bot.py')