print("Welcome to the world of guessing number \n you will get 3 chances to win the game \n Have a try and see your Luck")
print(30*"*")
import random
value = random.randint(1,10)
chance=3
for i in range(3):
    chance-=1
    a=int(input("Enter your favourite number from 1 to 10:"))
    if (value==a):
        print("Hurray You WON!!!!!!!!!!!!!!")
        break
    else:
        print("Your guess is wrong and you have",chance,"more chances")
print("The random value is",value)