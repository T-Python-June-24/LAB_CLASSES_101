from panda import Panda

# create 4 instances
panda1 = Panda("Mimi", 10, "Black", "Male")
panda2 = Panda("Zozo", 15, "Red", "Female")
panda3 = Panda("Kiki", 20, "Red", "Male")
panda4 = Panda("Lulu", 25, "Black", "Female")

#print an attribute 
print(panda1.name)

#call 2 methods
panda1.fight(panda2)
panda1.walk()