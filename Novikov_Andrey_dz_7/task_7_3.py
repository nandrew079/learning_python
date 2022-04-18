import os
from shutil import copy2

root_dir = os.path.join(os.getcwd(), 'my_project')
new_dir = os.path.join(root_dir, 'templates')
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            name_folder = os.path.basename(root)
            full_dir = os.path.join(new_dir, name_folder)
            if root == full_dir:
                continue
            if not os.path.exists(full_dir):
                os.mkdir(full_dir)

            copy2(os.path.join(root, file), os.path.join(full_dir, file))

