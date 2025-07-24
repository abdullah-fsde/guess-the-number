import random
randNumber = random.randint(1,10)
num = 0
guesses = 0
while(num!=randNumber):
    num = int(input("Enter your guessed number:"))
    if(randNumber==num):
        print("You Guessed it right, Congrats!")
    elif(num>randNumber):
        print("Your Guess wasn't right, Enter a smaller number and try.")
    elif(num<randNumber):
        print("Your Guess wasn't right, Enter a larger number and try.")
    else:
        print("Enter a valid number")
    guesses+=1
print(f"You guessed it in {guesses} guesses")
with open("hiscore.txt",'r') as f:
    hiscore=int(f.read())
if(guesses<hiscore):
    print("New Reord!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))