class Student(object):
    name = 'Student'


s = Student()

print(s.name)

s.name = "Karol"
print(s.name)

del s.name

print(s.name)
