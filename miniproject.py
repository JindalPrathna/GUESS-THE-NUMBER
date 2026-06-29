"""GUESS THE NUMBER"""
import random

target=random.randint(20,30)

while True:
    user_no=int(input("guess the target:"))
    if(user_no==target):
        print("WINNER")
        break
    if(user_no<target):
        print("think greater number...!!")
    else:
        print("think lesser number...!!")

print("Game End")