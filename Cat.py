from Animals_in_the_Garden.Animal import Animal


class Cat(Animal):
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


