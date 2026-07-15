# we are going to write a program that generates a random number ask the user to guess it?


import random

rand = random.randint(1,100)

player = -1
guesses = 0
while( player != rand):
    guesses +=1
    player = int(input("enter the guess no:"))

    if(player > rand):
        print("lower number please")


    else:
        print("higher number please")

print(f"you have guessed the number correctly in {guesses} attempt")