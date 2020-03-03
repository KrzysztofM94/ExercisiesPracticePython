import datetime

# Main Solution
# name = input("Write your name: ")
# age = int(input("Write your age: "))
# hundred_year = datetime.datetime.now()
# print("{} in {} years you well be 100!!!".format(name, (hundred_year.year + (100 - age))))

# Extras 1:
name = input("Write your name: ")
age = int(input("Write your age: "))
repeat = int(input("How many I will must repeat answer?"))
hundred_year = datetime.datetime.now()
message = "{} in {} years you well be 100!!! ".format(name, (hundred_year.year + (100 - age)))
print(message * repeat)

