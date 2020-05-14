class GetValue:
    def getting_integer_value(self):
        while True:
            try:
                x = int(input("Enter the number: "))
                return x
            except Exception as e:
                print(f"error: {e}")
                continue

    def getting_string(self):
        x = input("Enter the value: ")
        return x

    def getting_float_value(self):
        while True:
            try:
                x = float(input("Enter the number: "))
                return x
            except Exception as e:
                print(f"error: {e}")
                continue