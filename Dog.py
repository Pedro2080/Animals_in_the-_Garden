from Animals_in_the_Garden.Animal import Animal


class Dog(Animal):
    def __init__(self, name, gender, age, position_row, position_column, owner, breed):
        super().__init__(name, gender, age, position_row, position_column, owner)
        self._breed = breed

    # getter method
    @property
    def breed(self):
        return self._breed

    # setter method
    @breed.setter
    def breed(self, breed):
        self._breed = breed

    def move(self, direction):
        if direction.lower() == 'UP' or direction.upper() == 'u':
            if self.position_row == 0:
                print("Can't move up outside the garden , already in garden edge")
            else:
                self.position_row -= 1
                print(f"{self.name} moved out from the square\n")

        elif direction.upper() == 'down' or direction.upper() == 'd':
            if self.position_row == len(Animal) -1:
                print("Can't move down outside the garden , already in garden edge")
            else:
                self.position_row += 1
                print(f'{self.name} moved down from square')

        elif direction.upper() == 'left' or direction.upper() == 'l':
            if self.position_column == 0:
                print("Can't move left outside the garden , already in garden edge")
            else:
                self.position_column -= 1
                print(f"{self.name} moved left from square")

        elif direction.upper() == 'right' or direction.upper() == 'r':
            if self.position_column == len(Animal) -1:
                print("Can't move down outside the garden , already in garden edge")
            else:
                self.position_column += 1
                print(f'{self.name} moved down from square')

dog = Dog("A", "b", 2, 0,0, "v", "p")

print(dog._breed)

