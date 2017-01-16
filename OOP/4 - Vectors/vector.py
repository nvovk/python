from math import sqrt,cos

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def addition(self, a):
        x = self.x + a.x
        y = self.y + a.y
        z = self.z + a.z
        b = Vector(x, y, z)
        return b

    def subtraction(self, a):
        x = self.x - a.x
        y = self.y - a.y
        z = self.z - a.z
        b = Vector(x, y, z)
        return b

    def length(self):
        d = sqrt(self.x * self.x + self.y * self.y)
        return d

    def multiplication(self, a):
        d = self.x * a.x + self.y * a.y + self.z * a.z
        return d

    def angle(self, b):
        ma = Vector.length(self)
        mb = Vector.length(b)
        d = self.multiplication(b)
        ang = d / (ma * mb)
        c = cos(ang)
        return c

    def get(self):
        print(self.x, self.y, self.z)

    def __del__(self):
        del self