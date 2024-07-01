from Pandas import Panda

def Name(self):
    print(f"My name is {self.name}")

def City(self):
    print(f"I live in {self.location}")

Panda1 = Panda("Ahmed", 23 , "Riyadh" , "Pizza")
Panda2 = Panda("Saleh", 28 , "Dammam" , "Pasta")
Panda3 = Panda("Nora", 21 , "Jizan" , "Kushri")
Panda4 = Panda("Mariam", 27 , "Makkah" , "Beriani")

print(Panda1.Name(), Panda1.City())
print(Panda2.Name(), Panda2.City())
print(Panda3.Name(), Panda3.City())
print(Panda4.Name(), Panda4.City())