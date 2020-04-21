Select_a_level = input ("Please select a level, easy, medium,hard:")
if Select_a_level == "easy":
  guess = int (input ("Choose a number between 1-10:") )

numberOfGuessesLeft = 5
i = 0

while guess != 3:
  guess = int (input ("That was wrong, you have " + str(numberOfGuessesLeft)+ " number of guesses left, make another guess:"))
  numberOfGuessesLeft = numberOfGuessesLeft - 1
  i += 1
  if guess == 3:
    print("You got it right!")
    break
  elif i == 5:
          print("Gameover!")
          break


Select_a_level = input ("Please select a level, easy, medium,hard:")        
if Select_a_level == "medium":
  guess = int (input ("Choose a number between 1-20:") )

numberOfGuessesLeft = 3
i = 0

while guess != 4:
  guess = int (input ("That was wrong, you have " + str(numberOfGuessesLeft)+ " number of guesses left, make another guess:"))
  numberOfGuessesLeft = numberOfGuessesLeft - 1
  i += 1
  if guess == 4:
    print("You got it right!")
    break
  elif i == 3:
          print("Gameover!")
          break

Select_a_level = input ("Please select a level, easy, medium,hard:")        
if Select_a_level == "hard":
  guess = int (input ("Choose a number between 1-50:") )

numberOfGuessesLeft = 2
i = 0

while guess != 5:
  guess = int (input ("That was wrong, you have " + str(numberOfGuessesLeft)+ " number of guesses left, make another guess:"))
  numberOfGuessesLeft = numberOfGuessesLeft - 1
  i += 1
  if guess == 5:
    print("You got it right!")
    break
  elif i == 2:
          print("Gameover!")
          break
