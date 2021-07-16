import random

machine_number=random.randint(1,50)
while True:
  user_number=int(input("Enter your guess "))
  if int(user_number)>machine_number:
    print("Your Guess is Great")
  elif int(user_number)<machine_number:
    print("Your Guess is small")
  else:
    print("your guess is correct")
    print("Yes Machine's number is also %d" %machine_number)
    break
