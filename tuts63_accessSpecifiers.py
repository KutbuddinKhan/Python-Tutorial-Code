# Public - public means koi bhi chiz jo har koi dekh sake
# Protected - protected means e.g mujhe apne ghar walo ko bhi kuch dikhna hai ya mai cheta hu wo bhi isse dekhe
# Private - private means srif mai dekh skta ho aor koi nhi

class Employee:
    no_of_leaves = 9
    var = 1
    _protec = 9
    __private = 100
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
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printGood(string):
        print("This is good " + string)

emp = Employee("Saad", 5000, "Porgrammer")
print(emp.var)
print(emp._protec)
print(emp._Employee__private)
