import datetime

# Main Solution
name = input("Write your name: ")
age = int(input("Write your age: "))
hundred_year = datetime.datetime.now()
print("{} in {} years you well be 100!!!".format(name, (hundred_year.year + (100 - age))))
