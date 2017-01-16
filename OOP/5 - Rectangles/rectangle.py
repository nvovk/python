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
        h1 = self.height()
        h2 = r.height()
        w1 = self.width()
        w2 = r.width()
        a1 = [0, 0]

        if h1 >= h2:
            c1 = [w1 + w2, h1]
            r1 = Rectangle(a1, c1)
        else:
            c1 = [w1 + w2, h2]
            r1 = Rectangle(a1, c1)

        if w1 >= w2:
            c1 = [w1, h1 + h2]
            r2 = Rectangle(a1, c1)
        else:
            c1 = [w2, h1 + h2]
            r2 = Rectangle(a1, c1)

        if r1.size() >= r2.size():
            return r1
        else:
            return r2

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