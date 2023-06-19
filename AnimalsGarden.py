"""from Animals_in_the_Garden.Functions import addOwner"""
from Animals_in_the_Garden.Functions import create_users_file, check_if_file_exist
from Animals_in_the_Garden.Functions import display_menu, add_user

users_file_name = 'users.txt'
animals_file_name = 'animals.txt'

if not check_if_file_exist(users_file_name):
    create_users_file(users_file_name)

if not check_if_file_exist(animals_file_name):
    create_users_file(animals_file_name)

# Call display function
display_menu()

option = int(input("Enter one of the options:\n"))

owner_name = input("Add the name of the owner.")
owner_surname = input("Add the surname of the owner.")
owner_gender = input("Add the gender of the owner.")
owner_age = int(input("Add the age of the owner."))

while True:
    if option == 1:
        print('Chosen 1. Add owner\n')
        add_user(users_file_name, owner_name, owner_surname, owner_gender, owner_age)
        print("---------------------------")
        break
