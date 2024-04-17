import random                 #To pick a random word from our other file
import sys                    #To terminate the program when a player does not want to play anymore 
from words import words       #Stores all of our words


class Hangman():

   def __init__(self):
      
      #Initialization
      
      self.correct_counter=[]
      self.word=random.choice(words)                     # Picks a random word                            
      self.guess_made=0                                  
      self.guess_list=[]                                 # Stores all correct guesses
      self.letters_guessed=[]                            # Stores all incorrect guesses      
      self.length=len(self.word)                         # Gets the length of the current word for future loops        
      for i in range(self.length):                               
         self.guess_list.append('_')                     # Makes a list of the same size as our word                                         
         self.correct_counter.append("_")                # A list to compare with self.word as it will eventually be a string of underscores                     
        
   def main(self):           


      while True:                                        # Creates a while loop to be able to take input @ player_guess from the user w/o errors
         

         game.draw()                                     # Calls the draw() method to draw the stick figure and show how many strikes the user has left
         print(self.guess_list)

         player_guess=input('What is your guess?')       
         
         if player_guess=='' or player_guess in self.guess_list or player_guess in self.letters_guessed:        # Making sure that the input is not empty or reused 
            player_guess=input('You have left it empty or picked a word that has already been guessed. Please pick a character that has not been guessed.')


         if player_guess in self.word:                  # Checks if the guess is in the word, if it is it calls the check_position() method.
            game.check_position(player_guess)


         elif player_guess not in self.word:            # If the letter is not the word it increments the variable guess_made by 1 and appends the wrong guess into letters_guessed 
            self.letters_guessed.append(player_guess)
            self.guess_made+=1
         


         if ("".join(self.correct_counter))==self.word and self.guess_made<=7 :    # Checks if the player has guessed the correct letters by seeing if the word has turned to correct number of _
            print('YOU GUESSED THE WORD WOOOOOW!')
            retry=input('Would you like to try again?')                            # Takes input to see if player wants to play again
            
            if retry=='yes':                                                       # Resets all the variable if user typed yes and recalls the main() method
               
               self.correct_counter=[]
               self.word=random.choice(words)
               self.guess_made=0
               self.guess_list=[]
               self.letters_guessed=[]
               self.length=len(self.word)
               for i in range(self.length):
                   self.guess_list.append('_')
               for i in range(self.length):
                     self.correct_counter.append("_")
               game.main()
            
            else:                                                                  # If the player types anything other than yes we use the sys library to terminate the program
               sys.exit()
         
         elif self.guess_made==7:                                                  # If the player has taken 7 guesses we print the lose message and give them the option to retry or to quit
            print('You Lose and the remaining letters were {}.'.format(self.word))
            retry=input('Would you like to try again?')
            
            if retry.lower=='yes':
               self.word=random.choice(words)
               self.correct_counter=[]
               self.word=random.choice(words)
               self.guess_made=0
               self.guess_list=[]
               self.letters_guessed=[]
               self.length=len(self.word)
               for i in range(self.length):
                   self.guess_list.append('_')
               game.main()
            
            else:
               sys.exit()         


   def draw(self):

      # A list where each item is a stage of the stick figure
      stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     /
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        """,
        """
           --------
           |      
           |      
           |    
           |      
           |     
        """
    ]
      # Depending on the guesses made we print a different stage figure and a message showing how many guesses you have remaining and a list of all the incorrect letters you have guessed so far.
      if self.guess_made==0:
         print(stages[7])
         print('You have {} strikes remaining'.format(7-self.guess_made))
         print('The incorrect letters you have guessed so far are {}'.format(self.letters_guessed))
      
      elif self.guess_made==1:
         print(stages[6])
         print('You have {} strikes remaining'.format(7-self.guess_made))
         print('The incorrect letters you have guessed so far are {}'.format(self.letters_guessed))

      elif self.guess_made==2:
         print(stages[5])
         print('You have {} strikes remaining'.format(7-self.guess_made))
         print('The incorrect letters you have guessed so far are {}'.format(self.letters_guessed)) 
         

      elif self.guess_made==3:
         print(stages[4])
         print('You have {} strikes remaining'.format(7-self.guess_made))
         print('The incorrect letters you have guessed so far are {}'.format(self.letters_guessed))

      elif self.guess_made==4:
         print(stages[3])
         print('You have {} strikes remaining'.format(7-self.guess_made))
         print('The incorrect letters you have guessed so far are {}'.format(self.letters_guessed))

      elif self.guess_made==5:
         print(stages[2])
         print('You have {} strikes remaining'.format(7-self.guess_made))
         print('The incorrect letters you have guessed so far are {}'.format(self.letters_guessed))

      elif self.guess_made==6:
         print(stages[1])
         print('You have {} strikes remaining'.format(7-self.guess_made))
         print('The incorrect letters you have guessed so far are {}'.format(self.letters_guessed))

      elif self.guess_made==7:
         print(stages[0])

   def check_position(self,player_guess):                                     #Checks the position of a letter when it passes through the if statement in line 37
      
      
      position=self.word.index(player_guess)                                  # Gets the index of the guessed letter in the word                                 
      self.guess_list[position]=player_guess                                  # Place's it in that index in the guess list
      self.word=self.word[:position]+'_'+self.word[position+1:]               # And replaces the word with an underscore that's why we compare self.word with a bunch of underscores in line47                  
      if player_guess in self.word:                                           # If the word is still there we recall the method and do the process again
         game.check_position(player_guess)                                                              
      
      else:                                                                   # If it isn't we return the updated version of self.guess_list
         return self.guess_list







game=Hangman()
game.main()
