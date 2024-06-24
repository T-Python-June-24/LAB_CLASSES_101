class Panda:
    def __init__(self,name:str, age:int, origin:str, color:str) -> None:
        self.name = name
        self.age = age
        self.origin = origin
        self.color = color

    def introduce(self):
        return f"{self.name} is {self.age} years old, {self.color} and of origin, {self.origin}."
    
    def allowedToRace(self):
        if self.color == "white":
            print(f"The panda {self.name} is allowed to participate in the race.")
        else:
            print(f"The panda {self.name} is NOT allowed to participate in the race.")
    