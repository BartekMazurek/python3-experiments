# NESTED DATA TYPES
# ADDING NEW ELEMENTS INTO DICTIONARY IS FASTER THAN ADDING ELEMENTS INTO LIST

ratings = {
    "Bart": (4, 4, 5, 3, 3),
    "Thomas": (5, 5, 4, 2, 3),
    "Andrew": (4, 3, 4, 1)
}

# for rating in ratings:
#     print(ratings[rating])

people = {
    "c4ca4238a0b923820dcc509a6f75849b": {"firstname": "Bart", "lastname": "Kowalski", "age": 30},
    "c81e728d9d4c2f636f067f89cc14862c": {"firstname": "Thomas", "lastname": "Anderson", "age": 45},
    "eccbc87e4b5ce2fe28308fd9f2a7baf3": {"firstname": "Andrew", "lastname": "Jackson", "age": 60}
}

# ITERATE THROUGH PEOPLE
# for person in people:
#     for key in people[person]:
#         keyName = key
#         keyValue = people[person][key]
#         print('Person ' + person + ' ' + keyName + ' ' + str(keyValue))

# ITERATE THROUGH PEOPLE - ALTERNATIVE
for _id, dictionary in people.items():
    for key in dictionary:
        print('Key: ', key, ', value: ', dictionary[key])
