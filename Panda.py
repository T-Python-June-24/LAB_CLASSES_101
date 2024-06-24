class Panda:
    def __init__(self, name:str, age:int, height:float, weight:float) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def introduce(self):
        introdction = f"The panda is called {self.name}, and is {self.age} years old. It stands {self.height} meters tall and weighs about {self.weight} KG"
        return introdction
    
    def increment_age(self):
        self.age += 1
        message = f"{self.name} is now 1 year older!"
        return message
