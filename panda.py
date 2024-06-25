class Panda:
    def __init__(self, name, age, weight, is_hungry=True):
        self.name = name
        self.age = age
        self.weight = weight
        self.is_hungry = is_hungry
    
    def eat(self):
        if self.is_hungry:
            print(f"{self.name} is eating now.")
            self.is_hungry = False
        else:
            print(f"{self.name} is not hungry right now.")
    
    def sleep(self):
        print(f"{self.name} is now sleeping.")
    
    