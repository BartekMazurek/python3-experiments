import string


class User:
    firstname = "Firstname"


user1 = User()
user2 = User()
user3 = User()

# WILL CHANGE FIRSTNAME IN ALL OBJECTS (STATIC VARIABLE)
User.firstname = "Test"

print(user1.firstname)
print(user2.firstname)
print(user3.firstname)


class User2:
    firstname = "Firstname"

    def __init__(self, firstname: string):
        self.firstname = firstname

    def get_firstname(self) -> string:
        return self.firstname


user4 = User2("User4")
user5 = User2("User5")

print(user4.get_firstname())
print(user4.firstname)

print(user5.get_firstname())
print(user5.firstname)
