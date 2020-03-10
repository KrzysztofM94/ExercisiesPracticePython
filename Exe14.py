a = [1, 2, 3, 4, 5, 6, 1, 1, 2, 3, 4, 66, 5, 3, 13, 3, 5, 7]


class Exe14:

    def take_list(self, old_list):
        b = set(old_list)
        return print(b)


def menu():
    exe_14 = Exe14()
    exe_14.take_list(a)


menu()
