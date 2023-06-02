from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Each animal will have different implementation of this method
    Example: turtle
    """
    def __int__(self, name, gender, age, position_row, position_column, owner):
        self.gender = gender
        self.age = age
        self.position_row = position_row
        self.position_column = position_column
        self.owner = owner

    @abstractmethod
    def move(self, direction):
    # getter method
    @property
    def name(self):
        return self.name
    # setter method
    @name.setter
    def name(self, name):
        self.name = name
    @property
    def gender(self):
        return self.gender
    # setter method
    @gender.setter
    def gender(self, gender):
        self.gender = gender

    @property
    def age(self):
        return self.age
    # setter method
    @age.setter
    def age(self, age):
        self.age = age

    # getter method
    @property
    def position_row(self):
        return self.position_row

    # setter method
    @position_row.setter
    def position_row(self, position_row):
        self.position_row =position_row

    @property
    def position_column(self):
        return self.position_column

    @position_column.setter
    def position_column(self,position_column):
        self.position_column = position_column

    @property
    def owner(self):
        return self.owner
    # setter method
    @owner.setter
    def owner(self, owner):
        self.owner = owner
