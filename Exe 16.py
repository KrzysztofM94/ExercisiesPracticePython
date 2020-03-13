# Main Solution + extra
import string
import random


class Exe16:

    def size_pass(self):
        flag = True
        while flag:
            try:
                size = int(input("How long password generation: "))
                flag = False
            except ValueError:
                print("Input data not is a number. Please try again  ")
        print(self.password_gen(size))

    def password_gen(self, size):
        password = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password) for i in range(size))

    # def tests(self, size=2):
    #     password = 'a' + 'b'
    #     print(''.join(random.choice(password) for i in range(size)))


def menu():
    exe_16 = Exe16()
    exe_16.size_pass()
    # exe_16.tests()


menu()
