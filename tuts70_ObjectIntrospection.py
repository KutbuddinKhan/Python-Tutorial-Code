class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@Kkhan.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if None == self.fname or self.lname is None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@kkhan.com"

    @email.setter
    def email(self, string):
        print("Setting now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill", "f")
# print(skillf.email)
# print(type("this is string"))
# print(id("this is string"))
# print(id("this is "))


# print(type(skillf))

o = "this is string"
# print(dir(skillf))


import inspect

print(inspect.getmembers(skillf))

# quiz
# using inspect module help who inspect all module
