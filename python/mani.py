nested_list = [[1, 2], [3, 4], [5, 6]]

result = list(map(lambda sublist: list(map(lambda x: x + 5, sublist)), nested_list))

print(result)