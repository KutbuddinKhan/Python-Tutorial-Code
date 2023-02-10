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


kasim = Employee("Kasim", "khan")
# kkhan = Employee("kutbuddin", 'khan')
# print(kasim.email)
# print(kasim.explain())

print(kasim.email)
kasim.fname = "KasimSamim"
print(kasim.email)

kasim.email = "this.that@kkhan.com"

print(kasim.fname)
print(kasim.lname)
print(kasim.email)

del kasim.email
print(kasim.email)
kasim.email = "kasim.that@kkhan.com"
print(kasim.email)
print(kasim.lname)
