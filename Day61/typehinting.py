""" Typehinting """
def myfunction(mypara: int) -> str:
    return f"{mypara +10}"

def myfunction2(mypara2: str):
    print(mypara2)

myfunction2(myfunction(20))
