import json
import os

# changing the directory
os.chdir("C:/Users/sri-krishna/Desktop")

# reading from file
with open('test.json', 'r')as fileobj:
    json_data = json.load(fileobj)

file_dict = json_data['backends']
final_dict = {}
# print(file_dict)
# print(json.dumps(json_data, indent=4, sort_keys=True))

# modifying the dictionary
for index, item in enumerate(file_dict):
    for key, value in item.items():
        if key == "properties":
            for index1, item1 in enumerate(value):
                for key1, value1 in item1.items():
                    new_key = str(key1) + '_' + str(index) + '_' + str(index1)
                    final_dict[new_key] = item1[key1]
        else:
            new_key = str(key) + '_' + str(index)
            final_dict[new_key] = item[key]


for key, value in final_dict.items():
    print(str(key) + ':' + str(value))
# print(final_dict)
