# # TODO Make a class with 3 methods (not including __init__() )
# # TODO Post your class link inside of the thread

# class Puppy():
#     def __init__(self, name, age, breed):
#         self.breed = breed
#         self.age = 0
#         self.name = name

#     def get_puppy(self, money, breed):
#         self.money = money
#         self.breed = breed
#         self.age = 2
    
#     def let_puppy_go(self, money, breed):
#         self.money = money
#         self.breed = breed

#     def adopt_puppy(self, breed, age, money):
#         self.money = money
#         self.breed = breed
#         self.age = 3


# Oso = Puppy("Oso", "2", "Maltese")
# Oso.get_puppy("$2000", "Malese Poodle")


class NBAPlayer():
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team
        self.salary = 0

    def add_salary(self, salary_amount):
        self.salary += salary_amount
    
    def fine(self, fine_amount):
        self.salary -= fine_amount
    
    def trade_player(self, new_team):
        self.team = new_team

lebron_james = NBAPlayer("Lebron James", "PG", "Lakers")
lebron_james.add_salary(809090909)
print("{} salary is ${}.".format(lebron_james.name, lebron_james.salary))

# carmelo_anthony = NBAPlayer("Carmelo Anthony", "SF", "Rockets")
# carmelo_anthony.add_salary(5000000)
# print("{} salary is ${}.".format(carmelo_anthony.name, carmelo_anthony.salary))