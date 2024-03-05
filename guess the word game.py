rint("welcome to my Guess the word game")

#Create dictionary to hold words

game_dict = {
  "sports":['basketball', 'football' , 'waterpolo' , 'tennis' , 'cricket' , 'rugby' , 'hockey'],
  "colours":['orange' , 'purple' , 'blue' , 'yellow' , 'gold' ,'pink' , 'white'],
  "fruits":['apple' , 'banana' , 'orange' , 'melon' , 'strawberry' , 'raspberry', 'pineapple'],
  "classes":['english' , 'maths' , 'science' , 'art' , 'history' , 'technology' , 'careers' ],
}
#create a list of keys
game_keys = []
for key in game_dict.keys():
    game_keys.append (key)  

#the main game Loop
playing = True
while playing:
  #randomly pick the game
  game_category = game_keysrandom.randint(0,len(game_keys)-1)
  game_word = game_dict[game_category][random.randit(0,len(game_dict[game_category])-1)]

  blank_word = []
for letter in game_word:
  blank_word.append("-")
  print("guess a" + str(len(game_word))) + "letter word from the following category:" + game_category.title()

  guess = ""
  guess_count = 0

  #a single round loop 
  while guess != game_word:
    print("".join(blank_word))
    guess = input("\nEnter your guess: ").lower()
    guess_count += 1 


#guess is correct, user won
if guess == game_word:
  print("\nCorrect! You guessed the word in" + str(guess_count) + "guesses.")
  break

  #guess is incorrect

  else:
      print("That is not correct. let us reveal a letter to help you?")

    swapping = True
    while swapping:
      letter_index = random.randint(0, len(game_word)-1)
      if blank_word[letter_index] == "-":
        blank_word[letter_index] = game_word[letter_index]
        swapping = false

        choice = input("\nWould you like to play again (y/n): ").lower()
if choice != 'y':
  playing = False
  print("thank you for playing")




  print(game_category)
  print(game_word)
  input()
