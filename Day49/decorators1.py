def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt','a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}\n")
            f.write(f"{fname} returned value {value}\n")

        return value
    return wrapper

@logged
def add(x,y):
    return x + y

@logged
def sub(x,y):
    return x-y

@logged
def mul(x,y):
    return x*y

@logged
def div(x,y):
    return x/y

print(add(30,20))
print(sub(30,20))
print(mul(30,20))
print(div(30,20))
