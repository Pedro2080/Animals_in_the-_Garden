"""from Animals_in_the_Garden.AnimalsGarden import header"""


def check_if_file_exist(file_name):
    try:
        check_file = open(file_name, 'rt')
        check_file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createUsersFile(users_file_name):
    try:
         check_file = open(users_file_name, 'wt+')
         check_file.close()
    except:
        print('Error while openning the file!\n')
    else:
        print(f'File {users_file_name} created sucessfully!')
