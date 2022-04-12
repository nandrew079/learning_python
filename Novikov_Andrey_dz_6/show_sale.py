import sys
from itertools import islice

if __name__ == '__main__':
    start = None
    finish = None

    if len(sys.argv) > 1:
        start = int(sys.argv[1]) - 1
    if len(sys.argv) > 2:
        finish = int(sys.argv[2])

    with open('task_6_7.txt', 'r', encoding='utf-8') as f:
        lines = islice(f, start, finish)
        print(*lines, sep='')
