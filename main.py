from class23 import Panda
from datetime import date

panda1= Panda("Koki", "Red", 10, date(2024, 5, 1))
panda2= Panda("Lucy", "Black & White", 18, date(2024, 2, 1))
panda3= Panda("Ash", "Black & White", 12, date(2024, 4, 1))
panda4= Panda("Simba", "Red", 23, date(2024, 1, 1))

#calling first method
print(panda1.describe())
print(panda2.describe())
print(panda3.describe())
print(panda4.describe())

#calling second method
print(panda1.book())
print(panda2.book())
print(panda3.book())
print(panda4.book())
print()

#accessing an attribute
print(f"Panda #2 name: {panda2.name}")

