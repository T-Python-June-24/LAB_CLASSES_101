class Panda: # for gameing application
    
    numberOfPanda = 0 

    def __init__(self,name:str,weight:float) -> None:
        
        self.name = name 
        self.weight = weight
        self.posision = [0,0] # (x,y) default position on start a game 
        self.isAlive = True # default value on start a game 
        self.health = 100
        self.numberOfPanda += 1 # increment every time when create an instance 
    

    def moveUp(self,distance):
        oldPostion = [self.posision[0],self.posision[1]] # [x,y]
        self.posision[1] = self.posision[1] + distance  # i do not know how to move a player but assume that 
        print(f"{self.name} move {distance} feet up from ({oldPostion[0]},{oldPostion[1]}) to ({self.posision[0]},{self.posision[1]})")


    def moveRight(self,distance):
        oldPostion = [self.posision[0],self.posision[1]] # [x,y]
        self.posision[0] = self.posision[0] + distance  # i do not know how to move a player but assume that 
        print(f"{self.name} move {distance} feet right from ({oldPostion[0]},{oldPostion[1]}) to ({self.posision[0]},{self.posision[1]})")

    def fight(self,damge): # simulate a fighting 

        if self.isAlive and (damge > 0 and damge <= 100 ): 
            
            if damge > self.health:
                
                print(f'''\033[31m
            The panda: {self.name} can't figh with damge = {damge} becuase it is health is low you should level up         
            ''')
            
            else:

                self.health = self.health - damge 
                
                if self.health == 0:
                    self.isAlive = False
                    print(f''' \033[33m
            The panda named {self.name} has died
            ''')
                else :
                    print(f'''\033[33m
            Panda health of {self.name} after fight = {self.health}             
            ''')  
                      
        else:

            print(f'''\033[31m
            The panda: {self.name} can't figh becuase is dead         
            ''')
            
    def DisplyPandaProfile(self):

        if self.isAlive:

            print(f'''\033[32m
        Panda name: {self.name} 

        Panda weight: {self.weight}

        Panda health: {self.health}   
              ''')
        else:
            print(f''' \033[33m
        The panda named {self.name} has died
        ''')



