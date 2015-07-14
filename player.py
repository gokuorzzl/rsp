class Player:
    coin = 0
    win = 0
    lose = 0
    drew = 0
    win_win = 0
    best_win_win = 0
    log =0
    best_batting = 0

    def __init__(self):
        self.coin += 100
        print('개발자 밝을명이 게임을 실행한 플레이어에게 100코인을 '
              '선물하였습니다.')

    def print_info(self):
        print('전적 : 총', self.log , '전 <', self.win, '승', self.drew,
              '무', self.lose, '패>')
        print(
            '연승 : 현재',
            self.win_win,
            '연승 <최고 기록 :',
            self.best_win_win,
            '>',
        )
        print('현재 코인:', self.coin)
