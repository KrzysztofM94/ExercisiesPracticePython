class Exe11:

    def get_integer(self, help_text="Give me a number: ") -> int:
        return int(input(help_text))

    def text_no_prime(self, number):
        print("{} not is a prime.".format(number))
        self.is_prime()

    def text_is_prime(self, number):
        print("{} is a prime.".format(number))
        self.is_prime()

    def is_prime(self):
        counter = 0
        geting_int = self.get_integer()

        if (geting_int <= 1):
            self.text_no_prime(geting_int)
        else:
            result = [i for i in range(1, geting_int + 1)]
            for i in result:
                if geting_int % i == 0:
                    counter += 1
                if (counter > 2):
                    self.text_no_prime(geting_int)
                    break
            if counter == 2:
                self.text_is_prime(geting_int)


def menu():
    exe_11 = Exe11()
    exe_11.is_prime()


menu()
