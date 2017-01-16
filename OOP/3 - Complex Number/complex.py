class ComplNum:


    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, c1):
        a = self.a + c1.a
        b = self.b + c1.b
        c2 = ComplNum(a, b)
        return c2

    def subtraction(self, c1):
        a = self.a - c1.a
        b = self.b - c1.b
        c2 = ComplNum(a, b)
        return c2

    def multiplication(self, c1):
        a = self.a * c1.a - self.b * c1.b
        b = self.a * c1.b - self.b * c1.a
        c2 = ComplNum(a, b)
        return c2

    def division(self, c1):
        a = (self.a * c1.a + self.b * c1.b) / (c1.a * c1.a + c1.b * c1.b)
        b = (self.b * c1.a - self.a * c1.b) / (c1.a * c1.a + c1.b * c1.b)
        c2 = ComplNum(a, b)
        return c2

    def get(self):
        print('{:.2} + {:.2}i'.format(self.a, self.b))

    def __del__(self):
        del self