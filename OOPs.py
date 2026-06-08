class Student:
    pass

s1 = Student()
s1.name = "Risha"
s1.age = "22"
s1.course = "BCA"
s1.city = "Pamban"
s1.phn = "1234567890"

print(type(s1))#to find the type of an object or where it belongs too..

s2 = Student()
s2.name = "Kayal"
print(s1.name,s2.name)

print(type(s2))
