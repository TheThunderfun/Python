import random
# import my_module

# random_integer=random.randint(1,10)

# random_number_0_to_1=random.random()
# print(random_number_0_to_1) recommended to use uniform instead of random
# random_float=random.uniform(1,10)

rock="""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors="""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""


game_images=[rock,paper,scissors]


user_choice=int(input("what do you choose? Type 0 for Rock, 2 for Paper and 3 for Scissors.\n"))

if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])
    
computer_choice=random.randint(1,3)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice>=3 or user_choice<0:
    print("You tiped an invalid number.You lose!")
elif user_choice==0 and computer_choice==2:
    print("You wins!")
elif computer_choice==0 and user_choice==2:
    print("You lose!")
elif computer_choice>user_choice:
    print("You lose!")
elif user_choice>computer_choice:
    print("Ypu win!")
elif computer_choice==user_choice:
    print("It's a draw!")