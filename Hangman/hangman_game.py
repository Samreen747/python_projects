#hangman
import random
# r is raw string it treats '\' as normal text
stages=[r'''
       +-----+
       |     |
       O     |
      /|\    |
      / \    |
             |
             
    ---------------
        ''',
        r'''
       +-----+
       |     |
       O     |
      /|\    |
      /      |
             |
             
    ---------------
        ''',
        r'''
       +-----+
       |     |
       O     |
      /|\    |
             |
             |
             
    ---------------
        ''',
       r'''
       +-----+
       |     |
       O     |
      /|     |
             |
             |
    ---------------
        ''',
       r'''
       +-----+
       |     |
       O     |
      /      |
             |
             |
    ---------------
        ''',
        r'''
       +-----+
       |     |
       O     |
             |
             |
             |
    ---------------
        ''',
        r'''
       +-----+
       |     |
             |
             |
             |
             |
    ---------------
        ''']


words = ["apple", "banana", "orange", "grape", "chair", 
         "table", "window", "house", "garden", "school", 
         "river", "mountain", "cloud", "sun", "moon", 
         "star", "train", "car", "bus", "street"]

ran_word=random.choice(words)
print("let's start the hangman game ")

placeholder = ""
word_len=len(ran_word)
for i in range(word_len):
    placeholder += "_ "
print(placeholder)



correct_letters=[]
game_over=False
lives=6
while (not game_over) and lives>0:
   guess=input("guess a letter : ")
   if guess not in ran_word:
      print("guessed a wrong letter ,try again")
      lives -= 1
      print(f"you have {lives} lives left {stages[lives]} ")
      if lives == 0:
        print("======game over=======")
   
   else:   
      display=""
      for char in ran_word:
        if char == guess:
           display += guess
           correct_letters.append(guess)  # to add previously guessed letters to display string
        elif char in correct_letters:
           display += char
        else:
           display += "_"
      print(display) 
      print("you guessed a letter")
      print(f"you have {lives} lives left")
      print(stages[lives])

      if "_" not in display:
        game_over=True
        print("===you guessed the word===")    

