import unittest


def add(a, b):
    luas = a*b*0.5
    print(luas)
    return luas


def sayHello():
    return "hello"


class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 7.5)

    def test_not_equal(self):
        self.assertNotEqual(add(5, 3), 8)

    def test_greater(self):
        self.assertGreater(add(5, 3), 6)

    def test_greater_equal(self):
        self.assertGreaterEqual(add(5, 3), 7.5)


class TestSayHello (unittest.TestCase):
    def test_hello(self):
        self.assertEqual(sayHello(), "hello")

    def test_not_equal(self):
        self.assertNotEqual(sayHello(), "hai")


if __name__ == '__main__':
    unittest.main()
