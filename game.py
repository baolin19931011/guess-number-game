import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I picked a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("请输入一个有效的数字！（别输入字母或符号）")
            continue  # 输入错了，直接跳过这次循环，重新来

        # 只有输入成功，才会走到这里
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

guessing_game()