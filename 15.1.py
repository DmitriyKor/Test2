class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            add_width = other.get_square() / self.height
            return Rectangle(self.width+add_width, self.height)
        else:
            return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            return Rectangle(self.width * n, self.height)

    def __str__(self):
        return f"{self.height}x{self.width}"


r1 = Rectangle(2, 4)
print(r1)
r2 = Rectangle(3, 6)
print(r2)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
print(r3)
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
print(r4)
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
