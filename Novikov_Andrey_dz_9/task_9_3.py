class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.surname.capitalize()} {self.name.capitalize()}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus'] 


alex = Position('Alex', 'Petrov', 'Programmer', 100000, 50000)
print(alex.get_full_name())
print(alex.get_total_income())
