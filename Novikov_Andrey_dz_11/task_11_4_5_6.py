def checking_quantity(func):
    def _wrapper(*args, **kwargs):
        try:
            if type(args[1]) == str:
                raise ValueError
        except ValueError:
            print('Quantity is not number')
        else:
            func(*args, **kwargs)

    return _wrapper


class Warehouse:
    TOTAL_REMAINS = {}
    REMAINS_BY_DIVISION = {}

    @staticmethod
    @checking_quantity
    def receipt_product(product, quantity=0):
        """ Changes the rest of the product to number """
        quantity_product = Warehouse.TOTAL_REMAINS.get(product)
        if quantity_product is None:
            Warehouse.TOTAL_REMAINS[product] = 0
        Warehouse.TOTAL_REMAINS[product] += quantity

    @staticmethod
    @checking_quantity
    def move_to_division(product, quantity, to_division, from_division=''):
        """Moves the product in the quantity 'quantity' to the division 'to_division' from the division 'from_division'
        if it is specified"""

        Warehouse.change_quantity_product_in_division(product, quantity, to_division)

        if from_division != '':
            Warehouse.change_quantity_product_in_division(product, -quantity, from_division)

    @staticmethod
    @checking_quantity
    def change_quantity_product_in_division(product, quantity, division):
        """Moves the product in the quantity 'quantity' to the division 'division'"""
        remains_division = Warehouse.REMAINS_BY_DIVISION.get(division)
        if remains_division is None:
            Warehouse.REMAINS_BY_DIVISION[division] = {}
            remains_division = Warehouse.REMAINS_BY_DIVISION[division]

        quantity_product = remains_division.get(product)
        if quantity_product is None:
            remains_division[product] = 0
        remains_division[product] += quantity


class OfficeEquipment:
    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name, color=False):
        super().__init__(name)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, for_a3=False):
        super().__init__(name)
        self.for_a3 = for_a3


class Xerox(OfficeEquipment):
    def __init__(self, name, for_a5=False):
        super().__init__(name)
        self.for_a5 = for_a5


printer = Printer('test1', True)
scanner = Scanner('test2', False)
xerox = Xerox('test3', True)

print(printer.name, printer.color)
print(scanner.name, scanner.for_a3)
print(xerox.name, xerox.for_a5)

Warehouse.receipt_product(printer.name, 100)
Warehouse.receipt_product(scanner.name, '200')
Warehouse.receipt_product(xerox.name, 300)

print(Warehouse.TOTAL_REMAINS)

Warehouse.move_to_division(printer.name, 20, 'division1')
Warehouse.move_to_division(printer.name, 80, 'division2')
Warehouse.move_to_division(printer.name, 40, 'division1', 'division2')

print(Warehouse.REMAINS_BY_DIVISION)
