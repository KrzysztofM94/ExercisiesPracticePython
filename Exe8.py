class Players():
    flag = True
    value = None

    def startGame(self):

        while flag:
            input_data = str(input("What you choice: \n"
                                   "1: Rock \n"
                                   "2: Scissors \n"
                                   "3: Paper \n")).lower()
            flag = self.whatChoice(input_data)

    def secondPlayer(self):
        print()

    def whatChoice(self, input_data):

        if (input_data == 'rock' or input_data == '1') or (input_data == 'scissors' or input_data == '2') or (
                input_data == 'paper' or input_data == '3'):
            self.value = input_data
            return False

        else:
            print("\n Wrong choice. Try again! \n")
            return True


class CompareValue(Players):

    # def winnerIs(self,player_1, player_2):
    #     if(player_1 == 'rock' and player_2 == 'scissors')


def menu():
    player1 = Players()
    player1.startGame()
    player2 = Players()
    player2.startGame()


menu()
