class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"The name is {self.name}, Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good " + string)
        # return 'thenga'


kkhan = Employee("Kkhan", 155, "Instructor")
saad = Employee("Saad", 555, "Programmer")
kasim = Employee("Kasim", 355, "Administrator")
print(kkhan.printDetails())
print(kasim.printGood("Kkhan "))
