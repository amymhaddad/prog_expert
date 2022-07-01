def add_one(func):
    def wrapper(x, y):
        result = func(x, y)
        return result + 1

    return wrapper


@add_one
def add_values(x, y):
    return x + y


print(add_values(1, 2))
