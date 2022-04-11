list_users = []
with open('users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        list_data = line.split(',')
