# FETCH JSON FROM SOURCE
# json.loads(json_string) - CONVERT JSON STRING INTO PYTHON DATA TYPE
# json.load(file_pointer) - LOAD JSON STRING FROM FILE AND RETURN RESULT AS PYTHON DATA TYPE

import json
import pprint

# FETCH DATA FROM JSON AND CONVERT INTO PYTHON DATA TYPE
data = json.loads('{"title": "Movie 1", "release": 2022, "budget": 100000, "won_oscar": false, "actors": '
                  '["John Test", "Jessica Test"], "cast": {"director": "John Doe", "actor1": "Nicolas Test",'
                  ' "actor2": "Thomas Payne"}}')
# print('Converted json data: ', data)
pprint.pprint(data)

# FETCH JSON DATA FROM FILE AND CONVERT INTO PYTHON DATA TYPE
with open("test_json", encoding="UTF-8") as file:
    data_2 = json.load(file)

# print('Fetched data from file: ', data_2)
pprint.pprint(data_2)
