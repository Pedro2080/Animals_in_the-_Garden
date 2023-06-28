from Animals_in_the_Garden.AnimalsGarden import animals_file_name


def list_animals():
    global check_animals_file
    get_file_lines = []  # Get all the lines in the text file
    results_file = []  # Stores the found data

    print("List of owners:")
    print('-'*43)

    print("name".center(0), "gender".center(10), "age".center(10) )
    try:
        check_animals_file = open(animals_file_name, 'r')
        file_read_lines = check_animals_file.readlines()

        for animals in file_read_lines:
            get_file_lines.append(animals)

        for each_lines in get_file_lines:
            file_lines = each_lines.replace(',', '')
            results_file.append(file_lines)

        print(*results_file)

    except FileNotFoundError:
        print('The file does not exist')
    check_animals_file.close()
