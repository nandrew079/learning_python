class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_number = input('Enter a number: ')
inp_divisor = input('Enter the divisor: ')

try:
    int_number = int(inp_number)
    int_divisor = int(inp_divisor)

    if int_divisor == 0:
        raise MyZeroDivision('Division by zero')

    print(int_number / int_divisor)

except ValueError as err:
    print(err)

except MyZeroDivision as err:
    print(err)
