import random
def start():
    random_num = random.randint(0, 100)
    def game():
        num = int(input("Guess the number: "))
        if random_num > num:
            print("Bigger")
            game()
        elif random_num < num:
            print("Smaller")
            game()
        else:
            print("You guessed the number!")
            play_again = input("Do you want to play again? Y/N: ")
            if play_again.lower() == "y":
                start()
            else:
                print()
    game()
start()