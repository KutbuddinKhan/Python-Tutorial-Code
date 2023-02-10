class Employee:
    no_of_leves = 8
    pass


kkhan = Employee()
kasim = Employee()

kkhan.name = "Kutbuddin khan"
kkhan.salary = 500
kkhan.role = 'Student'

kasim.name = "kasim khan"
kasim.salary = 400
kasim.role = 'Student'

print(kkhan.name)
print(kasim.no_of_leves)
print(kkhan.no_of_leves)
print(Employee.__dict__)  # __dict__ ek attribute hai
kasim.no_of_leves = 9
print(kasim.__dict__)
print(Employee.no_of_leves)
