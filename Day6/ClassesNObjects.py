class Person:
    #calling a construtor
    amount = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        
        Person.amount -= 1
    
    def __str__(self):
        return ("Name: {}, Age: {}, Height: {}".format(self.name,self.age,self.height))
    


x = Person("Shivam",21,156)
print(x)
y = Person("Superman",30,186)
print(y)
del y

print(Person.amount)