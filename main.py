from pprint import *
import copy
import time

# load wordlist and bigrams

with open('dict.txt') as file:
    wordlist = file.read().splitlines()

with open('bigrams.txt') as file:
    bigrams = file.read().splitlines()


def main():

    board = [
        ['0', '0', '0', '0'],
        ['0', '0', '0', '0'],
        ['0', '0', '0', '0'],
        ['0', '0', '0', '0'],
    ]

    # read in board

    for i in range(16):
        board[i // 4][i % 4] = input()[0]

    pprint(board)

    start_time = time.time()

    for i in range(16):
        recursive_search(copy.deepcopy(board), i // 4, i % 4, "")
        print()

    print("--- %s seconds ---" % (time.time() - start_time))


def recursive_search(board, i, j, word):
    if (board[i][j] == '0'):
        return
    
    if (len(word) >= 2 and word[-2:] in bigrams):
        return

    word += board[i][j]

    board[i][j] = '0'

    if len(word) > 4 and word in wordlist:
        if len(word) == 6:
            print(word + "-----------")
        elif len(word) == 5:
            print(word)
        else:
            print(word)

    if len(word) == 6:
        return

    top = i == 0
    bottom = i == 3
    left = j == 0
    right = j == 3

    if top and left:
        recursive_search(copy.deepcopy(board), i + 1, j, word)
        recursive_search(copy.deepcopy(board), i, j + 1, word)
        recursive_search(copy.deepcopy(board), i + 1, j + 1, word)
        return
    if top and right:
        recursive_search(copy.deepcopy(board), i + 1, j, word)
        recursive_search(copy.deepcopy(board), i, j - 1, word)
        recursive_search(copy.deepcopy(board), i + 1, j - 1, word)
        return
    if bottom and left:
        recursive_search(copy.deepcopy(board), i - 1, j, word)
        recursive_search(copy.deepcopy(board), i, j + 1, word)
        recursive_search(copy.deepcopy(board), i - 1, j + 1, word)
        return
    if bottom and right:
        recursive_search(copy.deepcopy(board), i - 1, j, word)
        recursive_search(copy.deepcopy(board), i, j - 1, word)
        recursive_search(copy.deepcopy(board), i - 1, j - 1, word)
        return
    if top:
        recursive_search(copy.deepcopy(board), i + 1, j, word)
        recursive_search(copy.deepcopy(board), i, j + 1, word)
        recursive_search(copy.deepcopy(board), i, j - 1, word)
        recursive_search(copy.deepcopy(board), i + 1, j + 1, word)
        recursive_search(copy.deepcopy(board), i + 1, j - 1, word)
        return
    if left:
        recursive_search(copy.deepcopy(board), i + 1, j, word)
        recursive_search(copy.deepcopy(board), i - 1, j, word)
        recursive_search(copy.deepcopy(board), i, j + 1, word)
        recursive_search(copy.deepcopy(board), i + 1, j + 1, word)
        recursive_search(copy.deepcopy(board), i - 1, j + 1, word)
        return
    if bottom:
        recursive_search(copy.deepcopy(board), i - 1, j, word)
        recursive_search(copy.deepcopy(board), i, j + 1, word)
        recursive_search(copy.deepcopy(board), i, j - 1, word)
        recursive_search(copy.deepcopy(board), i - 1, j + 1, word)
        recursive_search(copy.deepcopy(board), i - 1, j - 1, word)
        return
    if right:
        recursive_search(copy.deepcopy(board), i - 1, j, word)
        recursive_search(copy.deepcopy(board), i, j - 1, word)
        recursive_search(copy.deepcopy(board), i + 1, j - 1, word)
        recursive_search(copy.deepcopy(board), i + 1, j, word)
        recursive_search(copy.deepcopy(board), i - 1, j - 1, word)
        return

    recursive_search(copy.deepcopy(board), i + 1, j, word)
    recursive_search(copy.deepcopy(board), i - 1, j, word)
    recursive_search(copy.deepcopy(board), i, j + 1, word)
    recursive_search(copy.deepcopy(board), i, j - 1, word)
    recursive_search(copy.deepcopy(board), i + 1, j + 1, word)
    recursive_search(copy.deepcopy(board), i + 1, j - 1, word)
    recursive_search(copy.deepcopy(board), i - 1, j + 1, word)
    recursive_search(copy.deepcopy(board), i - 1, j - 1, word)
    return


if __name__ == '__main__':
    main()
