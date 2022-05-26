import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('Few arguments')

    with open('task_6_7.txt', 'a', encoding='utf-8') as f:
        if os.stat('task_6_7.txt').st_size != 0:
            f.write('\n')
        f.write(sys.argv[1])
