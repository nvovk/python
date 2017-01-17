from rectangle import Rectangle

A0 = [0, 0]
C0 = [3, 1]

print('Rectangle:')
r0 = Rectangle(A0, C0)
r0.get()

print('Move for 1 point OX and 1 point OY:')
r0.move(1, 1)
r0.get()

print('Resize for 1 point OX and 1 point OY:')
r0.resize(1, 1)
r0.get()

A1 = [1, 1]
C1 = [3, 5]

A2 = [1, 1]
C2 = [4, 3]

r1 = Rectangle(A1, C1)
r2 = Rectangle(A2, C2)

print('Rectangle 1:')
r1.get()

print('Rectangle 2:')
r2.get()

r = r1.plus(r2)
print('Rectangle 1 plus 2:')
r.get()

r = r1.common(r2)
print('Rectangle 1 and 2 (common scale):')
r.get()