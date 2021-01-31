######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################


def game():

    from random import randint

    status = True

    title = 'Welcome to the Number Guessing Game.'
    print(title, "\n", "-" * len(title), sep="")

    while status:
        random = randint(1,100)
        claim = 7

        while True:

            if claim > 0:
                guess = int(input("What do you think is the number? (1,100) "))
            else:
                print("You could not guess the number correctly. Number:{}".format(random))
                break

            if guess != random:
                claim -= 1
                if guess > random:
                    print("The number is below and your remaining guess is {}.".format(claim))
                else:
                    print("The number is above and your remaining guess is {}.".format(claim))
            else: 
                print("Congratulations! You found the number.")
                break
        check = input("Would you like to play again? (Y/N) \n")

        if check == "Y":
            status = True
        else:
            status = False
            print("Goodbye!")

game()



