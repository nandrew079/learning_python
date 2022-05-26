import sys


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('Few arguments')

    ind_line = int(sys.argv[1])
    new_sale = sys.argv[2]

    with open('task_6_7.txt', 'r+', encoding='utf-8') as f:
        for i in range(ind_line):
            f.readline()
        f.seek(f.tell())
        f.write(f'{new_sale}')
