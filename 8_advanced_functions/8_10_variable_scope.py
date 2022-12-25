# VARIABLE SCOPE

def some_function():
    print(variable)


# GLOBAL VARIABLE
variable = 10
some_function()


# GLOBAL VARIABLE WILL BE OVERWRITTEN - global CLAUSE
def second_function():
    global variable2
    variable2 = variable2 + 1
    print(variable2)


# GLOBAL VARIABLE AVAILABLE TO OVERWRITE IN FUNCTION
variable2 = 15

print(variable2)
second_function()
print(variable2)
