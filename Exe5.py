a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Main Solution
all_common = []

if a.__len__() < b.__len__():
    for i in b:
        if i in a:
            all_common.append(i)
else:
    for i in a:
        if i in b:
            all_common.append(i)
print(all_common)

