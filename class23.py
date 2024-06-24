from datetime import date

class Panda:
    def __init__(panda, name:str, color:str, weight:int, age:date):
        panda.name=name
        panda.color=color
        panda.weight=weight
        today = date.today()
        panda.age=today.month - age.month

    
    def describe(panda) -> str:
        return f"Hello I'm a {panda.color} Panda and my name is '{panda.name}'.\nI have {panda.weight} KG, and {panda.age} months old\n"
    
    def book(panda) -> str:
        return f"You have successfully booked a visit to see {panda.name}!"