"""from Animals_in_the_Garden.AnimalsGarden import header"""

"""Check if the file exists, if not create one"""


def check_if_file_exist(file_name):
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


"""main menu to be displayed each time user interacts"""


def display_menu():
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


def add_user(file_name, name, surname, sex, age):
    try:
        check_file = open(file_name, 'at')  # append text
    except:
        print('There was an error opening the file!\n')
    else:
        try:
            check_file.writelines(f'{name}, {surname}, {sex}, {age}\n')
        except:
            print('There was an error when writing the data!\n')
        else:
            print(f'name:{name}, surname:{surname}, sex:{sex}, age:{age} record added successfully.')
            check_file.close()


def check_if_username_exists(file_name, username): # TODO
    try:
        check_file = open(file_name, 'rt')
        file_read_lines = check_file.readlines()
        check_file.close()

        for user in file_read_lines:
            lines = user.split()

            for each_lines in lines:
                file_lines = each_lines.lower().strip()
                if file_lines == username:
                    print(f"The user {file_lines} exixts.")
                    break
                else:
                    print(f'The user {file_lines} does not exist.')
    except FileNotFoundError:
        print('The file does not exist')
