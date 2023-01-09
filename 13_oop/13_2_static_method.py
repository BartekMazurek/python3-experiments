class TestClass:

    @staticmethod
    def get_sum(first, second):
        return first + second


test = TestClass()
result = test.get_sum(1, 3)

print(result)

test2 = TestClass.get_sum(3, 4)

print(result)
