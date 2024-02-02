from random import randint
from random import choice
import copy
import time
import os


def Menu():
    status = 0
    n = 0
    print('Welcome !!\n')
    while status == 0:
        n = int(input('Enter whether Single Player/Double Player (1/2): '))
        if n == 1:
            status = 1
        elif n == 2:
            status = 1
        else:
            print("Please enter valid option !!")
    print("\nThis is the Environment we are going to play....")
    print("\n [1] | [2] | [3] \n-----|-----|-----\n [4] | [5] | [6] \n-----|-----|-----\n [7] | [8] | [9] \n")
    if n == 1:  # singlePlayer()
        trials = 1
        print("Welcome to Single Player Mode...")
        player = input("Enter your Name {X}:  ")
        while trials != 0:
            singlePlayer(player)
            again = input("\nIf you want to play again, enter 'y'......\n")
            if again != 'y':
                trials = 0
                clean()
    else:  # doublePlayer
        trials = 1
        print("Welcome to Double Player Mode...")
        player1 = input("Enter your Name Player1 {X}:  ")
        player2 = input("Enter your Name Player2 {O}:  ")
        while trials != 0:
            doublePlayer(player1, player2)
            again = input("\nIf you want to play again, enter 'y'......\n")
            if again != 'y':
                trials = 0
                clean()
    print('Thank you !!')


def getInput(GameMemory, used, player, XorO):
    n = int(input("Enter the space you want to Input {0}: ".format(player)))
    test = 0
    while test != 1:
        if n in used or n < 1 or n > 9:
            print("Enter the space value which are available {0}....\n".format(player))
            n = int(input("Enter the space you want to Input: "))
        else:
            test = 1
    GameMemory[n - 1] = XorO
    used.append(n)
    return GameMemory, used


def checkFinish(GameMemory):
    # Horizontal
    if GameMemory[0] == GameMemory[1] and GameMemory[1] == GameMemory[2]:
        GameMemory[3] = ' - '
        GameMemory[4] = ' - '
        GameMemory[5] = ' - '
        GameMemory[6] = ' - '
        GameMemory[7] = ' - '
        GameMemory[8] = ' - '
        return GameMemory, 1
    elif GameMemory[3] == GameMemory[4] and GameMemory[4] == GameMemory[5]:
        GameMemory[0] = ' - '
        GameMemory[1] = ' - '
        GameMemory[2] = ' - '
        GameMemory[6] = ' - '
        GameMemory[7] = ' - '
        GameMemory[8] = ' - '
        return GameMemory, 1
    elif GameMemory[6] == GameMemory[7] and GameMemory[7] == GameMemory[8]:
        GameMemory[0] = ' - '
        GameMemory[1] = ' - '
        GameMemory[2] = ' - '
        GameMemory[3] = ' - '
        GameMemory[4] = ' - '
        GameMemory[5] = ' - '
        return GameMemory, 1
    # Vertical
    elif GameMemory[0] == GameMemory[3] and GameMemory[3] == GameMemory[6]:
        GameMemory[1] = ' - '
        GameMemory[2] = ' - '
        GameMemory[4] = ' - '
        GameMemory[5] = ' - '
        GameMemory[7] = ' - '
        GameMemory[8] = ' - '
        return GameMemory, 1
    elif GameMemory[1] == GameMemory[4] and GameMemory[4] == GameMemory[7]:
        GameMemory[0] = ' - '
        GameMemory[2] = ' - '
        GameMemory[3] = ' - '
        GameMemory[5] = ' - '
        GameMemory[6] = ' - '
        GameMemory[8] = ' - '
        return GameMemory, 1
    elif GameMemory[2] == GameMemory[5] and GameMemory[5] == GameMemory[8]:
        GameMemory[0] = ' - '
        GameMemory[1] = ' - '
        GameMemory[3] = ' - '
        GameMemory[4] = ' - '
        GameMemory[6] = ' - '
        GameMemory[7] = ' - '
        return GameMemory, 1
    # Diagonal
    elif GameMemory[0] == GameMemory[4] and GameMemory[4] == GameMemory[8]:
        GameMemory[1] = ' - '
        GameMemory[2] = ' - '
        GameMemory[3] = ' - '
        GameMemory[5] = ' - '
        GameMemory[6] = ' - '
        GameMemory[7] = ' - '
        return GameMemory, 1
    elif GameMemory[2] == GameMemory[4] and GameMemory[4] == GameMemory[6]:
        GameMemory[0] = ' - '
        GameMemory[1] = ' - '
        GameMemory[3] = ' - '
        GameMemory[5] = ' - '
        GameMemory[7] = ' - '
        GameMemory[8] = ' - '
        return GameMemory, 1
    else:
        return GameMemory, 0
    # return GameMemory


