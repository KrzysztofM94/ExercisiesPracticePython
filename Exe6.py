def takeData():
    inputs = input("Give me a word: ")

    print("Słowo które podałeś {} palidnomem.".format(CheckPalindrom(inputs)))


def CheckPalindrom(inputWord):
    palindrom = inputWord[::-1]
    print(palindrom)

    if (inputWord == palindrom):
        return "jest"
    else:
        return "nie jest"


def Mainmenu():
    takeData()


Mainmenu()
