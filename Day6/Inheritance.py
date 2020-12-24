class Person:
    #calling a construtor
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self):
        return ("Name: {}, Age: {}, Height: {}".format(self.name,self.age,self.height))

    def get_older(years):
        self.age += years

#Inheritance 
class Worker(Person):
    #Accessing the parent class using Super
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name,age,height)
        self.salary = salary
    
    #Override
    def __str__(self):
        text = super(Worker,self).__str__()
        text += ", Salary: {}".format(self.salary)
        return text

    def calc_year_sar(self):
        return self.salary * 12

Worker1 = Worker("Shivam",21,156,500000)
print(Worker1)
print(Worker1.calc_year_sar())
