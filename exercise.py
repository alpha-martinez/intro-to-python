# TODO Make a class with 3 methods (not including __init__() )
# TODO Post your class link inside of the thread

class Puppy():
    def __init__(self, name, age, breed):
        self.breed = breed
        self.age = 0
        self.name = name

    def get_puppy(self, money, breed):
        self.money = money
        self.breed = breed
        self.age = 2
    
    def let_puppy_go(self, money, breed):
        self.money = money
        self.breed = breed

    def adopt_puppy(self, breed, age, money):
        self.money = money
        self.breed = breed
        self.age = 3

        
Oso = Puppy("Oso", "2", "Maltese")
Oso.get_puppy("$2000", "Malese Poodle")
