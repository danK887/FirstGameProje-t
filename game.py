print('Приветствую в игре "Крестики-Нолики". для игры используйте английские сиволы "х" или "о" (регистр не важен).')
print ('Игровая доска строится по подобию нумпада -> 3 ряда, верхний ряд - 7,8,9 -> нижний ряд 1,2,3')
# функция для вывода игрокого поля (для примера можно вывести тестого поле, заполненое Х и О) выпослнив --test_board = ['#','X','O','X','O','X','O','X','O','X'] --  display_board(test_board)--

def display_board(board):

    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# функция для выбора игроком символа для игры
# выбереите каким символом вы хотите играть (делать выбор, пока игрок не выберит нужный Х или О, а не другой символ)

def player_input():
    marker = ''
    # игрок 1 делает выбор символа для игры
    while  not (marker == 'X' or marker =='O'): # пока маркер не равен Х или О , то
        marker = input('Игрок 1: Чем вы хотите играть "Х" или "О"? ' ).upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player_input()


# функция ставить на желаемое место определенный символ
def place_marker(board, marker, position):
    board[position] = marker
'''    
place_marker(test_board,'$',8)
display_board(test_board)
'''
#функция проверяет выиграл ли сивол (Х или О)
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # горизонталь сверху
    (board[4] == mark and board[5] == mark and board[6] == mark) or # горизонталь в середине
    (board[1] == mark and board[2] == mark and board[3] == mark) or # горизонталь снизу
    (board[7] == mark and board[4] == mark and board[1] == mark) or # вертикаль слева
    (board[8] == mark and board[5] == mark and board[2] == mark) or # вертикаль в середине
    (board[9] == mark and board[6] == mark and board[3] == mark) or # вертикаль справа
    (board[7] == mark and board[5] == mark and board[3] == mark) or # диагональ
    (board[9] == mark and board[5] == mark and board[1] == mark)) # диагональ

win_check(test_board,'X')

#рандом. какой игрок начинает игру первым
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Игрок 2'
    else:
        return 'Игрок 1'


def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#выбор позиции для выставления символа
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Выберите следующую клетку: (1-9) '))
        
    return position


#играем еще или нет?
def replay():
    
    return input('Вы хотите сыграть снова? Yes или No: ').lower().startswith('y')


import time
print('Добро пожаловать в игру Крестики-Нолики!')
time.sleep(0.2)
# цикл while для определения победы\ничьей
while True:
    # Настройка игры
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('Первым ходит ' + turn + '.')
    
    play_game = input('Вы готовы играть? Введите Yes или No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Игрок 1':
            # Ход Игрока 1
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Поздравляю! Вы выиграли!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 2'

        else:
            # Ход Игрока 2
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Игрок 2 выиграл!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 1'

    if not replay():
        break