def singlePlayer(player):
    GameMemory = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]']
    used = []
    iterations_left = 9
    print("Do you want to Start 1st {0}?? (y/n):  ".format(player))
    while True:
        YorN = input()
        if YorN == 'y':
            start = 1
            break
        elif YorN == 'n':
            start = 2
            break
        else:
            print("Please enter valid option {0}!!".format(player))
    while iterations_left != 0:
        print("\n {0} | {1} | {2} \n-----|-----|-----\n {3} | {4} | {5} \n-----|-----|-----\n {6} | {7} | {8} \n"
              .format(GameMemory[0],
                      GameMemory[1], GameMemory[2],
                      GameMemory[3], GameMemory[4],
                      GameMemory[5], GameMemory[6],
                      GameMemory[7], GameMemory[8]))
        if start % 2 != 0:  # player
            print("{0}'s turn-".format(player))
            GameMemory, used = getInput(GameMemory, used, player, ' X ')
            GameMemory, check = checkFinish(GameMemory)
            if check == 1:
                print("\n{0} has won the game!! ".format(player))
                print("\U0001F644" * 5)
                print(
                    "\n {0} | {1} | {2} \n-----|-----|-----\n {3} | {4} | {5} \n-----|-----|-----\n {6} | {7} | {8} \n"
                    .format(GameMemory[0],
                            GameMemory[1], GameMemory[2],
                            GameMemory[3], GameMemory[4],
                            GameMemory[5], GameMemory[6],
                            GameMemory[7], GameMemory[8]))
                break
            else:
                pass
        else:  # computer
            TM = randint(3, 6)
            print("Computer is thinking", end='')
            for i in range(TM):
                print('.', end='')
                time.sleep(0.5)
            print('\n\n')
            rand = computerInput(GameMemory, iterations_left, used)
            c = ' O '
            GameMemory[rand - 1] = c
            used.append(rand)
            GameMemory, check = checkFinish(GameMemory)
            print("Computer chooses:", rand)
            if check == 1:
                print("\nComputer has won the game!! ")
                print("\U0001F923" * 5)
                print(
                    "\n {0} | {1} | {2} \n-----|-----|-----\n {3} | {4} | {5} \n-----|-----|-----\n {6} | {7} | {8} \n"
                    .format(GameMemory[0],
                            GameMemory[1], GameMemory[2],
                            GameMemory[3], GameMemory[4],
                            GameMemory[5], GameMemory[6],
                            GameMemory[7], GameMemory[8]))
                break
            else:
                pass
        iterations_left -= 1
        start += 1
        if iterations_left == 0:
            print("\nIt is a Tie!! ")
            print("\U0001F610" * 5)
            print("\n {0} | {1} | {2} \n-----|-----|-----\n {3} | {4} | {5} \n-----|-----|-----\n {6} | {7} | {8} \n"
                  .format(GameMemory[0],
                          GameMemory[1], GameMemory[2],
                          GameMemory[3], GameMemory[4],
                          GameMemory[5], GameMemory[6],
                          GameMemory[7], GameMemory[8]))


