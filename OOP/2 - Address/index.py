from address import Address

Forte = Address(46555, 'Ternopil 5', 'Zhyvov 5', 55, 5)

print(Forte.index, ' - index')
print(Forte.town, ' - town')
print(Forte.street, ' - street')
print(Forte.house, ' - house')
print(Forte.office, ' - office')

Forte.changeindex(46000)
Forte.changetown('Ternopil')
Forte.changestreet('Zhyvov')
Forte.changehouse(32)
Forte.changeoffice(3)

print(Forte.index, ' - index')
print(Forte.town, ' - town')
print(Forte.street, ' - street')
print(Forte.house, ' - house')
print(Forte.office, ' - office')

Forte2 = Address(22222, 'Ternopil', 'Ruska', 22, 2)

del Forte2
print(Forte2.index, ' - index')