from worker import *
from actions import *

c1 = Circle(1)
c2 = Circle(2)

print(c1.rad, ' - radius с1')
print(c1.centre, ' - centre с1')
print(c2.rad, ' - radius с2')
print(c2.centre, ' - centre с2')

c1.move(3,3)
c1.resize(3)
c2.move(4,4)
c2.resize(4)

print(c1.rad, ' - radius с1')
print(c1.centre, ' - centre с1')
print(c2.rad, ' - radius с2')
print(c2.centre, ' - centre с2')

r1 = Rectangle(1,1)
r2 = Rectangle(2,2)

print(r1.width, ' - width r1')
print(r1.height, ' - height r1')
print(r1.centre, ' - centre r1')
print(r2.width, ' - width r2')
print(r2.height, ' - height r2')
print(r2.centre, ' - centre r2')

r1.move(3,3)
r1.resize(3,3)
r2.move(4,4)
r2.resize(4,4)

print(r1.width, ' - width r1')
print(r1.height, ' - height r1')
print(r1.centre, ' - centre r1')
print(r2.width, ' - width r2')
print(r2.height, ' - height r2')
print(r2.centre, ' - centre r2')

s1 = Square(1)
s2 = Square(2)

print(s1.side, ' - side s1')
print(s1.centre, ' - centre s1')
print(s2.side, ' - side s2')
print(s2.centre, ' - centre s2')

s1.move(3,3)
s1.resize(3)
s2.move(4,4)
s2.resize(4)

print(s1.side, ' - side s1')
print(s1.centre, ' - centre s1')
print(s2.side, ' - side s2')
print(s2.centre, ' - centre s2')