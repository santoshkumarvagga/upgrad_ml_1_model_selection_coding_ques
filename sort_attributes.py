input_1 = [('Ram', 23, 3000), ('Mohan', 22, 4000), ('Suresh', 19, 8000)]
input_2 = 2

# get each tuple
# navigate to index
# add element to list
# sort list
# pick each element, add its tuple to result list
# print each element of result list

res = []
for i in input_1:
    res.append(i[input_2])

res.sort()

print("Sorted is:", res)

def get_tuple(x):
    for k in input_1:
        if x == k[input_2]:
            print("returning tuple of :", x)
            return k

result = []

for i in res:
    result.append(get_tuple(i))

for i in result:
    print(i)
