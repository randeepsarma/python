class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i+{self.y}j+{self.z}k"

    def __add__(self, nw):
        return Vector(self.x + nw.x, self.y + nw.y, self.z + nw.z)


one = Vector(1, 2, 3)
print(one)
two = Vector(4, 5, 6)
print(two)
# operator overloading means changing the meaning of operators
print(one + two)
