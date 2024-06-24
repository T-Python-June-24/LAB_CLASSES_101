from Panda import Panda
print("\033[1m\033[94m=== Welcom to the panda care program ==\033[0m")

print("here are the statistics :......... ")
panda1 = Panda("female", 75, 7, "giant panda")
panda2 = Panda("male", 165, 16, "red panda")
panda3 = Panda("male", 50, 4, "giant panda")
panda4 = Panda("female", 98, 13, "red panda")
print(f"the first panda is : {panda1.panda_species}")
print(panda1.panda_info())
print(panda2.panda_info())
print(panda3.panda_info())
print(panda4.panda_info())