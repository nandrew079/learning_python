import os
import random


if __name__ == '__main__':
    dir_list = []
    dir_folder = os.getcwd()
    index_folder = 0
    with open('config.yaml', 'r', encoding='utf-8') as file:
        for line in file:
            entity_name = line

            index_folder = int(entity_name.find('|--') / 3)
            if index_folder < 0:
                break

            entity_name = entity_name.strip()
            entity_name = entity_name.replace('|', '')
            entity_name = entity_name.replace('-', '')
            entity_name = entity_name.replace(' ', '')

            is_file = entity_name.find('.') != -1

            if not is_file:
                dir_list.insert(index_folder, entity_name)
                full_dir = os.path.join(dir_folder, '\\'.join(dir_list[:index_folder + 1]))
                if not os.path.exists(full_dir):
                    os.mkdir(full_dir)
            else:
                full_dir = os.path.join(dir_folder, '\\'.join(dir_list[:index_folder]))
                full_dir = os.path.join(full_dir, entity_name)
                f_content = ''.join([str(random.randint(0, 255)) for _ in range(random.randrange(10 ** 5))])
                with open(full_dir, 'w') as f:
                    f.write(f_content)
