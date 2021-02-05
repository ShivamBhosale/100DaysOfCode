def myDecorator(function):
     
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("I'm decorating the function.")
        return return_value
        
    return wrapper

@myDecorator

def hello(Person):
    print(f"Hello {Person}")
    return  f"Hello {Person}"

print(hello("Shivam"))

