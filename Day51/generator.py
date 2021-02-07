import sys

def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(100)

for x in range(1,10):
    print(next(values))


print("Size: {} bytes".format(sys.getsizeof((values))))


def infinite_sequences():
    result = 1
    while True:
        yield result
        result += 5
values2 = infinite_sequences()

for i in range(1,10):
    print(next(values2))

print("Size: {} bytes".format(sys.getsizeof((values2))))

def iter_sequences(num):
    flag = 1
    while True:
        yield flag
        flag *= 10
num = int(input("Enter a number: "))
values3 = iter_sequences(num)

for j in range(1,10):
    print(next(values3))

