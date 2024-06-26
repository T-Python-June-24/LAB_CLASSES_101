# # LAB_CLASSES_101


# ## Using what you learned about classes , create a class to represent a Panda. The class should have the following:
# - 4 Attributes
# - 2 Methods


# ### Create 4 instances/objects of the class Panda , print 1 attribute value,  and call the two methods on each instance. 
# #### Note:
# Arrange your code in seperate files (one for the main file for main logic , and another for the definition of the class). 



class Panda:

    def __init__(self, name:str, gender:str, age:int, weight:float) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight



    def eat(self, food):
        return f"{self.name} is eating {food}"

    def sleep(self, hours):
        return f"{self.name} is sleeping for {hours} hours"
