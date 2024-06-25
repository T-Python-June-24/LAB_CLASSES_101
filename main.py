from panda import Panda

def main():
    # Create 4 Panda instances
    panda1 = Panda(name="panda1", age=5, weight=100)
    panda2 = Panda(name="panda2", age=7, weight=120)
    panda3 = Panda(name="panda3", age=8, weight=110)
    panda4 = Panda(name="panda4", age=6, weight=105)
   
    # Print the name attribute of each panda
    print(f"Panda name: {panda1.name}")
    print(f"Panda name: {panda2.name}")
    print(f"Panda name: {panda3.name}")
    print(f"Panda name: {panda4.name}")

    # Call the eat method
    panda1.eat()
    panda2.eat()
    panda3.eat()
    panda4.eat()
    
    # Call the sleep method
    panda1.sleep()
    panda2.sleep()
    panda3.sleep()
    panda4.sleep()

if __name__ == "__main__":
    main()