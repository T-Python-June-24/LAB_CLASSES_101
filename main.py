from panda_class import Panda

panda1 = Panda("abdullah", 5, "Male", "Makkah")
panda2 = Panda("Ahmed", 3, "Male", "Riyadh")
panda3 = Panda("Sarah", 4, "Female", "Jeddah")
panda4 = Panda("Rahaf", 2, "Female", "Makkah")

print(f"The Panda 1 Panda Name is{panda1.name} And His Age is {panda1.age} And His Gender is {panda1.gender}And His Location is {panda1.location}")
print("----------")
print(f"The Panda 2 Name is{panda1.name} And His Age is {panda1.age} And His Gender is {panda1.gender}And His Location is {panda1.location}")
print("----------")
print(f"The Panda 3 Name is{panda1.name} And His Age is {panda1.age} And His Gender is {panda1.gender}And His Location is{panda1.location}")
print("----------")
print(f"The Panda 4 is{panda1.name} And His Age is {panda1.age} And His Gender is {panda1.gender}And His Location is {panda1.location}")
print("----------")
panda1.eat()
print("----------")
panda4.sleep()
print("----------")