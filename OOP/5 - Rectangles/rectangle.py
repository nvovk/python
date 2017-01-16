class Rectangle:

    def __init__(self, a, c):
        self.a = a
        self.c = c
        self.b = [a[0], c[1]]
        self.d = [c[0], a[1]]

    def get(self):
        print(self.a, ' - A')
        print(self.b, ' - B')
        print(self.c, ' - C')
        print(self.d, ' - D')

    def move(self, osx, osy):
        self.a[0] += osx
        self.b[0] += osx
        self.c[0] += osx
        self.d[0] += osx
        self.a[1] += osy
        self.b[1] += osy
        self.c[1] += osy
        self.d[1] += osy

    def resize(self, w, h):
        self.c[0] += w
        self.d[0] += w
        self.c[1] += h
        self.b[1] += h

    def plus(self, r):

        if self.height() >= r.height():

        else:

        if self.width() >= r.width():
            a1 = self.a
            c1 = [self.c[0], self.c[1] + r.height()]
            r3 = Rectangle(a1,c1)
        else:
            a1 = self.a
            c1 = [self.c[0], self.c[1] + r.height()]
            r4 = Rectangle(a1, c1)







    def height(self):
        return abs(self.a[1]-self.b[1])

    def width(self):
        return abs(self.a[0] - self.d[0])

    def size(self):
        return self.height() * self.width()




class Square:

    def __init__(self, side):
        self.side = side
        self.centre = [0, 0]

    def resize(self, side):
        self.side += side

    def move(self, osx, osy):
        self.centre[0] += osx
        self.centre[1] += osy