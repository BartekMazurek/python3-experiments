# APPEND DATA INTO FILE
# a - APPEND DATA MODE

with open("file1.txt", "a") as file:
    file.write("Content\n")
    print(file.tell()) # PRINT FILE READ POINTER LAST POSITION NUMBER
