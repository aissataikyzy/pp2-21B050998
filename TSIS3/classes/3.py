class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, a = 0, b = 0):
        Shape.__init__(self)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

a, b = list(map(int, input().split))
c = Rectangle(a, b)
print(c.area())
print(Rectangle().area())