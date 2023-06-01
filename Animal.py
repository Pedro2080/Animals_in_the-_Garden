from abc import ABC, abstractmethod


class Animal():
    """
    Each animal will have different implementation of this method
    Example: turtle
    """
    def __int__(self, name, gender, age, position_row, position_column, owner):
        self.name = name
        self.gender = gender
        self.age = age
        self.position_row = position_row
        self.position_column = position_column
        self.owner = owner

    @abstractmethod
    def move(self, direction):

    #getter method
    def getName(self):

        return self.name

    # setter method
    def setName(self, name):
        self.name = name

    def getGender(self):

        return self.gender

    def setGender(self, gender):
        self.gender = gender

    def getAge(self):

        return self.age

    def setAge(self, age):
        self.age = age

    def getPositionRow(self):

        return self.position_row

    def setPositionRow(self, position_row):
        self.position_row =position_row

    def getPosiotionColumn(self):

        return self.position_column

    def getOwner(self):

        return self.owner

    def setOwner(self, owner):
        self.owner = owner
