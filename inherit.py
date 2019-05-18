# Filename: inherit.py
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
        print('Initialized SchoolMembers:%s'%self.name)

    def tell(self):
        '''Tell my details.'''
        print('My name: %s, Age:%s, live in %s'%(self.name,self.age,self.adress))

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self,name,age,adress,salary):
        SchoolMember.__init__(self,name,age,adress)
        self.salary=salary
        print('Initialized Teacher:%s' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:%s'%self.salary)


class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, adress, marks):
        SchoolMember.__init__(self, name, age, adress)
        self.marks = marks
        print('Initialized student:%s' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:%d' % self.marks)


t=Teacher('Mrs',33,'nankai',15000)
s=Student('Hao',23,'nankai',94)

print()

members=[t,s]
for a in members:
    a.tell()