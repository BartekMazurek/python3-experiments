test_list = [1, "1", "{'test': 1}", False]

# PRINT ALL ELEMENTS IN LIST
for i in test_list:
    print(i)

# OVERWRITE ELEMENT VALUE
test_list[3] = True

for i in test_list:
    print(i)

# CHECK LIST FOR SPECIFIED ELEMENT
element_to_check = "1"
is_element_on_list = element_to_check in test_list

print(is_element_on_list)

second_element_to_check = "2"
is_second_element_on_list = second_element_to_check in test_list

print(is_second_element_on_list)
