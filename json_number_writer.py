import json

numbers = [2,4,6,8,10,12]

filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)