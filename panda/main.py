from panda import Panda
 
 
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