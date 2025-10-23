import unittest

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def isTriangle(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def isIsosceles(self):
        return self.isTriangle() and (self.a == self.b or self.a == self.c or self.b == self.c)

    def isScalene(self):
        return self.isTriangle() and (self.a != self.b and self.a != self.c and self.b != self.c)

    def isEquilateral(self):
        return self.isTriangle() and (self.a == self.b == self.c)


class TestTriangulo(unittest.TestCase):

    def test_isTriangle_valid(self):
        t = Triangulo(3, 4, 5)
        self.assertTrue(t.isTriangle())

    def test_isTriangle_invalid(self):
        t = Triangulo(1, 2, 3)
        self.assertFalse(t.isTriangle())

    def test_isIsosceles(self):
        t = Triangulo(5, 5, 3)
        self.assertTrue(t.isIsosceles())

    def test_isScalene(self):
        t = Triangulo(7, 8, 9)
        self.assertTrue(t.isScalene())

    def test_isEquilateral(self):
        t = Triangulo(5, 5, 5)
        self.assertTrue(t.isEquilateral())


if __name__ == '__main__':
    unittest.main()
