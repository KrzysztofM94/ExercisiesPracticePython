import random


class GameOne():
    random_number = None
    answer = int
    tries = 0
    flag = True

    def random_number(self) -> int:
        self.random_number = random.randint(0, 9)

    def input_answer(self) -> int:
        while self.flag:
            try:
                self.answer = int(input("Guess the number from 0 to 9: "))
            except ValueError:
                print("\n Musisz wybrać liczbę od 0 do 9. \n")
                continue
            self.flag = False
            self.how_close()

    def how_close(self) -> str:
        if self.answer > self.random_number:
            print("The drawn number is larger.")
            self.tries = self.tries + 1
            self.flag = True
            self.answer = None
            self.input_answer()

        elif self.answer < self.random_number:
            print("The drawn number is smaller.")
            self.tries = self.tries + 1
            self.flag = True
            self.answer = None
            self.input_answer()
        else:
            if self.tries > 0: self.tries = self.tries + 1
            print("Your number: {}, draw number: {}, number of tries: {} ".format(self.answer, self.random_number,
                                                                                  self.tries))


def menu():
    game_one = GameOne()
    game_one.random_number()
    game_one.input_answer()


menu()
