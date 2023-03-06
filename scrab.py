# importing modules
import random
import re

# loading file with all possible words and creating a list of it
file = open('slowniczek.txt', 'r', encoding='utf-8')
allwords = []
for x in file:
    x = x.rstrip()
    x = x.upper()
    allwords.append(x)

# Dictionary with point value for every lettter
valuetable = {'*': 0, 'A': 1, 'E': 1, 'I': 1, 'N': 1, 'O': 1, 'R': 1, 
'S': 1, 'W': 1, 'Z': 1, 'C': 2, 'D': 2, 'K': 2, 'L': 2, 'M': 2, 
'P': 2, 'T': 2, 'Y': 2, 'B': 3, 'G': 3, 'H': 3, 'J': 3, 'Ł': 3, 
'U': 3, 'Ą': 5, 'Ę': 5, 'F': 5, 'Ó': 5, 'Ś': 5, 'Ż': 5, 'Ć': 6, 
'Ń': 7, 'Ź': 9}

# Alphabet
alphabet = ['*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 
            'Y', 'Z', 'Ó', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ś', 'Ź', 'Ż']


# Bag with letters
bag = ['*', '*', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
       'E', 'E', 'E', 'E', 'E', 'E', 'E', 'I', 'I', 'I', 'I', 
       'I', 'I', 'I', 'I', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 
       'O', 'O', 'O', 'O', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 
       'S', 'W', 'W', 'W', 'W', 'Z', 'Z', 'Z', 'Z', 'Z', 'C', 
       'C', 'C', 'D', 'D', 'D', 'K', 'K', 'K', 'L', 'L', 'L', 
       'M', 'M', 'M', 'P', 'P', 'P', 'T', 'T', 'T', 'Y', 'Y', 
       'Y', 'Y', 'B', 'B', 'G', 'G', 'H', 'H', 'J', 'J', 'Ł', 
       'Ł', 'U', 'U', 'Ą', 'Ę', 'F', 'Ó', 'Ś', 'Ż', 'Ć', 'Ń', 'Ź']

# create variables
hand = []
playerpoints = 0
enemypoints = 0

# dictionary with fields
allfields = {'A1': ' ', 'B1': ' ', 'C1': ' ', 'D1': ' ', 'E1': ' ', 'F1': ' ', 'G1': ' ', 
             'H1': ' ', 'I1': ' ', 'J1': ' ', 'K1': ' ', 'L1': ' ', 'M1': ' ', 'N1': ' ', 
             'O1': ' ', 'A2': ' ', 'B2': ' ', 'C2': ' ', 'D2': ' ', 'E2': ' ', 'F2': ' ', 
             'G2': ' ', 'H2': ' ', 'I2': ' ', 'J2': ' ', 'K2': ' ', 'L2': ' ', 'M2': ' ', 
             'N2': ' ', 'O2': ' ', 'A3': ' ', 'B3': ' ', 'C3': ' ', 'D3': ' ', 'E3': ' ', 
             'F3': ' ', 'G3': ' ', 'H3': ' ', 'I3': ' ', 'J3': ' ', 'K3': ' ', 'L3': ' ', 
             'M3': ' ', 'N3': ' ', 'O3': ' ', 'A4': ' ', 'B4': ' ', 'C4': ' ', 'D4': ' ', 
             'E4': ' ', 'F4': ' ', 'G4': ' ', 'H4': ' ', 'I4': ' ', 'J4': ' ', 'K4': ' ', 
             'L4': ' ', 'M4': ' ', 'N4': ' ', 'O4': ' ', 'A5': ' ', 'B5': ' ', 'C5': ' ', 
             'D5': ' ', 'E5': ' ', 'F5': ' ', 'G5': ' ', 'H5': ' ', 'I5': ' ', 'J5': ' ', 
             'K5': ' ', 'L5': ' ', 'M5': ' ', 'N5': ' ', 'O5': ' ', 'A6': ' ', 'B6': ' ', 
             'C6': ' ', 'D6': ' ', 'E6': ' ', 'F6': ' ', 'G6': ' ', 'H6': ' ', 'I6': ' ', 
             'J6': ' ', 'K6': ' ', 'L6': ' ', 'M6': ' ', 'N6': ' ', 'O6': ' ', 'A7': ' ', 
             'B7': ' ', 'C7': ' ', 'D7': ' ', 'E7': ' ', 'F7': ' ', 'G7': ' ', 'H7': ' ', 
             'I7': ' ', 'J7': ' ', 'K7': ' ', 'L7': ' ', 'M7': ' ', 'N7': ' ', 'O7': ' ', 
             'A8': ' ', 'B8': ' ', 'C8': ' ', 'D8': ' ', 'E8': ' ', 'F8': ' ', 'G8': ' ', 
             'H8': ' ', 'I8': ' ', 'J8': ' ', 'K8': ' ', 'L8': ' ', 'M8': ' ', 'N8': ' ', 
             'O8': ' ', 'A9': ' ', 'B9': ' ', 'C9': ' ', 'D9': ' ', 'E9': ' ', 'F9': ' ', 
             'G9': ' ', 'H9': ' ', 'I9': ' ', 'J9': ' ', 'K9': ' ', 'L9': ' ', 'M9': ' ', 
             'N9': ' ', 'O9': ' ', 'A10': ' ', 'B10': ' ', 'C10': ' ', 'D10': ' ', 'E10': ' ',
             'F10': ' ', 'G10': ' ', 'H10': ' ', 'I10': ' ', 'J10': ' ', 'K10': ' ', 'L10': ' ',
             'M10': ' ', 'N10': ' ', 'O10': ' ', 'A11': ' ', 'B11': ' ', 'C11': ' ', 'D11': ' ',
             'E11': ' ', 'F11': ' ', 'G11': ' ', 'H11': ' ', 'I11': ' ', 'J11': ' ', 'K11': ' ', 
             'L11': ' ', 'M11': ' ', 'N11': ' ', 'O11': ' ', 'A12': ' ', 'B12': ' ', 'C12': ' ', 
             'D12': ' ', 'E12': ' ', 'F12': ' ', 'G12': ' ', 'H12': ' ', 'I12': ' ', 'J12': ' ', 
             'K12': ' ', 'L12': ' ', 'M12': ' ', 'N12': ' ', 'O12': ' ', 'A13': ' ', 'B13': ' ', 
             'C13': ' ', 'D13': ' ', 'E13': ' ', 'F13': ' ', 'G13': ' ', 'H13': ' ', 'I13': ' ', 
             'J13': ' ', 'K13': ' ', 'L13': ' ', 'M13': ' ', 'N13': ' ', 'O13': ' ', 'A14': ' ', 
             'B14': ' ', 'C14': ' ', 'D14': ' ', 'E14': ' ', 'F14': ' ', 'G14': ' ', 'H14': ' ', 
             'I14': ' ', 'J14': ' ', 'K14': ' ', 'L14': ' ', 'M14': ' ', 'N14': ' ', 'O14': ' ', 
             'A15': ' ', 'B15': ' ', 'C15': ' ', 'D15': ' ', 'E15': ' ', 'F15': ' ', 'G15': ' ', 
             'H15': ' ', 'I15': ' ', 'J15': ' ', 'K15': ' ', 'L15': ' ', 'M15': ' ', 'N15': ' ', 'O15': ' '}


# dictionary with bonus values for each field:
# 0 = no bonus
# 1 = double letter
# 2 = triple letter
# 3 = double word
# 4 = triple word
allbonus = {'A1': 4, 'B1': 0, 'C1': 0, 'D1': 1, 'E1': 0, 'F1': 0, 'G1': 0, 
             'H1': 4, 'I1': 0, 'J1': 0, 'K1': 0, 'L1': 1, 'M1': 0, 'N1': 0, 
             'O1': 4, 'A2': 0, 'B2': 3, 'C2': 0, 'D2': 0, 'E2': 0, 'F2': 0, 
             'G2': 0, 'H2': 0, 'I2': 0, 'J2': 0, 'K2': 0, 'L2': 0, 'M2': 0, 
             'N2': 3, 'O2': 0, 'A3': 0, 'B3': 0, 'C3': 3, 'D3': 0, 'E3': 0, 
             'F3': 0, 'G3': 0, 'H3': 0, 'I3': 0, 'J3': 0, 'K3': 0, 'L3': 0, 
             'M3': 3, 'N3': 0, 'O3': 0, 'A4': 1, 'B4': 0, 'C4': 0, 'D4': 3, 
             'E4': 0, 'F4': 0, 'G4': 0, 'H4': 0, 'I4': 0, 'J4': 0, 'K4': 0, 
             'L4': 3, 'M4': 0, 'N4': 0, 'O4': 1, 'A5': 0, 'B5': 0, 'C5': 0, 
             'D5': 0, 'E5': 3, 'F5': 0, 'G5': 0, 'H5': 0, 'I5': 0, 'J5': 0, 
             'K5': 3, 'L5': 0, 'M5': 0, 'N5': 0, 'O5': 0, 'A6': 0, 'B6': 2, 
             'C6': 0, 'D6': 0, 'E6': 0, 'F6': 2, 'G6': 0, 'H6': 0, 'I6': 0, 
             'J6': 2, 'K6': 0, 'L6': 0, 'M6': 0, 'N6': 2, 'O6': 0, 'A7': 0, 
             'B7': 0, 'C7': 1, 'D7': 0, 'E7': 0, 'F7': 0, 'G7': 1, 'H7': 0, 
             'I7': 1, 'J7': 0, 'K7': 0, 'L7': 0, 'M7': 1, 'N7': 0, 'O7': 0, 
             'A8': 4, 'B8': 0, 'C8': 0, 'D8': 0, 'E8': 0, 'F8': 0, 'G8': 0, 
             'H8': 3, 'I8': 0, 'J8': 0, 'K8': 0, 'L8': 0, 'M8': 0, 'N8': 0, 
             'O8': 4, 'A9': 0, 'B9': 0, 'C9': 1, 'D9': 0, 'E9': 0, 'F9': 0, 
             'G9': 1, 'H9': 0, 'I9': 1, 'J9': 0, 'K9': 0, 'L9': 0, 'M9': 1, 
             'N9': 0, 'O9': 0, 'A10': 0, 'B10': 2, 'C10': 0, 'D10': 0, 'E10': 0,
             'F10': 2, 'G10': 0, 'H10': 0, 'I10': 0, 'J10': 2, 'K10': 0, 'L10': 0,
             'M10': 0, 'N10': 2, 'O10': 0, 'A11': 0, 'B11': 0, 'C11': 0, 'D11': 0,
             'E11': 3, 'F11': 0, 'G11': 0, 'H11': 0, 'I11': 0, 'J11': 0, 'K11': 3, 
             'L11': 0, 'M11': 0, 'N11': 0, 'O11': 0, 'A12': 1, 'B12': 0, 'C12': 0, 
             'D12': 3, 'E12': 0, 'F12': 0, 'G12': 0, 'H12': 0, 'I12': 0, 'J12': 0, 
             'K12': 0, 'L12': 3, 'M12': 0, 'N12': 0, 'O12': 1, 'A13': 0, 'B13': 0, 
             'C13': 3, 'D13': 0, 'E13': 0, 'F13': 0, 'G13': 0, 'H13': 0, 'I13': 0, 
             'J13': 0, 'K13': 0, 'L13': 0, 'M13': 3, 'N13': 0, 'O13': 0, 'A14': 0, 
             'B14': 3, 'C14': 0, 'D14': 0, 'E14': 0, 'F14': 0, 'G14': 0, 'H14': 0, 
             'I14': 0, 'J14': 0, 'K14': 0, 'L14': 0, 'M14': 0, 'N14': 3, 'O14': 0, 
             'A15': 4, 'B15': 0, 'C15': 0, 'D15': 0, 'E15': 0, 'F15': 0, 'G15': 0, 
             'H15': 4, 'I15': 0, 'J15': 0, 'K15': 0, 'L15': 0, 'M15': 0, 'N15': 0, 'O15': 4}
toprow = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
        'I', 'J', 'K', 'L', 'M', 'N', 'O']


