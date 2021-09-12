import random
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
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >=3 or user_choice < 0 :
  print(" You tayped an invalid number, you lose ")
else:
  print(game_images[user_choice])

  random_computer_choice = random.randint(0,2)
  print("computer chose : ")
  print(game_images[random_computer_choice])

#  generally who have the largest number wins except
# we have two exception with 0 (rock) and 2 (scissors) we need to write them first
# if user_choice >= 3 or user_choice < 0 :
#   print(" You typed an invalid number, you lose")
  if user_choice == 0 and random_computer_choice == 2:
    print("You win")
  elif user_choice == 2 and random_computer_choice == 0:
    print("You lose")
  elif user_choice > random_computer_choice :
    print("You win")
  elif user_choice < random_computer_choice :
    print("You lose")
  elif user_choice == random_computer_choice :
    print("It's a draw")
