import json

numbers = [i for i in range(1, 101, 2)]

with open("numbers.json", 'w') as file:
    json.dump(numbers, file)
