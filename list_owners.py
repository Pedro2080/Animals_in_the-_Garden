from Animals_in_the_Garden.AnimalsGarden import users_file_name


def list_owners():
    global check_user_file
    get_file_lines = []  # Get all the lines in the text file
    results_file = []  # Stores the found data

    print("List of owners:")
    print('-'*43)

    print("name".center(0),"surname".center(15), "gender".center(10), "age".center(10) )
    try:
        check_user_file = open(users_file_name, 'r')
        file_read_read_lines = check_user_file.readlines()

        for users in file_read_read_lines:
            get_file_lines.append(users)

        for each_lines in get_file_lines:
            file_lines = each_lines.replace(',', '')
            results_file.append(file_lines)

        print(*results_file)

    except FileNotFoundError:
        print('The file does not exist')
    check_user_file.close()
