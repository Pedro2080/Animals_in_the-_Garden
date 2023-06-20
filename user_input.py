from Animals_in_the_Garden.add_user import add_owner
from Animals_in_the_Garden.check_if_user_exist import check_if_username_exists


def input_user():
    option = int(input("Enter one of the options:\n"))

    while True:
        if option == 1:
            print('Chosen 1. Add owner\n')
            add_owner()
            print("---------------------------")
            break

        elif option == 2:
            print('Chosen 2. List owner:\n')
            check_if_username_exists()
            print("---------------------------")
            break

