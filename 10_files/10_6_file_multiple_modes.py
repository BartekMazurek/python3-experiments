# FILE MULTIPLE MODES
# r+ - FOR READ & WRITE
# w+ - FOR WRITE & READ (WILL ERASE EXISTING FILE CONTENT OR CREATE NEW ONE IF NOT EXIST)
# a+ - FOR APPEND & READ (FILE POINTER IS ALWAYS AT THE END OF THE FILE)

# r+
# with open("file1.txt", "r+") as file:
#     file.write("Content in r+ mode\n")

# w+
# with open("file1111.txt", "w+") as file:
#     file.write("Content in w+ mode\n")

# a+
with open("file1.txt", "a+") as file:
    file.write("Content in a+ mode\n")
    print(file.tell())
