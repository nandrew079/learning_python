import os
import sys


def get_multiplicity_10(size_f, num):
    if size_f / num > 10:
        num = get_multiplicity_10(size_f, num * 10)
    return num


if __name__ == '__main__':
    root_dir = ''
    result_dict = {}
    try:
        root_dir = sys.argv[1]
    except IndexError as e:
        print('Введите путь к каталогу')
        exit(1)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            size = os.stat(os.path.join(root, file)).st_size
            multiple = get_multiplicity_10(size, 10)
            if multiple in result_dict:
                temp_list = list(result_dict[multiple])
                temp_list[0] += 1
                if not ext in temp_list[1]:
                    temp_list[1].append(ext)
                result_dict[multiple] = tuple(temp_list)
            else:
                ext_list = [ext]
                result_dict[multiple] = (1, ext_list)

    sorted_tuple = sorted(result_dict.items(), key=lambda x: x[0])
    print(dict(sorted_tuple))
