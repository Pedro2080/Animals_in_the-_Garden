from Animals_in_the_Garden.Animal import Animal


class Turtle(Animal):
    def __init__(self, name, gender, age, position_row, position_column, owner, state):
        super().__init__(name, gender, age, position_row, position_column, owner)
        self._state = state

    # getter method
    @property
    def state(self):
        return self._state

    # setter method
    @state.setter
    def state(self, state):
        self._state = state
