s1 = 'Hello'
s2 = 'World'

s1 = list(s1)
s2 = list(s2)

# print(s1)
# print(s2)

if len(s1) >= len(s2):
    big = s1
    small = s2
else:
    big = s2
    small = s1

# print(big)
# print(small)

res = []

for i in big:
    if i in small and i not in res:
        res.append(i)

res.sort()

# print(res)

for i in res:
    print(i)
