class A:
    classVar1 = "I am class variable in class A"

    def __init__(self):
        self.Var1 = "I am inside class A's constructor"
        self.classVar1 = "Instance variable in class A"
        self.special = "special"

class B(A):
    classVar1 = "I am class variable in class B"

    def __init__(self):
        self.Var1 = "I am inside class B's constructor"
        self.classVar1 = "Instance variable in class B"
        super().__init__()
        print(super().classVar1)

a = A()
b = B()
print(b.special, b.Var1, b.classVar1)
