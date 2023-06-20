from Animals_in_the_Garden.add_user import add_user


def input_user():
    option = int(input("Enter one of the options:\n"))

    while True:
        if option == 1:
            print('Chosen 1. Add owner\n')
            print(add_user())
            print("---------------------------")
            break
