a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
import random

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

# Extras: 1

# aa = []
# bb = []
# random_size_aa = random.randint(0,20)
# random_size_bb = random.randint(0,20)
#
# for i in range(0,random_size_aa):
#     aa.append(random.randint(0,20))
# for i in range(0,random_size_bb):
#     bb.append(random.randint(0,20))

# Extras: 2
print([lista for lista in b if lista in a])()