# FUNCTION create scrabble board 
def create_board(hand):
    x = 0
    y = 0
    z = 0
    line = '|  '
    border = '  |  '
    topborder1 = '\n       A     B     C     D     E     F     G     H     I     J     K     L     M     N     O'
    topborder2 = '     _________________________________________________________________________________________'
    botborder1 = '    |____*|_____|_____|____-|_____|_____|_____|____*|_____|_____|_____|____-|_____|_____|____*|'
    botborder2 = '    |_____|____^|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|____^|_____|'
    botborder3 = '    |_____|_____|____^|_____|_____|_____|_____|_____|_____|_____|_____|_____|____^|_____|_____|'
    botborder4 = '    |____-|_____|_____|____^|_____|_____|_____|_____|_____|_____|_____|____^|_____|_____|____-|'
    botborder5 = '    |_____|_____|_____|_____|____^|_____|_____|_____|_____|_____|____^|_____|_____|_____|_____|'
    botborder6 = '    |_____|____+|_____|_____|_____|____+|_____|_____|_____|____+|_____|_____|_____|____+|_____|'
    botborder7 = '    |_____|_____|____-|_____|_____|_____|____-|_____|____-|_____|_____|_____|____-|_____|_____|'
    botborder8 = '    |____*|_____|_____|____-|_____|_____|_____|____^|_____|_____|_____|____-|_____|_____|____*|'
    print(topborder1)
    print(topborder2)
    for field in allfields:
        line += allfields[field] + border
        x = x + 1
        if x == 15:
            y = y + 1
            z = z + 1
            if z < 10:
                print(' ', z, line)
                line = '|  '
            else:
                print('', z, line)
                line = '|  '
            if y == 1 or y == 15:
                print(botborder1)
            elif y == 2 or y == 14:
                print(botborder2)
            elif y == 3 or y == 13:
                print (botborder3)
            elif y == 4 or y == 12:
                print(botborder4)
            elif y == 5 or y == 11:
                print (botborder5)
            elif y == 6 or y == 10:
                print(botborder6)
            elif y == 7 or y == 9:
                print (botborder7)
            else:
                print(botborder8)
            x = 0
    printhand = ''
    for x in hand:
        printhand = printhand + x + ' '
    while len(printhand) < 14:
        printhand = printhand + ' '
    print('\n    POLA PREMIOWANE:                       TWOJE LITERY:                             WYNIK:')
    print('    - PODWÓJNA LITEROWA')
    print('    + POTRÓJNA LITEROWA                   ', printhand,'                           GRACZ: ', playerpoints)
    print('    ^ PODWÓJNA SŁOWNA')
    print('    * POTRÓJNA SŁOWNA                                                             KOMPUTER: ', enemypoints)

