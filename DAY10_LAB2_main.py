

from panda import Panda


panda1 = Panda("Bao", "Male", 5, 100)
panda2 = Panda("Ling", "Female", 8, 120)
panda3 = Panda("Tian", "Male", 6, 110)
panda4 = Panda("Zi", "Female", 4, 90)



pandas = [panda1, panda2, panda3, panda4]

for panda in pandas:
    print(f"Name: {panda.name}")
    print(f"Gender: {panda.gender}")
    print(f"Age: {panda.age}")
    print(f"Weight: {panda.weight}\n")




print(panda3.eat("bamboo"))
print(f"\n{panda2.name} and {panda1.name} {panda.sleep(10)}\n")