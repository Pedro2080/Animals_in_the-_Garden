from Animals_in_the_Garden.AnimalsGarden import users_file_name


def delete_owner():
    global check_file
    get_lines = []  # Get all the lines in the text file
    results = []  # Stores the deleted owner

    try:
        check_file = open(users_file_name, 'rt')
        file_read_lines = check_file.readlines()

        owner_name = input("Enter the name of the owner to be delete.\n")

        for user in file_read_lines:
            lines = user.split(',')
            get_lines.append(lines)

        for each_lines in get_lines: # TODO
            file_lines = each_lines[0].lower().strip()

            if owner_name in file_lines:
                results.remove(owner_name)

        if owner_name in results:
            print(f"User {owner_name} removed successfully.")
        else:
            print(f'User {owner_name} not found.')
    except FileNotFoundError:
        print('The file does not exist')
    check_file.close()