# FUNCTION game opening
def game_opening():
    print('\n\n Witaj w Scrabble!')
    print('\n Aby ułożyć słowo:')
    print(' - wpisz słowo')
    print(' - wpisz numer pola, na którym ma się znaleźć pierwsza literka')
    print(' - wpisz kierunek tekstu - pionowo / poziomo lub ^ / >')
    print(' - wciśnij ENTER')
    print(' Koniecznie zachowaj kolejność SŁOWO POLE KIERUNEK oddzielone spacją. Wielkość liter nie ma znaczenia. ')
    print('\n Przykłady:')
    print(' DOM A10 pionowo')
    print(' samochód b2 ^')
    print('\n Aby wymienić literki wpisz "/wymiana" i po spacji wypisz literki, które chcesz wymienić')
    print('\n Po dodaniu słowa ponownie wciśnij ENTER aby dodać słowo przeciwnika')
    print('\n Aby rozpocząć grę, wpisz NORMAL lub EXPERT aby wybrać poziom trudności, a następnie wciśnij ENTER.')
    print('\n Powodzenia!')
    start = input()
    while start != 'NORMAL' and start != 'EXPERT':
        print('\n Wystąpił błąd.')
        print(' Aby rozpocząć grę, wpisz NORMAL lub EXPERT aby wybrać poziom trudności, a następnie wciśnij ENTER.')
        start = input()
    return start

