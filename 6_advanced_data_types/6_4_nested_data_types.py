# NESTED DATA TYPES

guest1 = ("Bart", "Kowalski", 30)
guest2 = ("Thomas", "Anderson", 45)
guest3 = ("Andrew", "Jackson", 60)

guest_list = [
    guest1,
    guest2,
    guest3
]

print('Gust list: ', guest_list)
print('Third element on list: ', guest_list[2])

player1 = {"firstname": "Bart", "lastname": "Kowalski", "age": 30}
player2 = {"firstname": "Thomas", "lastname": "Anderson", "age": 45}
player3 = {"firstname": "Andrew", "lastname": "Jackson", "age": 60}

player_list = [
    player1,
    player2,
    player3
]

print('Players list: ', player_list)

player_list.append({"firstname": "Gregory", "lastname": "Johnson", "age": 55})
print('Updated players list: ', player_list)

# PROCESSING LIST IN LOOP - ASSIGN ITERATED DICTIONARY PROPERTIES INTO LOCAL VARIABLES
for firstname, lastname, age in guest_list:
    print(firstname, lastname, age)
    print("\n")
