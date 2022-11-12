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

#Write your code below this line 👇

import random

choices = [rock, paper, scissors]

my_score = 0
cpu_score = 0
tie = 0

for i in range(1,11):
  number = random.randint(1,3)
  cpu = choices[number - 1]
  my_choice = int(input("ROCK, PAPER, SCISSORS... GO!\n(1=rock, 2=paper, 3=scissors) "))
  range_num = (1, 2, 3)
  if my_choice not in range_num:
    print("\n\nINVALID ENTRY!! YOU LOST!\n\n")
    cpu_score += 1
  else:
    me = choices[my_choice - 1]
    print(f"\nYOUR CHOICE:{me}")
    print(f"\nCOMPUTER'S CHOICE:{cpu}")


    #me=rock variations
    if me == rock and cpu == paper:
      print("*** BOOOOO!!!... YOU LOST!... ***\n\n")
      cpu_score += 1
    elif me == rock and cpu == scissors:
      print("*** CONGRATS!!! :)) YOU WON! ***\n\n")
      my_score += 1
    elif me == rock and cpu == rock:
      print("*** HMMM... IT'S A TIE! ***\n\n")
      tie += 1

    #me=paper variations
    elif me == paper and cpu == paper:
      print("*** HMMM... IT'S A TIE! ***\n\n")
      tie += 1
    elif me == paper and cpu == scissors:
      print("*** BOOOOO!!!... YOU LOST!... ***\n\n")
      cpu_score += 1
    elif me == paper and cpu == rock:
      print("*** CONGRATS!!! :)) YOU WON! ***\n\n")
      my_score += 1

        #me=scissors variations
    elif me == scissors and cpu == paper:
      print("*** CONGRATS!!! :)) YOU WON! ***\n\n")
      my_score += 1
    elif me == scissors and cpu == scissors:
      print("*** HMMM... IT'S A TIE! ***\n\n")
      tie += 1
    elif me == scissors and cpu == rock:
      print("*** BOOOOO!!!... YOU LOST!... ***\n\n")
      cpu_score += 1
      
print(f"Your Score: {my_score}")
print(f"Computer's Score: {cpu_score}")
print(f"Tie: {tie}")
