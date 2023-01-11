class Test:

    def __init__(self, value: int):
        self.value = value

    def get_value(self) -> int:
        return self.value


class TestCompare:

    @staticmethod
    def get_difference_value(first: Test, second: Test) -> int:
        return first.get_value() - second.get_value()


firstValue: int = 10
secondValue: int = 15

test1 = Test(firstValue)
test2 = Test(secondValue)

difference = TestCompare.get_difference_value(test1, test2)

print(difference)
