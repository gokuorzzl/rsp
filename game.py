import random
import sys

class Game:
    hands = ('가위', '바위', '보')

    def __init__(self, player):
        self.player = player
        self.batting_coin = 0
        self.bonus = 0

    def game_start(self):
        batting_coin = input('배팅할 코인량을 입력해주세요:')
        try:
            self.batting_coin = int(batting_coin)
        except ValueError:
            print('잘못된 입력입니다.')
            return
        else:
            if self.batting_coin > self.player.coin:
                print('잘못된 입력입니다.')
                return
        self.game()

    def game(self):
        my_hand = input('가위 바위 보!:')
        if my_hand in self.hands:
            com_hand = random.choice(self.hands)
            print('플레이어<', my_hand ,'>', '컴퓨터<', com_hand, '>')
            if my_hand == com_hand:
                self.draw()
            elif my_hand == '가위' and com_hand == '바위':
                self.lose()
            elif my_hand == '가위' and com_hand == '보':
                self.win()
            elif my_hand == '바위' and com_hand == '보':
                self.lose()
            elif my_hand == '바위' and com_hand == '가위':
                self.win()
            elif my_hand == '보' and com_hand == '가위':
                self.lose()
            elif my_hand == '보' and com_hand == '바위':
                self.win()
        else:
            print('잘못 입력 하셨습니다.')
            self.game()

    def win(self):
        self.player.coin += self.batting_coin
        print('이겼습니다.')
        self.player.win += 1
        self.player.win_win += 1
        self.player.log += 1
        if self.player.best_win_win < self.player.win_win:
            self.player.best_win_win = self.player.win_win
            if self.player.win_win > 1:
                self.bonus = 10*(self.player.win_win**2)

        print(self.player.win_win, '연승 중 입니다. 연승보너스로',
              self.bonus, '코인이 추가 지급 됩니다.')

    def draw(self):
        print('비겼습니다.')
        self.game()
        self.player.drew += 1
        self.player.log += 1

    def lose(self):
        self.player.coin -= self.batting_coin
        print('졌습니다.')
        self.player.lose += 1
        self.player.log += 1
        self.player.win_win = 0
        self.bonus = 0
        if self.player.coin == 0:
            print('파산하셨습니다.', file=sys.stderr)
            raise SystemExit()

