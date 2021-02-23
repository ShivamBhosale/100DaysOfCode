""" Rewind 5 """
def partition(num,low,high):
    pivot = num[(low+high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while num[i] < pivot:
            i += 1
        j -= 1
        while num[j] > pivot:
            j -= 1
        if i >= j:
            return j

        num [i], num [j] = num[j], num[i]

def quick_sort(num):
    def quick_sort2(items,low,high):
        if low < high:
            split_index = partition(items,low,high)
            quick_sort2(items,low,split_index)
            quick_sort2(items,split_index + 1, high)
    quick_sort2(num,0,len(num)-1)
    return num

n=int(input("Enter the number of elements in the array: "))
a=list(map(int,input("Enter the elements in the array: ").strip().split()))[:n]
print("Array before the quick sort: ",a)
print("Array after the quick sort:",quick_sort(a))

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
