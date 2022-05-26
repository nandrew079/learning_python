class Cell:
    def __init__(self, number_cells):
        self.number_cells = int(number_cells)

    def __add__(self, other):
        return Cell(self.number_cells + other.number_cells)

    def __sub__(self, other):
        result = self.number_cells - other.number_cells
        if result >= 0:
            return Cell(result)
        else:
            raise ValueError('The number of cells is less than zero')

    def __mul__(self, other):
        return Cell(self.number_cells * other.number_cells)

    def __truediv__(self, other):
        return Cell(self.number_cells / other.number_cells)

    def __floordiv__(self, other):
        return Cell(self.number_cells // other.number_cells)


def make_order(cell, number_cells_in_line):
    result = ''
    for i in range(1, cell.number_cells + 1):
        if i % number_cells_in_line != 0:
            result += '*'
        else:
            result = f'{result}\n'

    return result


a = Cell(100)
b = Cell(31)

c = a + b
print(c.number_cells)

c = a - b
print(c.number_cells)

c = a * b
print(c.number_cells)

c = a / b
print(c.number_cells)

c = a // b
print(c.number_cells)

# c = b - a
# print(c.number_cells)

print(make_order(a, 7))
