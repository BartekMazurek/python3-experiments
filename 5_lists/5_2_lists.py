test_list = ["John", "Max", "Thomas", "Bart", "Donald"]

# GET LIST LENGTH - len()
list_length = len(test_list)
print(list_length)

# APPEND NEW ELEMENT AT THE END OF THE LIST - append()
test_list.append("Mark")
print(len(test_list))
print("Append: ", test_list)

# EXTEND LIST WITH NEW LIST ELEMENT - extend()
test_list.extend(["Anthony"])
print(len(test_list))
print("Extend: ", test_list)

# INSERT NEW ELEMENT - insert()
test_list.insert(0, "Andrew")
print("Insert: ", test_list)

# GET SPECIFIED ELEMENT INDEX VALUE (ONLY FIRST OCCURRENCE) - index()
index_value = test_list.index("Max")
print("Index value: ", index_value)

# SORT LIST - sort()
test_list.sort()
print("Sorted list: ", test_list)

# REMOVE LAST ELEMENT FROM LIST - pop()
test_list.pop()
print("Updated list after pop: ", test_list)

# REMOVE ELEMENT FIRST OCCURRENCE FROM LIST - remove()
test_list.remove("Andrew")
print("Updated list after remove: ", test_list)

# REVERSE LIST ELEMENTS ORDER
test_list.reverse()
print("Reversed list: ", test_list)

# CLEAR LIST
test_list.clear()
print("Cleared list: ", test_list)
