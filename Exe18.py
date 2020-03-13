import random


class CowsBulls:
    digital = random.randint(1000, 9999)
    cows = 0
    bulls = 0
    tmp_cows = 0

    def input_num(self):
        flag = True
        print("Welcome to the Cows and Bulls Game!\n" + " Enter a number: ")
        # print("{}\n".format(self.digital))

        while flag:

            try:
                number = input()
                for i, num in enumerate(number):
                    if self.digital.__str__()[i] == str(num):
                        self.cows += 1
                if self.cows == 4:
                    print("You win!! Generating number is: {}".format(self.digital))
                    flag = False
                if self.cows < self.tmp_cows:
                    self.bulls = self.tmp_cows - self.cows

                print("{} cow, {} bull".format(self.cows, self.bulls))
                self.tmp_cows = self.cows
                self.cows = self.bulls = 0

            except ValueError:
                print("Input data must be number. Try again!")


def menu():
    cows_bulls = CowsBulls()
    cows_bulls.input_num()


menu()
