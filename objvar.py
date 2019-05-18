#Filename:objvar.py
class Person:
    '''Represents a person'''
    population=0

    def __init__(self,name):
        print('初始化数据')
        self.name=name
        print('Initializing %s'%self.name)
        # When this person is created, he/she
        # adds to the population
        Person.population+=1

    def __def__(self):
        '''I am dying.'''
        Person.population-=1

        if Person.population==0:
            print('I am the last one')
        else:
            print('There still %d people left'%Person.population)
    def sayHi(self):
        '''Greeting by the person.
        Really, that's all it does.'''
        print('Hi, my name is %s'%self.name)
    def howMany(self):
        '''Prints the current population.'''
        if Person.population==1:
            print('I am the only person here')
        else:
            print('We have %d persons here'%Person.population)

andy=Person('andy')
andy.sayHi()
andy.howMany()

kat=Person('kat')
jack=Person('jack')
kat.sayHi()
kat.howMany()

jack.__def__()
andy.sayHi()
andy.howMany()
