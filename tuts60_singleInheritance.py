class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"The name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def form_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good "+ string)

class Programmer(Employee):
    no_of_holiday = 10

    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"The Programmer name is {self.name}, salary is {self.salary} and is role is {self.role}. and The languages are {self.languages}"

kkhan = Employee("Kkhan", 255, "Instructor")
kasim = Employee("kasim", 2355, "Programmer")

aslam = Programmer("Aslam", 4000, "Programmer", ['python', 'javaScript', 'C', 'Java'])
mohsin = Programmer("Mohsin", 5000, "WebDeveloper", ['python', 'javaScript', 'C'])

print(aslam.printprog())
print(aslam.no_of_holiday)
# print(aslam.printDetails())
