import string


class Test:

    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

        return {
            "isSuccess": True,
            "message": "Value has been set",
            "value": value
        }


test = Test()
result = test.set_value(100)

print(result)


class Result:

    def __init__(self, is_success: bool, message: string, value: int):
        self.is_success = is_success
        self.message = message
        self.value = value


class Test2:

    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

        return Result(
            True,
            "Value has been set",
            value
        )


test2 = Test2()
result2 = test.set_value(200)

print(result2)
