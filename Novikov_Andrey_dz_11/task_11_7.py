class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + self.y * other.x
        return ComplexNumber(x, y)

    def __str__(self):
        return f'{self.x} + i{self.y}'


num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(4, 5)
print(num1 + num2)
print(num1 * num2)