# FUNCTION draw letters
def draw_letters(hand, bag):
    if len(bag) >= (7-len(hand)):
        for x in range(7-len(hand)):
            randomletter = random.choice(list(bag))
            hand.append(randomletter)
            bag.remove(randomletter)
    else:
        for x in range(len(bag)):
            randomletter = random.choice(list(bag))
            hand.append(randomletter)
            bag.remove(randomletter)
    return hand, bag
    
# FUNCTION to check validity of input
def check_validity(put_list, word, coordinate, direction):
    while(True):

        if len(put_list) != 3:
            print(' Nieprawidłowe hasło. Wpisz w formie SŁOWO POLE KIERUNEK!')
            put = input(" Spróbuj ponownie:")
            continue

        word = put_list[0]
        coordinate = put_list[1]
        direction = put_list[2]

        if re.search('[A-Z]', word) == None:
            print(re.search('[A-Z]', word), word)
            print(' Nieprawidłowe SŁOWO1!')
            put = input(" Spróbuj ponownie:")
            continue

        if len(word) > 8 or len(word) < 2:
            print(' Nieprawidłowe SŁOWO2!')
            put = input(" Spróbuj ponownie:")
            continue

        if len(coordinate) > 3 or len(coordinate) < 2:
            print(' Nieprawidłowe POLE1!')
            put = input(" Spróbuj ponownie:")
            continue

        if re.search('^[A-O]', coordinate) == None:
            print(' Nieprawidłowe POLE2!')
            put = input(" Spróbuj ponownie:")
            continue

        if int(coordinate[1:]) > 15:
            print(' Nieprawidłowe POLE3!')
            put = input(" Spróbuj ponownie:")
            continue

        if direction != 'PIONOWO' and direction != 'POZIOMO' and direction != '^' and direction != '>':
            print(' Nieprawidłowy KIERUNEK!')
            put = input(" Spróbuj ponownie:")
            continue

        if direction == 'PIONOWO' or direction == '^':
            if int(coordinate[1:]) + len(word) - 1 > 15:
                print(' Słowo nie mieści się na planszy!')
                put = input(" Spróbuj ponownie:")
                continue

        if direction == 'POZIOMO' or direction == '>':
            if alphabet.index(coordinate[0]) + len(word) - 1 > 15:
                print(' Słowo nie mieści się na planszy!')
                put = input(" Spróbuj ponownie:")
                continue

        if word not in allwords:
            print(' To słowo nie jest dopuszczalne!')
            put = input(" Spróbuj ponownie:")
            continue

        word_test3 = 0
        temp_hand = []
        used_hand = []
        temp_hand = temp_hand + hand

        for x in word:
            for y in temp_hand:
                if x == y:
                    word_test3 = word_test3 + 1
                    used_hand.append(y)
                    temp_hand.remove(y)
                    break

        if word_test3 < len(word):
            print(' Nie posiadasz tych literek!')
            put = input(" Spróbuj ponownie:")
            continue

        break
    return put_list, word, coordinate, direction

