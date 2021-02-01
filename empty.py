input_list = [[1, 2, 3], [], [4, 5], [], [], [6, 7, 8]]
res_list = []
for i in input_list:
    if len(i) != 0:
        res_list.append(i)
print(res_list)
