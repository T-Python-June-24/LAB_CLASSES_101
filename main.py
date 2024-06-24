from Panda import Panda
panda_1 = Panda("White", 7, 2.2, 300)
print(panda_1.introduce())
print(panda_1.increment_age())
print(f"{panda_1.name} is {panda_1.age} years old.")
print()

panda_2 = Panda("WhiteBlack", 14, 2.5, 370)
print(panda_2.introduce())
print(panda_2.increment_age())
print(f"{panda_2.name} is {panda_2.age} years old.")
print()

panda_3 = Panda("Black", 9, 2.3, 280)
print(panda_3.introduce())
print(panda_3.increment_age())
print(f"{panda_3.name} is {panda_3.age} years old.")
print()

panda_4 = Panda("BlackWhite", 1, 1.2, 120)
print(panda_4.introduce())
print(panda_4.increment_age())
print(f"{panda_4.name} is {panda_4.age} years old.")
