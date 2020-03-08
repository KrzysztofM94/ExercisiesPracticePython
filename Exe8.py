class Players():
    nick_player = None
    flag = True
    value = None

    def playerNick(self):
        self.nick_player = str(input("Give me your nick/name: ")).rstrip()

    def startGame(self):

        while self.flag:
            input_data = str(input("What you choice: \n"
                                   "1: Rock \n"
                                   "2: Scissors \n"
                                   "3: Paper \n")).lower()
            self.flag = self.whatChoice(input_data)

    def secondPlayer(self):
        print()

    def whatChoice(self, input_data) -> bool:

        if (input_data == 'rock' or input_data == '1'):
            self.value = 'rock'
            return False
        elif input_data == 'scissors' or input_data == '2':
            self.value = 'scissors'
            return False
        elif (input_data == 'paper' or input_data == '3'):
            self.value = 'paper'
            return False
        else:
            print("\n Wrong choice. Try again! \n")
            return True


class CompareValue(Players):

    def winnerIs(self, player_1, player_2):
        if (player_1.value == 'rock' and player_2.value == 'scissors') or (
                player_1.value == 'scissors' and player_2.value == 'paper') or (
                player_1.value == 'paper' and player_2.value == 'rock'):
            print("Player {} win!!".format(player_1.nick_player))
        elif player_1.value == player_2.value:
            print("Gracz {} i {} zremisowali!!!".format(player_1.nick_player, player_2.nick_player))
        else:
            print("Player {} win!!".format(player_2.nick_player))


def menu():
    player1 = Players()
    player2 = Players()

    player1.playerNick()
    player1.startGame()

    player2.playerNick()
    player2.startGame()
    compareValue = CompareValue()
    compareValue.winnerIs(player1, player2)

menu()
