from panda import panda
 
 
def main(): 
    Panda1=Panda(15 , 20 , "male" , 112.5) 
    Panda2=Panda(42 , 10 , "male" , 100.0) 
    Panda3=Panda(6 , 30 , "male" , 114.5) 
    Panda4=Panda(22 , 40 , "male" , 120.5) 
 
    print(f"Panda1: ID {Panda1.id}") 
    print(f"Panda2: age {Panda2.age}") 
    print(f"Panda3: gender {Panda3.gender}") 
    print(f"Panda4: weight {Panda4.weight}") 
 
    Panda1.inc_age(5) 
    Panda1.upd_weight(120) 
 
    Panda2.inc_age(10) 
    Panda2.upd_weight(100) 
 
    Panda3.inc_age(20) 
    Panda3.upd_weight(111) 
 
    Panda4.inc_age(22) 
    Panda4.upd_weight(115) 
 
main()
























'''
from panda import panda

panda1 = panda("marco", 5, "cereal" , 10 , "black") 
panda2 = panda("coco", 7, "cereal" , 15 ,"red") 
panda3 = panda("minig", 19,"leaves", 60,"yello") 
panda4 = panda("mincoch", 30,"leaves", 100, "white") 
 
 
print(panda1.name) 
print(panda3.age)
print(panda3.food)
print(panda3.weight)


panda1.color("black")
panda1.number(1)

panda2.color("red")
panda2.number(2)

panda3.color("yellow")
panda3.number(3)

panda4.color("white")
panda4.number(4)

'''