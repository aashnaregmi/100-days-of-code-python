# guess the number
import random

choosen_num=random.randint(1,100)
print(choosen_num)

while True:
    easy=10
    hard=5
    level=input("Choose a difficulty level: ")
    
    if level=="easy":
        print(f"You have {easy} attemps")
        break
    elif level=="hard":
        print(f"You have {easy} attemps")
        break
    else:
        print ("Choose between easy of hard!! ")
        continue

        