def computerInput(GameMemory, iterations_left, used):
    allPositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    not_used = []
    for i in allPositions:
        if i not in used:
            not_used.append(i)
        else:
            pass
    if iterations_left == 9:  # 1st priority
        rand = randint(1, 9)
        return rand  # returns the position the computer has to input
    else:
        assign = preventPlayer(GameMemory, used, ' O ')
        if assign != 0:  # if game can be won
            return assign
        else:  # if prevention is required
            prevent = preventPlayer(GameMemory, used, ' X ')
            if prevent != 0:
                return prevent
            else:
                totalPossiblePositionsO, totalPossiblePositionsX = findPosition(GameMemory)
                final_pos = []
                for i in totalPossiblePositionsO:
                    if i in totalPossiblePositionsX:
                        final_pos.append(i)
                    else:
                        pass
                if len(final_pos) != 0:
                    rand = choice(final_pos)
                    return rand
                else:
                    rand = choice(not_used)
                    return rand


def findPosition(GameMemory):
    totalPossiblePathsX = []
    temp_totalPossiblePathsX = []
    totalPossiblePathsO = []
    temp_totalPossiblePathsO = []
    for i in GameMemory:
        if i == ' X ':
            temp_paths = predictPossibleCompletion(GameMemory, ' X ')
            for j in temp_paths:
                temp_totalPossiblePathsX.append(j)
        elif i == ' O ':
            temp_paths = predictPossibleCompletion(GameMemory, ' O ')
            for j in temp_paths:
                temp_totalPossiblePathsO.append(j)
        else:
            pass
    for i in temp_totalPossiblePathsX:
        if i not in totalPossiblePathsX:
            totalPossiblePathsX.append(i)
        else:
            pass
    for i in temp_totalPossiblePathsO:
        if i not in totalPossiblePathsO:
            totalPossiblePathsO.append(i)
        else:
            pass

    totalPossiblePositionsX = []
    temp_totalPossiblePositionsX = []
    for i in totalPossiblePathsX:
        for j in i:
            temp_totalPossiblePositionsX.append(j)
    for i in temp_totalPossiblePositionsX:
        if i not in totalPossiblePositionsX:
            totalPossiblePositionsX.append(i)
        else:
            pass

    totalPossiblePositionsO = []
    temp_totalPossiblePositionsO = []
    for i in totalPossiblePathsO:
        for j in i:
            temp_totalPossiblePositionsO.append(j)
    for i in temp_totalPossiblePositionsO:
        if i not in totalPossiblePositionsO:
            totalPossiblePositionsO.append(i)
        else:
            pass
    finalO = []
    finalX = []
    for i in totalPossiblePositionsO:
        if i != ' O ':
            finalO.append(i)
    for i in totalPossiblePositionsX:
        if i != ' X ':
            finalX.append(i)
    return finalO, finalX


def preventPlayer(GameMemory, used, type):
    not_used = []
    checks = []
    for i in range(1, 10):
        if i not in used:
            not_used.append(i)
    for i in not_used:
        temp_GameMemory = copy.deepcopy(GameMemory)
        temp_GameMemory[i - 1] = type
        predict = predictPrevention(temp_GameMemory)
        if predict == 1:
            checks.append(i)
        else:
            pass
    if len(checks) != 0:
        rand = choice(checks)
        return rand
    else:
        return 0


def predictPrevention(temp_GameMemory):
    # Horizontal
    if temp_GameMemory[0] == temp_GameMemory[1] and temp_GameMemory[1] == temp_GameMemory[2]:
        return 1
    elif temp_GameMemory[3] == temp_GameMemory[4] and temp_GameMemory[4] == temp_GameMemory[5]:
        return 1
    elif temp_GameMemory[6] == temp_GameMemory[7] and temp_GameMemory[7] == temp_GameMemory[8]:
        return 1
    # Vertical
    elif temp_GameMemory[0] == temp_GameMemory[3] and temp_GameMemory[3] == temp_GameMemory[6]:
        return 1
    elif temp_GameMemory[1] == temp_GameMemory[4] and temp_GameMemory[4] == temp_GameMemory[7]:
        return 1
    elif temp_GameMemory[2] == temp_GameMemory[5] and temp_GameMemory[5] == temp_GameMemory[8]:
        return 1
    # Diagonal
    elif temp_GameMemory[0] == temp_GameMemory[4] and temp_GameMemory[4] == temp_GameMemory[8]:
        return 1
    elif temp_GameMemory[2] == temp_GameMemory[4] and temp_GameMemory[4] == temp_GameMemory[6]:
        return 1
    else:
        return 0


