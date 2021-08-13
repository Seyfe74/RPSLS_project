
from random import seed
from player import Player
#from random import randint
import random
class Ai(Player):
    def __init__ (self,name):
        super().__init__(name)
# prepare a sequence
    def comp_choice(self):
        return(random.choice(self.gesture))
        
# make choices from the sequence

        
       
           