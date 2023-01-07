# JSON
# json.dumps(data) - CONVERT VARIABLE DATA INTO JSON STRING
# json.dump(data, file_pointer, ensure_ascii=False) - SAVE DATA IN FILE AS JSON STRING
# indent - PROVIDES PRETTY PRINT FOR JSON STRING

import json

movie = {
    "title": "Movie 1",
    "release": 2022,
    "budget": 100000,
    "won_oscar": False,
    "actors": ("John Test", "Jessica Test"),
    "cast": {
        "director": "John Doe",
        "actor1": "Nicolas Test",
        "actor2": "Thomas Payne"
    }
}

# CONVERT DATA INTO JSON STRING
movie_json = json.dumps(movie, ensure_ascii=False, indent=4)
print("Json data: ", movie_json)

# SAVE DATA INTO FILE AS JSON STRING
with open("test_json", "w", encoding="UTF-8") as file:
    json.dump(movie, file, ensure_ascii=False, indent=4)
