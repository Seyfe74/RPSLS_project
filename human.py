


from player import Player
from gesture import Gesture

class Human(Player):
    def __init__ (self,name):
        super().__init__(name)

        
    def get_choice(self):
        for i in range (len(Gesture().gesture)):
            print (i,Gesture().gesture [i])
        user_input =  int (input("Enter the value that corresponds to your desired gesture   "))
        if user_input not in [0,1,2,3,4]:
             print("That is not valid, please try again!")
             return self.get_choice()
        else: 
            return Gesture().gesture[user_input]