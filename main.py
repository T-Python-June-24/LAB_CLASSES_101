from Panda import Panda


try:

    # four instance of panda 
    panda1 = Panda("Mei",77)
    panda2 = Panda("Lun",88)
    panda3 = Panda("Xi",67)
    panda4 = Panda("Yuan",89)

    panda1.DisplyPandaProfile()
    panda2.DisplyPandaProfile()
    panda2.fight(50)
    panda2.moveUp(20)
    print("\033[32m\n The number of created pandas = ",panda1.numberOfPanda,end="\n")

except Exception as e :

    print(f'''\033[31m
    Error: {e}       
    ''')