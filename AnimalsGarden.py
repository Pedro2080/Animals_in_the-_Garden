"""from Animals_in_the_Garden.Functions import addOwner"""
from Animals_in_the_Garden.Functions import createUsersFile, check_if_file_exist

users_file_name = 'readUserFiles.txt'
owners_file_name = 'readOwnersFiles.txt'

if not check_if_file_exist(users_file_name):
    createUsersFile(users_file_name)

if not check_if_file_exist(owners_file_name):
    createUsersFile(owners_file_name)
