# DEEP & SHALLOW COPY
# PREVENT TO CHANGE FUNCTION ORIGINAL ARGUMENTS
import copy


def clear_list(list_to_clear):
    print('Function argument id :', id(list_to_clear))
    print('Function argument nested object id: ', id(list_to_clear[0]))
    list_to_clear.clear()


# CLEAR ORIGINAL LIST PASSED INTO FUNCTION AS ARGUMENT
test_list = [1, 2, 3, 4]
clear_list(test_list)
print('Test list :', test_list)

# SHALLOW COPY
# DON'T CLEAR ORIGINAL LIST PASSED AS ARGUMENT - CREATED LIST COPY AS LOCAL VARIABLE INSTEAD
# NOT RECOMMENDED IF LIST CONTAINS NESTED OBJECTS EX. LIST OF LISTS - NESTED OBJECTS HAS SAME ID'S AS ORIGINAL OBJECTS
second_test_list = [[1, 2], [3, 4], [5, 6]]
print('Id of original second list: ', id(second_test_list))
print('Id of first element in second list: ', id(second_test_list[0][0]))

clear_list(second_test_list.copy())
print('Second test list :', second_test_list)

print("============================================")

# DEEP COPY
# REQUIRE TO IMPORT COPY PACKAGE
# RECOMMENDED IF LIST CONTAINS NESTED ELEMENTS (LIST OF LISTS) TO COPY ALL NESTED ELEMENTS (UNIQUE OBJECTS WITH NEW ID)
third_test_list = [[1, 2], [3, 4], [5, 6]]
print('Id of original third list: ', id(third_test_list))
print('Id of first element in third list: ', id(third_test_list[0][0]))

clear_list(copy.deepcopy(third_test_list))
print('Second test list :', third_test_list)
