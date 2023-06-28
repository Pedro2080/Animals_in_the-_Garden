# Animals in the Garden

There is a square garden of size SIZE x SIZE (where 1 < SIZE < 15).
There are animals in the garden like: **cats**, **dogs** and **turtles**.
The purpose of the project is to track their location.
Each animal has its (one) owner, the owner can have several pets.

The owner has the following characteristics:
- Name
- Surname
- Sex
- Age

Each animal has the following characteristics:
- Name
- Sex
- Age
- Current location
- Owner

Additionally:
- Cats and Dogs have the "race" trait.
- Turtles have the "state" feature, which takes the following values: "hidden in shell", "active".
The program should provide the following features:
- Text menu that allows you to select individual options or exit from the program.

Example:
1.  Add owner
2.  Check if owner exists
3.  List all owners
4.  Remove an owner
5.  Add a new animal
6.  Check if animal exists
7.  List all animals
8.  Remove an animal
9.  Move the animal
10. Feed the turtle
<other options>
0. Save and exit

## Register of owners
- The ability to add a new owner.
- The ability to delete an existing owner.
- The ability to view a list of all owners (all data) with a list of animals belonging to them.
- Records of animals.
- The ability to add a new animal.
- The ability to delete an existing animal.
- Ability to list all animals (all data). 

## Movement of animals
- The starting position of all animals is the upper left corner garden.
- In order to move an animal, first select which one you want to move the animal, and then select the direction: up, down,
left right.
- The animal moves only one field in the selected direction if the target field is in the garden.

- In the case of an attempt to move an animal into a prohibited area field the user should get an appropriate error message (no
however, this should abort the program).
- Turtles can only move if they are enable to "active".
- After each movement of the turtle, its state changes to "hidden in a shell".
- An attempt to move a turtle hidden in its shell should display the appropriate error.
- After a successful move it should be displayed a message informing about the position to which it was left
shifted animal data.

## Feeding the turtles
- The ability to choose a turtle to feed, the fed turtle changes its status to "active".
## Data saving
- Before closing the program, data on all owners should be saved to the "users.txt" file, and animal data to the file "animals.txt".
- When starting the program, data should be read from the above files.

## Author

- [@joaopedrodasilva](https://github.com/Pedro2080)
