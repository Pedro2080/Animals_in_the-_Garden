"""from Animals_in_the_Garden.Functions import addOwner"""
from Animals_in_the_Garden.Functions import create_users_file, check_if_file_exist


users_file_name = 'users.txt'
animals_file_name = 'animals.txt'

if not check_if_file_exist(users_file_name):
    create_users_file(users_file_name)

if not check_if_file_exist(animals_file_name):
    create_users_file(animals_file_name)

