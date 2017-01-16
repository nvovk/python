from vector import Vector

a = Vector(1, 1, 1)
b = Vector(6, 6, 6)

k1 = a.addition(b)
k2 = a.subtraction(b)
k3 = a.length()
k4 = a.multiplication(b)
k5 = a.angle(b)

k1.get()
k2.get()
print(k3)
print(k4)
print(k5)