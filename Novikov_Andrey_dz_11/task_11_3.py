import re


class CheckingForNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


RE_NUMBER = re.compile(r'^\d{1,}$')
result_list = []

while True:
    inp_data = input('Enter a number or "stop": ')
    if inp_data == 'stop':
        break
    match = RE_NUMBER.match(inp_data)
    try:
        if match is None:
            raise CheckingForNumber("You didn't enter number")
        result_list.append(int(inp_data))
    except CheckingForNumber as err:
        print(err)

print(result_list)
