class NotIntegerError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"{value} is not an integer!")

args = (1, 'h', 3, 'a')

try:
    for arg in args:
        if not isinstance(arg, int):
            raise NotIntegerError(arg)
except NotIntegerError as e:
    print(f"Caught exception: {e}")


