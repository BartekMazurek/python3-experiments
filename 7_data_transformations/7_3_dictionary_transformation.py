# DICTIONARY EXPRESSIONS

names = ["Bart", "Thomas", "Andrew"]

# {
#     KEY: VALUE
#     FOR ELEMENT IN ELEMENTS
#     CONDITION BASED ON ELEMENT
# }
#

names_length = {
    name: len(name)
    for name in names
    if name.startswith("B")
}

print('Names length that starts on B letter: ', names_length)

# 2
temperatures_in_celsius = {"t1": 25, "t2": 26, "t3": 30, "t4": 21, "t5": 35}

temperatures_in_fahrenheit = {
    key: ((celsius * 1.8) + 32)
    for key, celsius in temperatures_in_celsius.items()
    if celsius > 10
}
print('Temperatures conversed into celsius, higher than 10 degrees: ', temperatures_in_fahrenheit)
