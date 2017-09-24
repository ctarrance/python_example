# file: fruit3.py
# even more fun with fruit
# make this more functional


def guess_fruit_basket(basket):
    guess = input("Guess a fruit: ")
    good_guess = guess in basket

    if good_guess:
        print("You win!")
    else:
        while not good_guess:
            guess = input("Sorry, no " + guess + ". Try again or type 'quit': ")
            good_guess = guess in basket or guess == 'quit'
            if guess == 'quit':
                print("Bye!")
            elif good_guess:
                print("You win!")

def main():
    basket = ['apple', 'banana', 'kiwi', 'watermelon', 'peach']
    guess_fruit_basket(basket)

main()
