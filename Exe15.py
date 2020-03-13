class Exe15:

    def input_word(self):
        words = (input("Give me a long string containning multiple words: ")).split()
        print(" ".join(words[::-1]))


def menu():
    exe_15 = Exe15()
    exe_15.input_word()


menu()
