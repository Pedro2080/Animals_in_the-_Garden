from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Each animal will have different implementation of this method
    Example: turtle
    """
    def __init__(self, name, gender, age, position_row, position_column, owner):
        self._name = name
        self._gender = gender
        self._age = age
        self._position_row = position_row
        self._position_column = position_column
        self._owner = owner

    def move(self, direction):
        pass

    def exibir(self):
        print(f"{self._name}, {self._owner}")


    # getter method
    @property
    def name(self):
        return self._name

    # setter method
    @name.setter
    def name(self, name):
        self._name = name

    # getter method
    @property
    def gender(self):
        return self._gender

    # setter method
    @gender.setter
    def gender(self, gender):
        self._gender = gender

    # getter method
    @property
    def age(self):
        return self._age

    # setter method
    @age.setter
    def age(self, age):
        self._age = age

    # getter method
    @property
    def position_row(self):
        return self._position_row

    # setter method
    @position_row.setter
    def position_row(self, position_row):
        self._position_row = position_row

    # getter method
    @property
    def position_column(self):
        return self._position_column

    # setter method
    @position_column.setter
    def position_column(self, position_column):
        self._position_column = position_column

    # getter method
    @property
    def owner(self):
        return self._owner

    # setter method
    @owner.setter
    def owner(self, owner):
        self._owner = owner
