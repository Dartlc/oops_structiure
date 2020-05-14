from models.get_value import GetValue


class OddEven:
    def __init__(self):
        obj = GetValue()
        input_value = obj.getting_integer_value()
        if input_value % 2 == 0:
            print(f"{input_value} is even number")
        else:
            print(f"{input_value} is odd number")


if __name__ == '__main__':
    obj = OddEven()
