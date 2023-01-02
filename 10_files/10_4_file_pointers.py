# FILE POINTERS
# tell - INFORM WHERE WAS THE LAST OPERATION ON FILE
# seek - SEARCH & REPLACE IN DEFINED PLACE

with open("file1.txt") as file:
    print(file.readline())
    print(file.tell()) # TELLS POINTER POSITION NUMBER AFTER READING 1 LINE FROM FILE
