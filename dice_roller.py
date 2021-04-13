import random

roll_again = "y"

while roll_again == "y":
    print("Your dice are ....")
    print(random.randint(1, 9))
    roll_again = input("Roll the dices again? Y/N - ").lower()
