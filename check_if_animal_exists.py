from Animals_in_the_Garden.AnimalsGarden import animals_file_name


def check_if_animal_exists():
    global check_file
    get_lines = []  # Get all the lines in the text file
    results = []  # Stores the found data

    try:
        check_file = open(animals_file_name, 'rt')
        file_read_lines = check_file.readlines()

        animal_name = input("Enter the name of the animal to be checked.\n")

        for owner in file_read_lines:
            lines = owner.split(',')
            get_lines.append(lines)

        for each_lines in get_lines:
            file_lines = each_lines[0].lower().strip()

            if animal_name in file_lines:
                results.append(animal_name)

        if animal_name in results:
            print(f"Animal {animal_name} found successfully.")
        else:
            print(f'Animal {animal_name} not found.')
    except FileNotFoundError:
        print('The file does not exist')
    check_file.close()
