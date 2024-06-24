class Panda: 
    def __init__(self , id : int , age:int, gender:str , weight:float) -> None: 
        self.id=id 
        self.age=age 
        self.gender=gender 
        self.weight=weight 
 
    def inc_age(self , years:int): 
        self.age+=years 
        print(f"Panda ID {self.id} is now {self.age} years old.") 
 
    def upd_weight(self , new_weight:float): 
        self.weight=new_weight 
        print(f"Panda ID {self.id} now weight {self.weight} kg")



'''

class panda: 
 
    def __init__(self, name:str, age:int, food:str ,weight:int , color:str) -> None: 
        self.name= name 
        self.age = age 
        self.food = food 
        self.weight=weight 
        self.color=color 

 

    def color(self , color:str): 
        print(f" panda name is {self.name} color  {color} visits") 


    def number(self , name):
        print(f" panda name is {self.name} number  {name} visits") 
'''

 
