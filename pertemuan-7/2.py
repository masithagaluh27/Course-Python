import logging
logging.basicConfig(level=logging.DEBUG)


def add(a, b):
    logging.debug(f"a: {a}, b: {b}")
    return a + b


print(add(5, 3))
