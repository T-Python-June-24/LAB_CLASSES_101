class Panda:
    def __init__(self, name:str, age:int, gender:str, location:str):
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location

    def eat(self,name:str,location:str,gender:int):
         self.location = location
         self.name = name
         self.gender = gender
         print(f"{name} is a {gender}.")
         print(f"{name}'location in {location}.")

    def sleep(self,name:str):
        self.name = name
        print(f"{self.name} is sleeping 🛌.")
        
if __name__ == "__main__":
    print("hello")
    