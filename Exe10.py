# Solution: Two copied lists

class ExeTen():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    new_list = []

    def check_len(self):
        if self.a.__len__() > self.b.__len__():
            for i, l in enumerate(self.a):
                if not (self.a[i] == self.new_list) and self.a[i] == self.b[i]:
                    self.new_list.append(self.a[i])
            print(self.new_list)
        elif self.b.__len__() > self.a.__len__():
            for i, l in enumerate(self.b):
                if not (self.b[i] == self.new_list) and self.b[i] == self.a[i]:
                    self.new_list.append(self.b[i])
            print(self.new_list)


def menu():
    exe = ExeTen()
    exe.check_len()


menu()