def exchange(hand, bag, put):
    put_list = []
    put_list = put.split(' ')
    put_letters = []
    for x in put_list[1]:
        put_letters.append(x)
        hand.remove(x)
        randomletter = random.choice(list(bag))
        hand.append(randomletter)
    for x in put_letters:
        bag.append(x)

while len(bag) > 0 or len(hand) > 0:
    draw_letters(hand, bag)
    create_board(hand)

    if allfields['H8'] == ' ':
        print('\n Ty zaczynasz. Pamiętaj, że pierwsze słowo musi przechodzić przez środek planszy (H8).')
        print(' Powiększ okno tak, by widzieć całą planszę.')
        put = input('\n Wpisz słowo, pole i kierunek:')
    else:
        put = input("\n Twoja kolej. Wpisz słowo, pole i kierunek:")
    if put.startswith('/wymiana'):
        put = put.upper()
        exchange(hand, bag, put)
    else:
        put = put.upper()
        put_list = put.split()
        word = ''
        coordinate = ''
        direction = ''
        coor_list = []
        used = []

        check_validity(put_list, word, coordinate, direction)

        word = put_list[0]
        coordinate = put_list[1]
        direction = put_list[2]

        # create coor_list - list of all fields used to place this word
        if direction == 'PIONOWO' or direction == '^':
            for x in range(len(word)):
                coor = coordinate[0] + str(int(coordinate[1:]) + x)
                coor_list.append(coor)

        if direction == 'POZIOMO' or direction == '>':
            for x in range(len(word)):
                coor = alphabet[alphabet.index(coordinate[0]) + x] + coordinate[1:]
                coor_list.append(coor)

        # put the word on the board and delete used letters from hand
        # if allfields['H8'] == ' ':
        #     if 'H8' in coor_list:
        for x in range(len(word)):
            allfields[coor_list[x]] = word[x]
            used.append(word[x])
            hand.remove(word[x])
            

        # count the points and add to total score
        for x in range(len(used)):
            print(x, used[x], coor_list[x])
            playerpoints = playerpoints + valuetable[used[x]]