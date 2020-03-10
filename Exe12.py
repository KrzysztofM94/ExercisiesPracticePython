a = [5, 10, 15, 20, 25]

class Exe12:
    def take_num(self,list):
        return list[0], list[-1]




#class Exe12:
#     list_num = []
#
#     def take_many_num(self) -> []:
#
#         flag = True
#         while flag:
#             try:
#                 number = int(input("Give me a number: "))
#                 self.list_num.append(number)
#             except ValueError:
#                 if 0 >= self.list_num.__len__():
#                     flag = True
#                 else:
#                     flag = False
#         print("First num: {}, last num: {}".format(self.list_num[-1], self.list_num[0]))
#
#
def menu():
    exe_12 = Exe12()
    print(exe_12.take_num(a))


menu()
