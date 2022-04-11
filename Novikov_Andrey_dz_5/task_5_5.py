src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_set = set()
tmp = set()
for item in src:
    if item not in tmp:
        unique_set.add(item)
    else:
        unique_set.discard(item)
    tmp.add(item)
result = [item for item in src if item in unique_set]
print(result)
