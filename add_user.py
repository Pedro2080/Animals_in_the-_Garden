from Animals_in_the_Garden.AnimalsGarden import users_file_name
from Animals_in_the_Garden.Owner import Owner


def add_user():
    owners_list = []
    global check_file

    while True:
        owner_name = input("Add the name of the owner.\n")
        owner_surname = input("Add the surname of the owner.\n")
        owner_gender = input("Add the gender of the owner.\n")
        owner_age = int(input("Add the age of the owner.\n"))

        owner = Owner(owner_name, owner_surname, owner_gender, owner_age)

        owners_list.append(owner)
        print("The owner has been added into the owner's list.")
        answer = input("Do you want to add another owner?\n")

        if answer != 'y':
            break

    print("All owners information:")
    for owners in owners_list:
        try:
            check_file = open(users_file_name, 'at')  # append text
        except:
            print('There was an error opening the file!\n')
        else:
            try:
                check_file.writelines(f'{owners.name}, {owners.surname}, {owners.gender}, {owners.age}\n')
            except:
                print('There was an error when writing the data!\n')
            else:
                print(
                    f'name:{owners.name}, surname:{owners.surname}, sex:{owners.gender}, age:{owners.age} record added successfully.')
                check_file.close()