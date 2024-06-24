
class Panda : 
    def __init__(self,gender:str ,weight:int,age:int,panda_species:str) -> None:
        self.gender = gender
        self.weight = weight
        self.age = age
        self.panda_species=panda_species
    def health(self)->str:
        if self.age<5 and  self.weight>=75 and self.weight<=110:
            return "\033[92mHealthy weight\033[0m"
        if (self.age>5 or self.age<15 ) and  self.weight>=90 and self.weight<=150:
            return "\033[92mHealthy weight\033[0m"
        if self.age>15  and  self.weight>=160 and self.weight<=170:
            return "\033[92mHealthy weight\033[0m"
        else:
            return "\033[1m\033[91m Unhealthy weight.\033[0m" 
    def panda_info(self)-> str:
        return f"pnanda species : {self.panda_species} of gender {self.gender}, with weight: {self.weight} KG, and  {self.age} years old , health status : {self.health()}"


