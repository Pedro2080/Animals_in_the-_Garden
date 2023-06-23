from Animals_in_the_Garden.Dog import Dog
from Animals_in_the_Garden.Cat import Cat
from Animals_in_the_Garden.Turtle import Turtle
from Animals_in_the_Garden.AnimalsGarden import animals_file_name


def add_animal():
    global check_file
    animals_list = []

    while True:
        animal_name = input("Enter the animal name.\n")
        animal_gender = input("Enter the animal gender.\n")
        animal_age = int(input("Enter the age.\n"))
        animal_owners = input("Enter the animal's owner\n")

        # get type of animal input from user
        type = int(input("Choose option number for the type : \n1-Dog\n2.Cat\n3.Turtle\n"))

        breed = None
        #if cat or dog , add the feature breed and take its input from user
        if type == 1 or type == 2:
            breed = input("Enter the breed of the animal\n")
        # if dog , create a Dog instance using Dog class constructor with current position as top left square ie. 00

        if type == 1:
             print('---List of Dogs---'.center(15))
             dog = Dog(animal_name, animal_gender, animal_age, 0, 0, animal_owners, breed)
             animals_list.append(dog)


             print("All Dog information:")
             for animals in animals_list:
                try:
                    check_file = open(animals_file_name, 'at')  # append text
                except:
                    print('There was an error opening the file!\n')
                else:
                    try:
                        check_file.writelines(f'{animals.name}, {animals.gender}, {animals.age},'
                                              f' {animals.position_row},{animals.position_column},{animals.breed}\n')
                    except:
                        print('There was an error when writing the data!\n')
                    else:
                        print(f'name:{animals.name} record added successfully.')
                    check_file.close()


        # if cat , create a Cat instance using Cat class constructor with current position as top left square ie.00

        if type == 2:
            print('---List of Cat---'.center(15))
            cat = Cat(animal_name, animal_gender, animal_age, 0, 0, animal_owners, breed)
            animals_list.append(cat)

            print("All Cat information:")
            for animals in animals_list:
                try:
                    check_file = open(animals_file_name, 'at')  # append text
                except:
                    print('There was an error opening the file!\n')
                else:
                    try:
                        check_file.writelines(f'{animals.name}, {animals.gender}, {animals.age},'
                                              f' {animals.position_row},{animals.position_column},{animals.breed}\n')
                    except:
                        print('There was an error when writing the data!\n')
                    else:
                        print(f'name:{animals.name} record added successfully.')
                    check_file.close()


        if type == 3:
            print('---List of Turtles---'.center(15))
            turtle = Turtle(animal_name, animal_gender, animal_age, 0, 0, animal_owners, "hidden in the shell")
            animals_list.append(turtle)


            print("All Turtle information:")
            for animals in animals_list:
                try:
                    check_file = open(animals_file_name, 'at')  # append text
                except:
                    print('There was an error opening the file!\n')
                else:
                    try:
                        check_file.writelines(f'{turtle.name}, {turtle.gender}, {turtle.age},'
                                              f' {turtle.position_row},{turtle.position_column},{turtle.state}\n')
                    except:
                        print('There was an error when writing the data!\n')
                    else:
                        print(f'name:{animals.name} record added successfully.')
                    check_file.close()

        answer = input("Do you want to add another animal?\n")

        if answer != 'y':
            break
