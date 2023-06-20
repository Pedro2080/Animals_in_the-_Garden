from Animals_in_the_Garden.AnimalsGarden import users_file_name


def check_if_username_exists():
    global check_file
    get_lines = []  # Get all the lines in the text file
    results = []  # Stores the found data

    try:
        check_file = open(users_file_name, 'rt')
        file_read_lines = check_file.readlines()

        owner_name = input("Enter the name of the owner to be checked.\n")

        for user in file_read_lines:
            lines = user.split(',')
            get_lines.append(lines)

        for each_lines in get_lines:
            file_lines = each_lines[0].lower().strip()

            if owner_name in file_lines:
                results.append(owner_name)

        if owner_name in results:
            print(f"User {owner_name} found successfully.")
        else:
            print(f'User {owner_name} not found.')
    except FileNotFoundError:
        print('The file does not exist')
    check_file.close()
