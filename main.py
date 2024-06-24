from animal import Panda

panda1 = Panda("Pat",5,"America","white")
panda2 = Panda("Juli",4,"Rusia","grey")
panda3 = Panda("Gowi",10,"Australia","white")
panda4 = Panda("Poam",2,"China","green")

print(panda1.name)
print(panda1.introduce())
panda1.allowedToRace()

print(panda2.name)
print(panda2.introduce())
panda2.allowedToRace()

print(panda3.name)
print(panda3.introduce())
panda3.allowedToRace()

print(panda4.name)
print(panda4.introduce())
panda4.allowedToRace()