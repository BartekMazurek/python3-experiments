# MUTABLE AND IMMUTABLE ARGUMENTS
# IMMUTABLE OBJECTS: bool, int, float, tuple, str

# FIRST EXAMPLE (IMMUTABLE)
# INT VARIABLES HAS DIFFERENT OBJECT ID
a = 4
b = a
b = 7

# PRINT DIFFERENT VALUES
print('A value: ', a)
print('B value: ', b)

# SECOND EXAMPLE (MUTABLE)
# PASSED list_sample MEMORY REFERENCE INTO list_sample_2
# LISTS HAS SAME IDS
list_sample = [1, 2, 3, 4]
list_sample_2 = list_sample
list_sample_2.append(5)

# PRINT SAME VALUES
print(list_sample)
print(list_sample_2)

print('Unique list_sample object id: ', id(list_sample))
print('Unique list_sample_2 object id: ', id(list_sample_2))


# THIRD EXAMPLE (MEMORY OPTIMISATION)
var1 = 10
var2 = 10

# WILL PRINT SAME VALUES BECAUSE 10 == 10 (SAME ID REFERENCE)
print('Var1 id value: ', id(var1))
print('Var2 id value: ', id(var2))
