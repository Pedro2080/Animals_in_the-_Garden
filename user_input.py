from Animals_in_the_Garden.add_user import add_owner
from Animals_in_the_Garden.check_if_user_exist import check_if_username_exists
from Animals_in_the_Garden.list_owners import list_owners
from Animals_in_the_Garden.delete_owner import delete_owner
from Animals_in_the_Garden.add_animal import add_animal


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

        elif option == 3:
            print('Chosen 3. List owner:\n')
            list_owners()
            print("---------------------------")
            break

        elif option == 4:
            print('Chosen 4. Delete owner:\n')
            delete_owner()
            print("---------------------------")
            break

        elif option == 5:
            print("Chosen 5. Add a new animal:")
            add_animal()
            print("---------------------------")
            break




