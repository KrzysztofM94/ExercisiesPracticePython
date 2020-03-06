number = int(input("Give me a number: "))
table_all_number = range(1, number + 1)

table_all_divisor = []
for i in table_all_number:
    if number % i == 0: table_all_divisor.append(i)
print(table_all_divisor)
