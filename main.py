from panda import Panda
# creating instances
panda1 = Panda("Pem", 5, 100, "strawberry")
panda2 = Panda("Meme", 3, 85, "Apples")
panda3 = Panda("Lila", 7, 120, "carrot")
panda4 = Panda("Tala", 2, 70, "Carrots")

#printing one attribute value 
print(panda1.name)

# calling the two methods on each instance
panda_list = [panda1, panda2, panda3, panda4]

for panda in panda_list:
  panda.eat()
  panda.sleep()