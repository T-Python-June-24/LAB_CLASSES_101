class Panda:


    def _init_(self , number:int , age:int , gender:str , location:str )-> None:
        self.number=number
        self.age=age
        self.gender=gender
        self.location=location


    def Visit(self , visit:int):
        print(f"Panda No. {self.number} gets {visit} visits")

    def weight(self , weight:float):
        print(f"Panda No.{self.number} weighs {weight} kg")