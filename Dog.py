class Dog:
    # Class Object Attribute
    # Same for any instance of a class
    species = 'mammal'

    # Constructor
    def __init__(self, breed, name):
        # Attributes
        self.breed = breed
        self.name = name

    # Methods
    def bark(self):
        print(f"Woof, I'm {self.name}")

