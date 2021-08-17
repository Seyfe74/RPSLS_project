

from player import Player
from gesture import Gesture

import random
class Ai(Player):
    def __init__ (self,name):
        super().__init__(name)
# prepare a sequence
    def get_choice(self):
        return(random.choice(Gesture().gesture))
