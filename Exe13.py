class Exe13:

    def fib(self, size):
        n_1 = 0
        n_2 = 0
        for i in range(0, size):
            if i == 0:
                n_1 = i
                print("{} ".format(n_1))
            elif i == 1:
                n_2 = n_1
                n_1 = i
                print("{} ".format(n_1))
            elif i > 1:
                fib_num = n_1 + n_2
                print("{} ".format(fib_num))
                n_2 = n_1
                n_1 = fib_num

    def fib_text(self,bla):
        print(bla)
        self.fib(self.size_fib())

    def size_fib(self) -> int:
        flag = True
        while flag:
            try:
                size = int(input("How many Fibonnaci number want to generate: "))

                if size < 0:
                    print("Fibonacci sequence cannot be less from 0")
                else:
                    flag = False
                    return size

            except ValueError:
                print("You must give me a number. Please try again.")


def menu():
    exe_13 = Exe13()
    exe_13.fib_text(13)


menu()
