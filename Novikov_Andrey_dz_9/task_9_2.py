class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass_asphalt(self, mass, height):
        return self._length * self._width * mass * height


mkad = Road(1500, 20)
print(mkad.calculate_mass_asphalt(20, 15))
