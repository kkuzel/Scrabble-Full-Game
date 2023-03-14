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

# List containing lists representing fields on the board. Each list represents: 
    # [0] - field name (e.g. 'A1', 'G12'); 
    # [1] - field number (1-225)
    # [2] - horizontal position (1-15); 
    # [3] - vertical position (1-15); 
    # [4] - letter multiplier bonus (1 - none, 2 - double, 3 - triple);
    # [5] - word multiplier bonus (1 - none, 2 - double, 3 - triple);
    # [6] - letter value (default = ' ');
allfields = [['A1', 0, 1, 1, 1, 3, ' '], ['B1', 1, 2, 1, 1, 1, ' '], ['C1', 2, 3, 1, 1, 1, ' '], ['D1', 3, 4, 1, 2, 1, ' '], ['E1', 4, 5, 1, 1, 1, ' '], 
             ['F1', 5, 6, 1, 1, 1, ' '], ['G1', 6, 7, 1, 1, 1, ' '], ['H1', 7, 8, 1, 1, 3, ' '], ['I1', 8, 9, 1, 1, 1, ' '], ['J1', 9, 10, 1, 1, 1, ' '], 
             ['K1', 10, 11, 1, 1, 1, ' '], ['L1', 11, 12, 1, 2, 1, ' '], ['M1', 12, 13, 1, 1, 1, ' '], ['N1', 13, 14, 1, 1, 1, ' '], ['O1', 14, 15, 1, 1, 3, ' '], 
             ['A2', 15, 1, 2, 1, 1, ' '], ['B2', 16, 2, 2, 1, 2, ' '], ['C2', 17, 3, 2, 1, 1, ' '], ['D2', 18, 4, 2, 1, 1, ' '], ['E2', 19, 5, 2, 1, 1, ' '], 
             ['F2', 20, 6, 2, 1, 1, ' '], ['G2', 21, 7, 2, 1, 1, ' '], ['H2', 22, 8, 2, 1, 1, ' '], ['I2', 23, 9, 2, 1, 1, ' '], ['J2', 24, 10, 2, 1, 1, ' '], 
             ['K2', 25, 11, 2, 1, 1, ' '], ['L2', 26, 12, 2, 1, 1, ' '], ['M2', 27, 13, 2, 1, 1, ' '], ['N2', 28, 14, 2, 1, 2, ' '], ['O2', 29, 15, 2, 1, 1, ' '], 
             ['A3', 30, 1, 3, 1, 1, ' '], ['B3', 31, 2, 3, 1, 1, ' '], ['C3', 32, 3, 3, 1, 2, ' '], ['D3', 33, 4, 3, 1, 1, ' '], ['E3', 34, 5, 3, 1, 1, ' '], 
             ['F3', 35, 6, 3, 1, 1, ' '], ['G3', 36, 7, 3, 1, 1, ' '], ['H3', 37, 8, 3, 1, 1, ' '], ['I3', 38, 9, 3, 1, 1, ' '], ['J3', 39, 10, 3, 1, 1, ' '], 
             ['K3', 40, 11, 3, 1, 1, ' '], ['L3', 41, 12, 3, 1, 1, ' '], ['M3', 42, 13, 3, 1, 2, ' '], ['N3', 43, 14, 3, 1, 1, ' '], ['O3', 44, 15, 3, 1, 1, ' '], 
             ['A4', 45, 1, 4, 2, 1, ' '], ['B4', 46, 2, 4, 1, 1, ' '], ['C4', 47, 3, 4, 1, 1, ' '], ['D4', 48, 4, 4, 1, 2, ' '], ['E4', 49, 5, 4, 1, 1, ' '], 
             ['F4', 50, 6, 4, 1, 1, ' '], ['G4', 51, 7, 4, 1, 1, ' '], ['H4', 52, 8, 4, 1, 1, ' '], ['I4', 53, 9, 4, 1, 1, ' '], ['J4', 54, 10, 4, 1, 1, ' '], 
             ['K4', 55, 11, 4, 1, 1, ' '], ['L4', 56, 12, 4, 1, 2, ' '], ['M4', 57, 13, 4, 1, 1, ' '], ['N4', 58, 14, 4, 1, 1, ' '], ['O4', 59, 15, 4, 2, 1, ' '], 
             ['A5', 60, 1, 5, 1, 1, ' '], ['B5', 61, 2, 5, 1, 1, ' '], ['C5', 62, 3, 5, 1, 1, ' '], ['D5', 63, 4, 5, 1, 1, ' '], ['E5', 64, 5, 5, 1, 2, ' '], 
             ['F5', 65, 6, 5, 1, 1, ' '], ['G5', 66, 7, 5, 1, 1, ' '], ['H5', 67, 8, 5, 1, 1, ' '], ['I5', 68, 9, 5, 1, 1, ' '], ['J5', 69, 10, 5, 1, 1, ' '], 
             ['K5', 70, 11, 5, 1, 2, ' '], ['L5', 71, 12, 5, 1, 1, ' '], ['M5', 72, 13, 5, 1, 1, ' '], ['N5', 73, 14, 5, 1, 1, ' '], ['O5', 74, 15, 5, 1, 1, ' '], 
             ['A6', 75, 1, 6, 1, 1, ' '], ['B6', 76, 2, 6, 3, 1, ' '], ['C6', 77, 3, 6, 1, 1, ' '], ['D6', 78, 4, 6, 1, 1, ' '], ['E6', 79, 5, 6, 1, 1, ' '], 
             ['F6', 80, 6, 6, 3, 1, ' '], ['G6', 81, 7, 6, 1, 1, ' '], ['H6', 82, 8, 6, 1, 1, ' '], ['I6', 83, 9, 6, 1, 1, ' '], ['J6', 84, 10, 6, 3, 1, ' '], 
             ['K6', 85, 11, 6, 1, 1, ' '], ['L6', 86, 12, 6, 1, 1, ' '], ['M6', 87, 13, 6, 1, 1, ' '], ['N6', 88, 14, 6, 3, 1, ' '], ['O6', 89, 15, 6, 1, 1, ' '], 
             ['A7', 90, 1, 7, 1, 1, ' '], ['B7', 91, 2, 7, 1, 1, ' '], ['C7', 92, 3, 7, 2, 1, ' '], ['D7', 93, 4, 7, 1, 1, ' '], ['E7', 94, 5, 7, 1, 1, ' '], 
             ['F7', 95, 6, 7, 1, 1, ' '], ['G7', 96, 7, 7, 2, 1, ' '], ['H7', 97, 8, 7, 1, 1, ' '], ['I7', 98, 9, 7, 2, 1, ' '], ['J7', 99, 10, 7, 1, 1, ' '], 
             ['K7', 100, 11, 7, 1, 1, ' '], ['L7', 101, 12, 7, 1, 1, ' '], ['M7', 102, 13, 7, 2, 1, ' '], ['N7', 103, 14, 7, 1, 1, ' '], ['O7', 104, 15, 7, 1, 1, ' '], 
             ['A8', 105, 1, 8, 1, 3, ' '], ['B8', 106, 2, 8, 1, 1, ' '], ['C8', 107, 3, 8, 1, 1, ' '], ['D8', 108, 4, 8, 1, 1, ' '], ['E8', 109, 5, 8, 1, 1, ' '], 
             ['F8', 110, 6, 8, 1, 1, ' '], ['G8', 111, 7, 8, 1, 1, 'D'], ['H8', 112, 8, 8, 1, 2, 'O'], ['I8', 113, 9, 8, 1, 1, 'M'], ['J8', 114, 10, 8, 1, 1, ' '], 
             ['K8', 115, 11, 8, 1, 1, ' '], ['L8', 116, 12, 8, 1, 1, ' '], ['M8', 117, 13, 8, 1, 1, ' '], ['N8', 118, 14, 8, 1, 1, ' '], ['O8', 119, 15, 8, 1, 3, ' '], 
             ['A9', 120, 1, 9, 1, 1, ' '], ['B9', 121, 2, 9, 1, 1, ' '], ['C9', 122, 3, 9, 2, 1, ' '], ['D9', 123, 4, 9, 1, 1, ' '], ['E9', 124, 5, 9, 1, 1, ' '], 
             ['F9', 125, 6, 9, 1, 1, ' '], ['G9', 126, 7, 9, 2, 1, ' '], ['H9', 127, 8, 9, 1, 1, ' '], ['I9', 128, 9, 9, 2, 1, ' '], ['J9', 129, 10, 9, 1, 1, ' '], 
             ['K9', 130, 11, 9, 1, 1, ' '], ['L9', 131, 12, 9, 1, 1, ' '], ['M9', 132, 13, 9, 2, 1, ' '], ['N9', 133, 14, 9, 1, 1, ' '], ['O9', 134, 15, 9, 1, 1, ' '], 
             ['A10', 135, 1, 10, 1, 1, ' '], ['B10', 136, 2, 10, 3, 1, ' '], ['C10', 137, 3, 10, 1, 1, ' '], ['D10', 138, 4, 10, 1, 1, ' '], ['E10', 139, 5, 10, 1, 1, ' '], 
             ['F10', 140, 6, 10, 3, 1, ' '], ['G10', 141, 7, 10, 1, 1, ' '], ['H10', 142, 8, 10, 1, 1, ' '], ['I10', 143, 9, 10, 1, 1, ' '], ['J10', 144, 10, 10, 3, 1, ' '], 
             ['K10', 145, 11, 10, 1, 1, ' '], ['L10', 146, 12, 10, 1, 1, ' '], ['M10', 147, 13, 10, 1, 1, ' '], ['N10', 148, 14, 10, 3, 1, ' '], ['O10', 149, 15, 10, 1, 1, ' '], 
             ['A11', 150, 1, 11, 1, 1, ' '], ['B11', 151, 2, 11, 1, 1, ' '], ['C11', 152, 3, 11, 1, 1, ' '], ['D11', 153, 4, 11, 1, 1, ' '], ['E11', 154, 5, 11, 1, 2, ' '], 
             ['F11', 155, 6, 11, 1, 1, ' '], ['G11', 156, 7, 11, 1, 1, ' '], ['H11', 157, 8, 11, 1, 1, ' '], ['I11', 158, 9, 11, 1, 1, ' '], ['J11', 159, 10, 11, 1, 1, ' '], 
             ['K11', 160, 11, 11, 1, 2, ' '], ['L11', 161, 12, 11, 1, 1, ' '], ['M11', 162, 13, 11, 1, 1, ' '], ['N11', 163, 14, 11, 1, 1, ' '], ['O11', 164, 15, 11, 1, 1, ' '], 
             ['A12', 165, 1, 12, 2, 1, ' '], ['B12', 166, 2, 12, 1, 1, ' '], ['C12', 167, 3, 12, 1, 1, ' '], ['D12', 168, 4, 12, 1, 2, ' '], ['E12', 169, 5, 12, 1, 1, ' '], 
             ['F12', 170, 6, 12, 1, 1, ' '], ['G12', 171, 7, 12, 1, 1, ' '], ['H12', 172, 8, 12, 1, 1, ' '], ['I12', 173, 9, 12, 1, 1, ' '], ['J12', 174, 10, 12, 1, 1, ' '], 
             ['K12', 175, 11, 12, 1, 1, ' '], ['L12', 176, 12, 12, 1, 2, ' '], ['M12', 177, 13, 12, 1, 1, ' '], ['N12', 178, 14, 12, 1, 1, ' '], ['O12', 179, 15, 12, 2, 1, ' '], 
             ['A13', 180, 1, 13, 1, 1, ' '], ['B13', 181, 2, 13, 1, 1, ' '], ['C13', 182, 3, 13, 1, 2, ' '], ['D13', 183, 4, 13, 1, 1, ' '], ['E13', 184, 5, 13, 1, 1, ' '], 
             ['F13', 185, 6, 13, 1, 1, ' '], ['G13', 186, 7, 13, 1, 1, ' '], ['H13', 187, 8, 13, 1, 1, ' '], ['I13', 188, 9, 13, 1, 1, ' '], ['J13', 189, 10, 13, 1, 1, ' '], 
             ['K13', 190, 11, 13, 1, 1, ' '], ['L13', 191, 12, 13, 1, 1, ' '], ['M13', 192, 13, 13, 1, 2, ' '], ['N13', 193, 14, 13, 1, 1, ' '], ['O13', 194, 15, 13, 1, 1, ' '], 
             ['A14', 195, 1, 14, 1, 1, ' '], ['B14', 196, 2, 14, 1, 2, ' '], ['C14', 197, 3, 14, 1, 1, ' '], ['D14', 198, 4, 14, 1, 1, ' '], ['E14', 199, 5, 14, 1, 1, ' '], 
             ['F14', 200, 6, 14, 1, 1, ' '], ['G14', 201, 7, 14, 1, 1, ' '], ['H14', 202, 8, 14, 1, 1, ' '], ['I14', 203, 9, 14, 1, 1, ' '], ['J14', 204, 10, 14, 1, 1, ' '], 
             ['K14', 205, 11, 14, 1, 1, ' '], ['L14', 206, 12, 14, 1, 1, ' '], ['M14', 207, 13, 14, 1, 1, ' '], ['N14', 208, 14, 14, 1, 2, ' '], ['O14', 209, 15, 14, 1, 1, ' '], 
             ['A15', 210, 1, 15, 1, 3, ' '], ['B15', 211, 2, 15, 1, 1, ' '], ['C15', 212, 3, 15, 1, 1, ' '], ['D15', 213, 4, 15, 1, 1, ' '], ['E15', 214, 5, 15, 1, 1, ' '], 
             ['F15', 215, 6, 15, 1, 1, ' '], ['G15', 216, 7, 15, 1, 1, ' '], ['H15', 217, 8, 15, 1, 3, ' '], ['I15', 218, 9, 15, 1, 1, ' '], ['J15', 219, 10, 15, 1, 1, ' '], 
             ['K15', 220, 11, 15, 1, 1, ' '], ['L15', 221, 12, 15, 1, 1, ' '], ['M15', 222, 13, 15, 1, 1, ' '], ['N15', 223, 14, 15, 1, 1, ' '], ['O15', 224, 15, 15, 1, 3, ' ']]

