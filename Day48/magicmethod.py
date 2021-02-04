class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __repr__(self):
        return f'X: {self.x}, Y: {self.y}, Z: {self.z}'

    def __len__(self):
        return 10
    
    def __call__(self):
        print("Hello this a call function")

    

v1 = Vector(10,20,50)
v2 = Vector(50,30,100)

v3 = v1 + v2

print(v3.x,v3.y,v3.z)
print("Whole Vector: ",v3)
print(len(v3))
v3()






     