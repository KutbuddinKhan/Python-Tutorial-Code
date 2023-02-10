# Google search mapping operator function
# Operator overloading and Dundar method: ye __ se strt aor end hote hai expmple __init__
class Employee:
    no_of_leaves = 9

    def __init__(self, aname, asalry, arole):
        self.name = aname
        self.salary = asalry
        self.role = arole

    def printDetails(self):
        return f"The name is {self.name},salary is {self.salary} and role is {self.role}"

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee({self.name}, {self.salary}, {self.role})"

    def __str__(self):
        return f"The name is {self.name}, salary is {self.salary}, and role is {self.role}"

emp1 = Employee("Kkhan", 100, "Programmer")
emp2 = Employee("Rohan", 10, "Cleaner")
print(emp1)
print(repr(emp1))
print(str(emp1))
# print(emp1 + emp2)
# print(emp1 / emp2)

