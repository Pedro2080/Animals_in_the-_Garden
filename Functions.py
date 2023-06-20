def check_if_file_exist(file_name): # Check if the file exists, if not create one
    try:
        check_file = open(file_name, 'rt')
        check_file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create_users_file(users_file_name):
    try:
        check_file = open(users_file_name, 'wt+')
        check_file.close()
    except:
        print('Error while opening the file!\n')
    else:
        print(f'File {users_file_name} created successfully!')


def display_menu():
    """
    main menu to be displayed each time user interacts
    """
    print("Enter the number for the below options:")
    print("1. Add owner")
    print("2. Delete the owner")
    print("3. List of owners")
    print("4. Add a new animal")
    print("5. Remove an animal")
    print("6. Lost of all animals")
    print("7. Move an animal")
    print("8. Feed the turtle")
    print("0. Save and exit")

