import json

numbers=[2,3,5,7,11,13]
cars=100

filename='number.json'
with open(filename,'w') as file_j:
    json.dump(numbers,file_j)
