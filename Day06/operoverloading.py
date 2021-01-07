class Vector:
    def __init__(self,x,y):
         self.x = x
         self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)

vec1 = Vector(10,5)
vec2 = Vector(12,6)

print(vec1)
print(vec2)

vec3 = vec1 + vec2
vec4 = vec1 - vec2

print(vec3)
print(vec4)