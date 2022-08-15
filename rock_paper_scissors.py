rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
rock_paper_scissors = [rock, paper, scissors]
computer_rps = random.randint(0, 2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if not player_choice <= 3 or player_choice < 0:
  print("Type a valid number, landlubber!")
else:
  print(f"\nYou chose: \n {rock_paper_scissors[player_choice]}")
  print(f"Computer chose: \n{rock_paper_scissors[computer_rps]}")
  
  #Draw
  if player_choice == computer_rps:
    print("Draw!")
  #Lose
  elif player_choice == 0 and computer_rps == 1 or player_choice == 1 and computer_rps == 2 or player_choice == 2 and computer_rps == 0:
    print("You lose!")
  #Win
  else:
    print("You win!")