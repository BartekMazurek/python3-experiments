# DEFINE EMPTY CLASS WITHOUT ANY PROPERTY OR METHOD
class User:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class UsersCollection:

    def __init__(self, users_collection):
        self.users = users_collection

    def __getitem__(self, key):
        return self.users[key]

    def __setitem__(self, key, value):
        self.users[key].name = value


user1 = User('User1', 16)
user2 = User('User2', 22)

# print(user1.get_name())
# print(user2.get_name())
#
# print(user1.get_age())
# print(user2.get_age())

users = [User('Test', 10) for _ in range(5)]
# print(users)

# PYTHON DUNDER (DOUBLE UNDERSCORE) SET & GET ITEM METHODS USAGE
collection = UsersCollection(users)
collection[0] = 'Test2'
collection[1] = 'Test3'

print(collection[0].name)