def predictPossibleCompletion(GameMemory, element):  # element is ' X ' or ' O '
    if element == ' X ':
        non_element = ' O '
    else:
        non_element = ' X '
    result = []
    # Horizontal
    if ((GameMemory[0] == element
         and GameMemory[1] != element and GameMemory[1] != non_element
         and GameMemory[2] != element and GameMemory[2] != non_element)
            or (GameMemory[1] == element
                and GameMemory[0] != element and GameMemory[0] != non_element
                and GameMemory[2] != element and GameMemory[2] != non_element)
            or (GameMemory[2] == element
                and GameMemory[0] != element and GameMemory[0] != non_element
                and GameMemory[1] != element and GameMemory[1] != non_element)):
        l = [1, 2, 3]
        result.append(l)
    if ((GameMemory[3] == element
         and GameMemory[4] != element and GameMemory[4] != non_element
         and GameMemory[5] != element and GameMemory[5] != non_element)
            or (GameMemory[4] == element
                and GameMemory[3] != element and GameMemory[3] != non_element
                and GameMemory[5] != element and GameMemory[5] != non_element)
            or (GameMemory[5] == element
                and GameMemory[3] != element and GameMemory[3] != non_element
                and GameMemory[4] != element and GameMemory[4] != non_element)):
        l = [4, 5, 6]
        result.append(l)
    if ((GameMemory[6] == element
         and GameMemory[7] != element and GameMemory[7] != non_element
         and GameMemory[8] != element and GameMemory[8] != non_element)
            or (GameMemory[7] == element
                and GameMemory[6] != element and GameMemory[6] != non_element
                and GameMemory[8] != element and GameMemory[8] != non_element)
            or (GameMemory[8] == element
                and GameMemory[6] != element and GameMemory[6] != non_element
                and GameMemory[7] != element and GameMemory[7] != non_element)):
        l = [7, 8, 9]
        result.append(l)
    # Vertical
    if ((GameMemory[0] == element
         and GameMemory[3] != element and GameMemory[3] != non_element
         and GameMemory[6] != element and GameMemory[6] != non_element)
            or (GameMemory[3] == element
                and GameMemory[0] != element and GameMemory[0] != non_element
                and GameMemory[6] != element and GameMemory[6] != non_element)
            or (GameMemory[6] == element
                and GameMemory[0] != element and GameMemory[0] != non_element
                and GameMemory[3] != element and GameMemory[3] != non_element)):
        l = [1, 4, 7]
        result.append(l)
    if ((GameMemory[1] == element
         and GameMemory[4] != element and GameMemory[4] != non_element
         and GameMemory[7] != element and GameMemory[7] != non_element)
            or (GameMemory[4] == element
                and GameMemory[1] != element and GameMemory[1] != non_element
                and GameMemory[7] != element and GameMemory[7] != non_element)
            or (GameMemory[7] == element
                and GameMemory[1] != element and GameMemory[1] != non_element
                and GameMemory[4] != element and GameMemory[4] != non_element)):
        l = [2, 5, 8]
        result.append(l)
    if ((GameMemory[2] == element
         and GameMemory[5] != element and GameMemory[5] != non_element
         and GameMemory[8] != element and GameMemory[8] != non_element)
            or (GameMemory[5] == element
                and GameMemory[2] != element and GameMemory[2] != non_element
                and GameMemory[8] != element and GameMemory[8] != non_element)
            or (GameMemory[8] == element
                and GameMemory[2] != element and GameMemory[2] != non_element
                and GameMemory[5] != element and GameMemory[5] != non_element)):
        l = [3, 6, 9]
        result.append(l)
    # Diagonal
    if ((GameMemory[0] == element
         and GameMemory[4] != element and GameMemory[4] != non_element
         and GameMemory[8] != element and GameMemory[8] != non_element)
            or (GameMemory[4] == element
                and GameMemory[0] != element and GameMemory[0] != non_element
                and GameMemory[8] != element and GameMemory[8] != non_element)
            or (GameMemory[8] == element
                and GameMemory[0] != element and GameMemory[0] != non_element
                and GameMemory[4] != element and GameMemory[4] != non_element)):
        l = [1, 5, 9]
        result.append(l)
    if ((GameMemory[2] == element
         and GameMemory[4] != element and GameMemory[4] != non_element
         and GameMemory[6] != element and GameMemory[6] != non_element)
            or (GameMemory[4] == element
                and GameMemory[2] != element and GameMemory[2] != non_element
                and GameMemory[6] != element and GameMemory[6] != non_element)
            or (GameMemory[6] == element
                and GameMemory[2] != element and GameMemory[2] != non_element
                and GameMemory[4] != element and GameMemory[4] != non_element)):
        l = [3, 5, 7]
        result.append(l)
    return result


