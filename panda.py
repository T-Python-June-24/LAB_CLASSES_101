class Panda:

  # intilize constructor 
  def __init__(self, name:str, age:int, weight:float, favorite_food:str) -> None:
    # atrributes
    self.name = name
    self.age = age
    self.weight = weight
    self.favorite_food = favorite_food

  # methods
  def eat(self):
    print(f"The {self.name} is eating {self.favorite_food}")

  def sleep(self):
    print(f"{self.name} panda is sleeping now")