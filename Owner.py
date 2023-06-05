class Owner():
    def __init__(self, name, surname, gender, age):
        self._name = name
        self._surname = surname
        self._gender = gender
        self._age = age

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
    def surname(self):
        return self._surname

    # setter method
    @surname.setter
    def surname(self, surname):
        self._surname = surname

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
