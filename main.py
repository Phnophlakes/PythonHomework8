# This mood checker was developed by Alfred Schubrig
mood = None
mood = input("How is you mood?: ")

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Always look on the bright side of live")
elif mood == "exited":
    print("Good Morning VIETNAAAM!")
elif mood == "relaxed":
    print("You should be more worried")
elif mood == "I am worried that machines will take over the world":
    print("I cannot let you do this Dave")
else:
    print("I don´t recognize this mood")

# Second part of the homework
game = input("Do you want to play a game? Please input Yes or No: ")

# This is the secret number
secret = 9

if game == "Yes":
    print("Ok! I have a secret number. Can you guess it?")
    guess = int(input("Secret number: "))
    if secret == guess:
        print("well done! You guessed right!")
    else:
        print("oh that is wrong! You lost!")
        chance = int(input("But you will get a second chance! Hint the number is between 5 and 10: "))
        if secret == chance:
            print("Well done, that is correct!")
        else:
            print("Sorry you lost again")
else:
    print("Bye then!")