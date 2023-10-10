import random

print("Welcome to the Quizz game by Arif!")

print("--------------NOTE---------------\n"
      "In this quizz you'll be asked to solve few \n"
      "simple mathmatical calculations. You have to \n"
      "calculate by your mind and have to write the \n"
      "correct answer with only integer number.")

if input("\nAre you ready to start?(yes/no) ") != "yes".lower():
    quit()
score = 0

RandInt11 = random.randint(1,15)
RandInt12 = random.randint(1,15)
answer= int(input(f"What is the solution of, {RandInt11} + {RandInt12} ? "))
if answer == RandInt11+RandInt12:
    print("Correct")
    score+=1
else:print("Incorrect")

RandInt21 = random.randint(1,15)
RandInt22 = random.randint(1,15)
answer= int(input(f"What is the solution of, {RandInt21} + {RandInt22} ? "))
if answer == RandInt21+RandInt22:
    print("Correct")
    score+=1
else:print("Incorrect")

RandInt31 = random.randint(1,15)
RandInt32 = random.randint(1,15)
answer= int(input(f"What is the solution of, {RandInt31} + {RandInt32} ? "))
if answer == RandInt31+RandInt32:
    print("Correct")
    score+=1
else:print("Incorrect")

RandInt41 = random.randint(1,15)
RandInt42 = random.randint(1,15)
answer= int(input(f"What is the solution of, {RandInt41} + {RandInt42} ? "))
if answer == RandInt41+RandInt42:
    print("Correct")
    score+=1
else:print("Incorrect")

RandInt51 = random.randint(1,15)
RandInt52 = random.randint(1,15)
answer= int(input(f"What is the solution of, {RandInt51} + {RandInt52} ? "))
if answer == RandInt51+RandInt52:
    print("Correct")
    score+=1
else:print("Incorrect")

print("---You Successfully finished the quizz---\n Here is your result:\n-------------------------"
      f"\nYou have {score} correct answers.\nYour total scrore {(score/5)*100}%")
