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




