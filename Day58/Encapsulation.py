""" Encapsulation or in a layman's term -> data hiding """
class Player:
    def __init__(self,name,age,position):
        self.__name = name # __ is used to make it as a private attribute.
        self.__age = age
        self.__position = position

    @property
    def Name(self):
        return self.__name

    @Name.setter   
    def Name(self,value):
        if value == "Bhosale":
            self.__name = "Default Name"
        else:
            self.__name == value

    @staticmethod
    def newmethod():
        print("This is a static method.")


p1 = Player("Shivam",21,"Mid-Field")
print(p1.Name)

p1.Name = ("Bhosale")
print(p1.Name)

Player.newmethod()