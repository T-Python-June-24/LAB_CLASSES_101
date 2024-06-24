class Panda:
    def __init__(self, name:str, age:int, gender:str, location:str):
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location

    def eat(self):
        print(f"{self.name} is a {self.gender}.")
        self.location 
        print(f"{self.name}'location in {self.location}.")

    def sleep(self):
        print(f"{self.name} is sleeping 🛌.")