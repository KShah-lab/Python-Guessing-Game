import random
num = random.randint(1, 100)
print ("Python has selected a number between 1 and 100 with 1 and 100 included. Now it is your turn!")
turns=0
while True:
    guess = int(input("Enter the number you guessed ="))
    if(guess == num):
        print ("Well done! You guessed the correct number!")
        break
    elif(guess < num):
            print("Its a bigger number!")
            turns+=1

    elif (guess > num):
            print("Its a smaller number!")
            turns+=1
print ("Number of turns = ",turns-1)
