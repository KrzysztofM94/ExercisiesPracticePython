# Main Solutiuon
# number = int(input("Writing the number: "))
# if (number % 2 == 0):
#     print("{} is even.".format(number))
# else:
#     print("{} is odd.".format(number))

# Extras: 1
number = int(input("Writing the number: "))
if (number % 2 == 0):
    if (number % 4 == 0):
        print("{} is multiple 4.".format(number))
    else:
        print("{} is even.".format(number))
else:
    print("{} is odd.".format(number))
