""" Factorial Series """
def fact(n):
    if n < 1:
        return 1
    else:
        number = n * fact(n-1)
        return number
a = int(input("Enter a number to find the factorial: "))
print(fact(a))

""" Fibbonacci Series """
def fib(m):
    if m == 0 or m == 1:
        return 1
    else:
        number2 = fib(m-1) + fib(m-2)
        return number2

b = int(input("Enter a number to find the fibbonacci value: "))
print(fib(b))
 