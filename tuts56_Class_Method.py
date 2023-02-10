class Employee:
    no_of_leaves = 9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdata(self):
        return f"the name of {self.name}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

kkhan = Employee("kutbuddin khan", 455, "student")
kasim = Employee("kasim khan", 450, "student")
kkhan.change_leaves(34)
# print(kkhan.printdata())
print(Employee.no_of_leaves)
