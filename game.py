
from human import Human
from ai import Ai
class Game:


   def __init__(self):
    #Has A
    self.player_one = Human(name = "")
    #self.player_one.name = ""
    self.player_two = None
   # Can Do
   def run_game(self):

      #Setup Phase  
      print("Welcome to the game:")
      print("Here are the rules:")
      rules = ["1. Rock crushes Scissors", "2. Scissors cuts Paper", "3. Paper covers Rock","4. Rock crushes Lizard","5. Lizard poisons Spock","6. Spock smashes Scissors","7. Scissors decapitates Lizard", "8. Lizard eats Paper, 9. Paper disproves Spock", "10. Spock vaporizes Rock"]
      for item in rules:
         print(item)

      self.determine_game_type()


      player_one_chosen_gesture = self.player_one.get_choice()
      print ("Player one chosen gesture is   " + player_one_chosen_gesture)
      player_two_chosen_gesture = self.player_two.get_choice()
      print ("Player two chosen gesture is   " + player_two_chosen_gesture)


    
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

   def determine_game_type(self):
    # Set self.player_two to human or AI
      num_players = input(" Enter 1 for single player or 2 for multiple  players")
      if num_players == "1":
         self.player_two = Ai(name= "")
         print("Its Human Vs Ai")
      else:
         self.player_two = Human(name = "")
         print("Its Human Vs Human")
         
      pass
