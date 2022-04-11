result_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list_data = line.split('-')
        remote_addr = list_data[0].strip()
        if remote_addr in result_dict:
            result_dict[remote_addr] += 1
        else:
            result_dict[remote_addr] = 1
max_count = max(result_dict.values())
for key, val in sorted(result_dict.items(), key=lambda x: x[1], reverse=True):
    print(key, val)
    break
