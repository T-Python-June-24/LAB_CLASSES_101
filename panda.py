class Panda:
    # 4 attributes
    def __init__(self, name, age, color, gender):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender

    # 2 methods
    def fight(self, other_panda):
        if self.gender == "male" and other_panda.gender == "female":
            print(f"{self.name} is fighting with {other_panda.name}")
        else:
            print(f"{other_panda.name} is fighting with {self.name}")
    
    def walk(self):
        print(f"{self.name} is walking")