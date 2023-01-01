# OPEN FILE 2
# OPEN FILE HANDLER & ASSIGN CONTENT INTO file VARIABLE
# FILE WILL BE CLOSED AUTOMATICALLY
# DATA IN FILE WILL BE OVERWRITTEN

with open("file.txt", "w") as file:
    file.write("Another test content with new method")
