import random


# Solution: Two copied lists


class ExeTen:
    a = [1, 2, 3, 4, 5, 6]
    b = [3, 4, 1, 2, 6, 5]
    new_list = []

    # def fill_lists(self):
    #
    #     size_list_a = random.randint(0, 10)
    #     size_list_b = random.randint(0, 10)
    #     for i in range(0, size_list_a, 1):
    #         self.a.append(random.randint(0, 10))
    #     for j in range(0, size_list_b, 1):
    #         self.b.append(random.randint(0, 10))

    # def check_len(self):
    #     if self.a.__len__() > self.b.__len__() or self.a.__len__() == self.b.__len__():
    #         for i, list in enumerate(self.a):
    #             if list not in self.new_list:
    #                 self.new_list.append(list)
    #         print(self.new_list)
    #     elif self.b.__len__() > self.a.__len__():
    #         for i, list_1 in enumerate(self.b):
    #             if list_1 not in self.new_list:
    #                 self.new_list.append(list_1)
    #         print(self.new_list)

    def fill_new_list(self):

        for i in self.a:
            if (i in self.new_list) == False:
                self.new_list.append(i)
        for j in self.b:
            if (j in self.new_list) == False:
                self.new_list.append(j)
        print(self.new_list)

    # def test(self):
    #
    #     abc = [1, 4, 2]
    #     defg = [3, 2, 3, 4, 17]
    #     nowa_lista = []
    #
    #     x = all(elem in nowa_lista for elem in abc)
    #     print(x)
    #
    #     results = len(set(abc)) <= xyz
    #
    #     if results:
    #         print("Znajduje się")
    #     else:
    #         print("Nie znajduje się")

    # def test_1(self):
    #     listOfStrings = [1, 2, 3, 4, 5, 6, 9, 9, 9, 9]
    #     result = False
    #     if len(listOfStrings) > 0:
    #         result = all(elem == 1 for elem in listOfStrings)
    #
    #     if result:
    #         print("All Elements in List are Equal")
    #     else:
    #         print("All Elements in List are Not Equal")


def menu():
    exe = ExeTen()
    # exe.test_1()
    # exe.fill_lists()
    # exe.test()
    exe.fill_new_list()


menu()
