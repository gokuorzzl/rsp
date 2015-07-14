from player import Player
from game import Game

def intro():
    print('*** 본격 사행성 게임 ***')
    print('-v.1.2 Anti-GRB')
    print('-Create by 밝을명 \n')

def main():
    intro()
    player = Player()

    while True:
        command = input('명령어를 입력해주세요. (명령어 목록: 도움말):')
        print(command)
        if command == '종료':
            break
        elif command == '승부':
            print('게임을 시작합니다.')
            game = Game(player)
            game.game_start()
        elif command == '정보':
            player.print_info()


if __name__ == '__main__':
    main()
