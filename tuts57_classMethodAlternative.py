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

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
#         one linear
        return cls(*string.split("-"))

kkhan = Employee("kutbuddin khan", 455, "student")
kasim = Employee("kasim khan", 450, "student")
aslam = Employee.from_dash("Aslam-40-student")

print("Aslam salary is:", aslam.salary)
print("Aslam no_of_leaves is:", aslam.no_of_leaves)

kkhan.change_leaves(34)
# print(kkhan.printdata())
# print(Employee.no_of_leaves)
