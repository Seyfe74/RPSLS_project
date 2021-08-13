
from human import Human
from ai import Ai
class Game:


   def __init__(self):
    #Has A
    self.player_one = Human()
    self.player_two = None
   # Can Do
   def run_game(self):
      self.determine_game_type()
      player_one_chosen_gesture = self.player_one.get_choice()
      player_two_chosen_gesture = self.player_two.get_choice()
    #Setup Phase
    #Welcome
    #Display rules, what beats what?
    #Determine Game Type-Single player or multi?
    #Creat player based on game type
    #(Not required) Ask players their name?


    #Game rounds - Repeat until one player has two points
    #Player one choose a gesture
    #Prompt user to enter gesture
    #Save choise somewhere
    #Player two chooses a gesture
    #Compare gustures
    #  - Winer gets a point
    #  - No point if tie round
    # Display winner of round


    #End game
    #Display winner of game
    #(Not required) Ask if they want to play again
    pass

   def determine_game_type(self):
    # Set self.player_two to human or AI
      self.player_two = Ai()
