secret = 10

guess = int(input("Guess the secret number between 1 and 20: "))

if guess == secret:
    print("Congratulations!! You have guessed the number!")
else:
    print("☹ More luck next time.Try agan!!")