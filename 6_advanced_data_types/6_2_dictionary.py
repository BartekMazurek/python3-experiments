# DICTIONARY
# KEY:VALUE DATA STRUCTURE
# KEY MUST BE UNIQUE

# FIRST DICTIONARY
test_dictionary = {
    1: "Firstname Lastname",
    2: "Firstname2 Lastname2",
    3: "Firstname3 Lastname3",
    4: "Firstname4 Lastname4",
}

# PRINT ALL ELEMENTS IN DICTIONARY
print("All elements: ", test_dictionary)

# PRINT SPECIFIED ELEMENT
print(test_dictionary[2])
print(test_dictionary.get(2))

# ADD NEW ELEMENT INTO DICTIONARY
test_dictionary.update({5: "Firstname5 Lastname5"})

# DELETE ELEMENT WITH SPECIFIED KEY
test_dictionary.pop(1)

# DELETE LAST ELEMENT IN DICTIONARY
test_dictionary.popitem()

print("All elements: ", test_dictionary)
