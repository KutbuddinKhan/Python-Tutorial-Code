class Employee:
    no_of_leaves = 9
    var = 8

    def __init__(self, aname, asalry, arole):
        self.name = aname
        self.salary = asalry
        self.role = arole

    def printDetails(self):
        return f"The name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good " + string)

class Player:
    no_of_games = 4
    var = 9

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printDetails(self):
        return f"The name is {self.name}, and the game is {self.game}"

class CoolProgrammer(Employee, Player):
    language = "python"
    var = 10

    def printLanguage(self):
        print(self.language)

kkhan = Employee("KKhan", 808, "Administrator")
kasim = Employee("Kasim", 1000, "Programmer")

saad = Player("Saad", ['Football'])
mohsin = CoolProgrammer("Mohsin", 5000, "coolProgrammer")
det = mohsin.printDetails()
mohsin.printLanguage()
print(det)
print(mohsin.var)
