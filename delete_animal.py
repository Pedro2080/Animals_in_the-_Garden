from Animals_in_the_Garden.AnimalsGarden import animals_file_name


def delete_animal():
    global check_file
    get_lines = []  # Get all the lines in the text file
    results = []  # Stores the deleted owner

    try:
        check_file = open(animals_file_name, 'rt')
        file_read_lines = check_file.readlines()

        animal_name = input("Enter the name of the animal to be delete.\n")

        for user in file_read_lines:
            lines = user.split(',')
            get_lines.append(lines)

        for each_lines in get_lines: # TODO
            file_lines = each_lines[0].lower().strip()

            if animal_name in file_lines:
                results.remove(animal_name)

        if animal_name in results:
            print(f"Animal {animal_name} removed successfully.")
        else:
            print(f'Animal {animal_name} not found.')
    except FileNotFoundError:
        print('The file does not exist')
    check_file.close()

