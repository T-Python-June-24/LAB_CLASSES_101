
class Panda:
    def __init__(self, name, age, weight, habitat):
        self.name = name
        self.age = age
        self.weight = weight
        self.habitat = habitat
    
    def eat(self, food):
        return f"{self.name} is eating {food}."
    
    def sleep(self, hours):
        return f"{self.name} is sleeping for {hours} hours."