# create variables
hand = []
playerscore = 0
pcscore = 0
toprow = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
        'I', 'J', 'K', 'L', 'M', 'N', 'O']

# FUNCTION create scrabble board 
def create_board(hand, pcscore):
    topborder = '\n       A     B     C     D     E     F     G     H     I     J     K     L     M     N     O\n     _________________________________________________________________________________________'
    borders = ['    |____*|_____|_____|____-|_____|_____|_____|____*|_____|_____|_____|____-|_____|_____|____*|', 
               '    |_____|____^|_____|_____|_____|____+|_____|_____|_____|____+|_____|_____|_____|____^|_____|', 
               '    |_____|_____|____^|_____|_____|_____|____-|_____|____-|_____|_____|_____|____^|_____|_____|',
               '    |____-|_____|_____|____^|_____|_____|_____|____-|_____|_____|_____|____^|_____|_____|____-|', 
               '    |_____|_____|_____|_____|____^|_____|_____|_____|_____|_____|____^|_____|_____|_____|_____|', 
               '    |_____|____+|_____|_____|_____|____+|_____|_____|_____|____+|_____|_____|_____|____+|_____|', 
               '    |_____|_____|____-|_____|_____|_____|____-|_____|____-|_____|_____|_____|____-|_____|_____|', 
               '    |____*|_____|_____|____-|_____|_____|_____|____^|_____|_____|_____|____-|_____|_____|____*|', 
               '    |_____|_____|____-|_____|_____|_____|____-|_____|____-|_____|_____|_____|____-|_____|_____|', 
               '    |_____|____+|_____|_____|_____|____+|_____|_____|_____|____+|_____|_____|_____|____+|_____|', 
               '    |_____|_____|_____|_____|____^|_____|_____|_____|_____|_____|____^|_____|_____|_____|_____|', 
               '    |____-|_____|_____|____^|_____|_____|_____|____-|_____|_____|_____|____^|_____|_____|____-|', 
               '    |_____|_____|____^|_____|_____|_____|____-|_____|____-|_____|_____|_____|____^|_____|_____|',
               '    |_____|____^|_____|_____|_____|____+|_____|_____|_____|____+|_____|_____|_____|____^|_____|', 
               '    |____*|_____|_____|____-|_____|_____|_____|____*|_____|_____|_____|____-|_____|_____|____*|']
    print(topborder)
    border = '  |  '
    line = '|  '
    y = 0
    z = 0
    for x in range(225):
        line += allfields[x][6] + border
        y = y + 1
        if y == 15:
            z = z + 1
            if z < 10:
                print(' ', z, line)
            else:
                print('', z, line)
            print(borders[z-1])
            line = '|  '
            y = 0
    strhand = ''
    for x in hand:
        strhand = strhand + x + ' '
    while len(strhand) < 14:
        strhand = strhand + ' '
    print('\n    POLA PREMIOWANE:                       TWOJE LITERY:                             WYNIK:')
    print('    - PODWÓJNA LITEROWA')
    print('    + POTRÓJNA LITEROWA                   ', strhand,'                           GRACZ: ', playerscore)
    print('    ^ PODWÓJNA SŁOWNA')
    print('    * POTRÓJNA SŁOWNA                                                             KOMPUTER: ', pcscore)

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
# FUNCTION that creates a list of all words that are possible to create, given hand and content of board, then it picks word with highest score and put it on board
def opponent_move(hand, pcscore):
    allpossible = []
    for x in range(len(allfields)):
        if allfields[x][6] != ' ':
            if (allfields[x-1][6] != ' ' or allfields[x+1][6] != ' ') and (allfields[x-15][6] != ' ' or allfields[x+15][6] != ' '):
                continue
            elif allfields[x-1][6] != ' ' or allfields[x+1][6] != ' ':
                up = 0
                down = 0
                for y in range(1, allfields[x][3]):
                    if allfields[x-(y*15)][3] > 1:
                        if allfields[x-(y*15)-1][6] == ' ' and allfields[x-(y*15)+1][6] == ' ' and allfields[x-(y*15)-15][6] == ' ':
                            up = up + 1
                        else:
                            break
                    else:
                        if allfields[x-(y*15)-1][6] == ' ' and allfields[x-(y*15)+1][6] == ' ':
                            up = up + 1
                        else:
                            break
                for y in range(1, 16-allfields[x][3]):
                    if allfields[x+(y*15)][3] < 15:
                        if allfields[x+(y*15)-1][6] == ' ' and allfields[x+(y*15)+1][6] == ' ' and allfields[x+(y*15)+15][6] == ' ':
                            down = down + 1
                        else:
                            break
                    else:
                        if allfields[x+(y*15)-1][6] == ' ' and allfields[x+(y*15)+1][6] == ' ':
                            down = down + 1
                        else:
                            break
                for checkword in allwords:
                    check = 0
                    tempscore = 0
                    possible = []
                    temphand = []
                    usedhand = []
                    temphand = temphand + hand
                    temphand.append(allfields[x][6])
                    if allfields[x][6] in checkword:
                        if ((up+down+1) >= len(checkword)) and (checkword.index(allfields[x][6]) <= up) and ((len(checkword)-checkword.index(allfields[x][6])-1) <= down):
                            for y in checkword:
                                if y in temphand:
                                    check = check + 1
                                    temphand.remove(y)
                                    usedhand.append(y)
                            if check == len(checkword):
                                possible.append(tempscore)
                                possible.append(checkword)
                                possible.append(allfields[x-(15*checkword.index(allfields[x][6]))][1])
                                possible.append('^')
                                multiplier = 1
                                for y in range(len(usedhand)):
                                    if allfields[possible[2]+y*15][6] == ' ':
                                        tempscore = tempscore + valuetable[usedhand[y]] * allfields[possible[2]+y*15][4]
                                        multiplier = multiplier * allfields[possible[2]+y*15][5]
                                    else:
                                        tempscore = tempscore + valuetable[usedhand[y]]
                                tempscore = tempscore * multiplier
                                possible[0] = tempscore
                                allpossible.append(possible)
                                

                
            elif allfields[x-15][6] != ' ' or allfields[x+15][6] != ' ':
                left = 0
                right = 0
                for y in range(1, allfields[x][2]):
                    if allfields[x-y][2] > 1:
                        if allfields[x-y-15][6] == ' ' and allfields[x-y+15][6] == ' ' and allfields[x-y-1][6] == ' ':
                            left = left + 1
                        else:
                            break
                    else:
                        if allfields[x-y-15][6] == ' ' and allfields[x-y+15][6] == ' ':
                            left = left + 1
                        else:
                            break
                for y in range(1, 16-allfields[x][2]):
                    if allfields[x+y][2] < 15:
                        if allfields[x+y-15][6] == ' ' and allfields[x+y+15][6] == ' ' and allfields[x+y+1][6] == ' ':
                            right = right + 1
                        else:
                            break
                    else:
                        if allfields[x+y-15][6] == ' ' and allfields[x+y+15][6] == ' ':
                            right = right + 1
                        else:
                            break
                for checkword in allwords:
                    check = 0
                    tempscore = 0
                    possible = []
                    temphand = []
                    usedhand = []
                    temphand = temphand + hand
                    temphand.append(allfields[x][6])
                    if allfields[x][6] in checkword:
                        if ((left+right+1) >= len(checkword)) and (checkword.index(allfields[x][6]) <= left) and ((len(checkword)-checkword.index(allfields[x][6])-1) <= right):
                            for y in checkword:
                                if y in temphand:
                                    check = check + 1
                                    temphand.remove(y)
                                    usedhand.append(y)
                            if check == len(checkword):
                                possible.append(tempscore)
                                possible.append(checkword)
                                possible.append(allfields[x-(checkword.index(allfields[x][6]))][1])
                                possible.append('>')
                                multiplier = 1
                                for y in range(len(usedhand)):
                                    if allfields[possible[2]+y][6] == ' ':
                                        tempscore = tempscore + valuetable[usedhand[y]] * allfields[possible[2]+y][4]
                                        multiplier = multiplier * allfields[possible[2]+y][5]
                                    else:
                                        tempscore = tempscore + valuetable[usedhand[y]]
                                tempscore = tempscore * multiplier
                                possible[0] = tempscore
                                allpossible.append(possible)

    allpossible.sort(reverse=True)
    print(allpossible[0:5])
    if allpossible[0][3] == '^':
        drophand = []
        for x in range(len(allpossible[0][1])):
            allfields[allpossible[0][2]+(x*15)][6] = allpossible[0][1][x]
            drophand.append(allpossible[0][1][x])
    elif allpossible[0][3] == '>':
        drophand = []
        for x in range(len(allpossible[0][1])):
            allfields[allpossible[0][2]+x][6] = allpossible[0][1][x]
            drophand.append(allpossible[0][1][x])
    for x in drophand:
        if x in hand:
            hand.remove(x)
    pcscore = pcscore + allpossible[0][0]
    print(pcscore, allpossible[0][0])
    return pcscore

# LOOP that plays the game (repeat drawing letters and putting words on board until the letter bag is empty)
while len(bag) > 0 or len(hand) > 0:
    draw_letters(hand, bag)
    create_board(hand, pcscore)
    opponent_move(hand, pcscore)
    print(pcscore)




