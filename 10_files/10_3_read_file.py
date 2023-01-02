# READ FILE

# OPEN FILE & GET ALL CONTENT INTO VARIABLE
# with open("file1.txt", "r", encoding="UTF-8") as file:
#     content = file.read()
#     print('All content :', content)

# OPEN FILE & GET ALL CONTENT INTO VARIABLE WITH SPLIT LINES AS LIST ELEMENTS
# with open("file1.txt", "r", encoding="UTF-8") as file:
#     content = file.read().splitline()
#     print('All content :', content)

# OPEN FILE & GET ALL CONTENT INTO VARIABLE
with open("file1.txt", "r", encoding="UTF-8") as file:
    print('Single line from file: ', file.readline())

# OPEN FILE & GET ALL CONTENT INTO VARIABLE
# with open("file1.txt", "r", encoding="UTF-8") as file:
#     print('Multiple lines :', file.readlines())
