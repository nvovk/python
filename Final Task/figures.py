class Circle:

    def __init__(self, rad):
        self.rad = rad
        self.centre = [0, 0]

    def resize(self, rad):
        self.rad += rad

    def move(self, osx, osy):
        self.centre[0] += osx
        self.centre[1] += osy


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.centre = [0, 0]

    def resize(self, width, height):
        self.width += width
        self.height += height

    def move(self, osx, osy):
        self.centre[0] += osx
        self.centre[1] += osy


class Square:

    def __init__(self, side):
        self.side = side
        self.centre = [0, 0]

    def resize(self, side):
        self.side += side

    def move(self, osx, osy):
        self.centre[0] += osx
        self.centre[1] += osy