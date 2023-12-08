#### MY SOLUTION
import sys
import random
import pdb #python debugger

def guessNum():
  try:
    userAttempts = 0
    numToGuess = None
    pdb.set_trace()
    # capturing n1 and n2 values to generate random number from sys.argv or default
    if len(sys.argv) > 1:
      n1, n2 = int(sys.argv[1]), int(sys.argv[2])
    else:
      n1, n2 = 1, 10

    numToGuess = random.randint(n1, n2)

    # runs until user 'quit's or guesses correctly
    while True:
      try:
        userResponse = input(f'\nGuess a whole number between {n1} and {n2}. \n    To quit type: \'quit\'\n    To change range type: \'range\'\n    For a hint type: \'hint\'\n   Your response:  ')
        
        # break loop if user quits
        if userResponse.upper() == 'QUIT':
          quittingMsg = f'\n********\nThank you for playing.\nThe correct number was {numToGuess}\nTotal Attempts: {userAttempts}\n********'
          print(quittingMsg)
          break
        
        # hint tells if numToGuess is odd or even
        if userResponse.upper() == 'HINT':
          hint = 'EVEN ⚖️' if numToGuess % 2 == 0 else 'ODD 👀'
          print(f'\n  HINT: The number to guess is {hint}')
          continue
        
        # creating new range through user responses
        if userResponse.upper() == 'RANGE':
          startRngMsg = '\nEnter start of range:  '
          endRngMsg = '\nEnter end of range:  '
          newStart, newEnd = int(input(startRngMsg)), int(input(endRngMsg))
          
          # Orders range values from lowest to highest``
          if newStart > newEnd: newStart, newEnd = newEnd, newStart
          
          # reassigning range values n1 and n2  to calculate new numToGuess
          n1, n2 = newStart, newEnd
          numToGuess = random.randint(n1, n2)
          prevUserAttempt = userAttempts
          userAttempts = 0
          print(f'\n    -> New range set: {n1} ~ {n2} \n  -> Total Attempts Reset: from {prevUserAttempt} to {userAttempts} ')
          continue

        userGuess = int(userResponse)

        # check userGuess against numToGuess, increase userAttempts *only* if incorrect
        if userGuess < n1 or userGuess > n2:
          outOfRangeMsg = f'\n  {userGuess} is not in within range. Total attempts not affected: {userAttempts}'
          print(outOfRangeMsg)
        elif userGuess != numToGuess:
          userAttempts += 1
          incorrectMsg = f'\n❌❌❌ {userGuess} is wrong. Try again! ❌❌❌\nTotal Attempts: {userAttempts}\n'
          print(incorrectMsg)
        else:
          userAttempts += 1
          winningMsg = f'\n********\n🥳🥳🥳 You guessed \'{numToGuess}\' correctly! 🎊🎊🎊\nTotal Attempts: {userAttempts}\n********'
          print(winningMsg)
          break
      except ValueError:
        print('\n ⚠️⚠️⚠️ Please enter whole number(s) only ⚠️⚠️⚠️\n')
  except ValueError:
    print(f'Given: \'{sys.argv[1]}\' and \'{sys.argv[2]}\' sys.argv at [1, 2] MUST be integers. ')


guessNum()




###### DEMO FROM UDEMY
# answer = random.randint(1, 10)

# guess = input('Guess a number 1 ~ 10')

# while True:
#   try:
#     if 0 < int(guess) < 11:
#       print('all good')
#       break
#   except ValueError:
#     print('please enter a number')
#     continue