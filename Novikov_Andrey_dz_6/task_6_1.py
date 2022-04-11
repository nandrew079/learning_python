result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list_data = line.split('-')
        remote_addr = list_data[0].strip()
        list_data_request = list_data[2].split('"')
        list_type_request = list_data_request[1].split(' ')
        request_type = list_type_request[0]
        requested_resource = list_type_request[1]
        result.append((remote_addr, request_type, requested_resource))
print(result)
