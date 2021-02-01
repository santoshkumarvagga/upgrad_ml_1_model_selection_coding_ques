lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Input list is :", lis)
k = 3
print("Given k is: ", k)
lis_len = len(lis)
print("length of input list is: ", lis_len)
no_of_times = lis_len // k
res = []
start = 0
iter_var = k
times_var = 0
while True:
    if iter_var <= k*no_of_times:
        # logic part
        if iter_var % k == 0:
            res.append(lis[start:iter_var])
            print("res now is: ", res)
            start = iter_var
        iter_var += 1
    else:
        print("breaking")
        break
print(iter_var)
# appending rest of elements in one list
if iter_var <= lis_len:
    for i in range((k * no_of_times), lis_len):
        res.append(lis[i::])
        break

print("resultant list is: ", res)
for i in res:
    print(i)
