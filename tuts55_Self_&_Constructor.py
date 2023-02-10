# print("This is self and constructor tutorials")
class Employee:
    no_of_leves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"Name is {self.name} Salary is {self.salary} and role is {self.role}"


kkhan = Employee("Kutbuddin khan", 500, 'Student')
# kasim = Employee()

# kkhan.name = "Kutbuddin khan"
# kkhan.salary = 500
# kkhan.role = 'Student'
#
# kasim.name = "kasim khan"
# kasim.salary = 400
# kasim.role = 'Student'

# print(kasim.printdetails())
print(kkhan.printDetails())
print(kkhan.salary)
print(kkhan.name)
print(kkhan.role)
