class Test:

    first = 0
    second = 0

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second


class Test2(Test):

    third = 0

    def __init__(self, first, second, third):
        super().__init__(first, second)
        self.third = third

    def get_third(self):
        return self.third

    def get_sum(self):
        return super().get_first() + super().get_second() + self.third


test = Test2(10, 20, 30)

print(test.get_first(), test.get_second(), test.get_third(), test.get_sum())