def doublePlayer(player1, player2):
    GameMemory = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]']
    used = []
    iterations_left = 9
    print("Do you want to Start 1st {0}?? (y/n):  ".format(player1))
    while True:
        YorN = input()
        if YorN == 'y':
            start = 1
            break
        elif YorN == 'n':
            start = 2
            break
        else:
            print("Please enter valid option {0}!!".format(player1))
    while iterations_left != 0:
        print("\n {0} | {1} | {2} \n-----|-----|-----\n {3} | {4} | {5} \n-----|-----|-----\n {6} | {7} | {8} \n"
              .format(GameMemory[0],
                      GameMemory[1], GameMemory[2],
                      GameMemory[3], GameMemory[4],
                      GameMemory[5], GameMemory[6],
                      GameMemory[7], GameMemory[8]))
        if start % 2 != 0:  # player1
            print("{0}'s turn-".format(player1))
            GameMemory, used = getInput(GameMemory, used, player1, ' X ')
            GameMemory, check = checkFinish(GameMemory)
            if check == 1:
                print("\n{0} has won the game!! ".format(player1))
                print(
                    "\n {0} | {1} | {2} \n-----|-----|-----\n {3} | {4} | {5} \n-----|-----|-----\n {6} | {7} | {8} \n"
                    .format(GameMemory[0],
                            GameMemory[1], GameMemory[2],
                            GameMemory[3], GameMemory[4],
                            GameMemory[5], GameMemory[6],
                            GameMemory[7], GameMemory[8]))
                break
            else:
                pass
        else:  # player2
            print("{0}'s turn-".format(player2))
            GameMemory, used = getInput(GameMemory, used, player2, ' O ')
            GameMemory, check = checkFinish(GameMemory)
            if check == 1:
                print("\n{0} has won the game!! ".format(player2))
                print(
                    "\n {0} | {1} | {2} \n-----|-----|-----\n {3} | {4} | {5} \n-----|-----|-----\n {6} | {7} | {8} \n"
                    .format(GameMemory[0],
                            GameMemory[1], GameMemory[2],
                            GameMemory[3], GameMemory[4],
                            GameMemory[5], GameMemory[6],
                            GameMemory[7], GameMemory[8]))
                break
            else:
                pass
        iterations_left -= 1
        start += 1
        if iterations_left == 0:
            print("\nIt is a Tie!! ")
            print("\n {0} | {1} | {2} \n-----|-----|-----\n {3} | {4} | {5} \n-----|-----|-----\n {6} | {7} | {8} \n"
                  .format(GameMemory[0],
                          GameMemory[1], GameMemory[2],
                          GameMemory[3], GameMemory[4],
                          GameMemory[5], GameMemory[6],
                          GameMemory[7], GameMemory[8]))


def clean():  # clear screen
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


Menu()
