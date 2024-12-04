import re

def read_input():
    letters = []
    with open("./day4_input.txt", "r", encoding="utf-8") as input:
        for line in input:
            letters.append(list(line.strip()))
    return letters

def solve_1():
    sum = 0
    letters = read_input()
    for i, line in enumerate(letters):
        for j, letter in enumerate(line):
            if letter == 'X':
                sum += 1 if horizontal(line, j) else 0
                sum += 1 if revHorizontal(line, j) else 0
                sum += 1 if vertical(letters, i, j) else 0
                sum += 1 if revVertical(letters, i, j) else 0
                sum += 1 if diagonal(letters, i, j) else 0
                sum += 1 if revDiagonal(letters, i, j) else 0
                sum += 1 if mirrorDiagonal(letters, i, j) else 0
                sum += 1 if revMirrorDiagonal(letters, i, j) else 0
    print(sum)

def horizontal(line, j):
    if j + 3 >= len(line):
        return False
    return line[j+1] == 'M' and line[j+2] == 'A' and line[j+3] == 'S'

def revHorizontal(line, j):
    if j - 3 < 0:
        return False
    return line[j-1] == 'M' and line[j-2] == 'A' and line[j-3] == 'S'

def vertical(letters, i, j):
    if i+3 >= len(letters):
        return False
    return letters[i+1][j] == 'M' and letters[i+2][j] == 'A' and letters[i+3][j] == 'S'

def revVertical(letters, i, j):
    if i-3 < 0:
        return False
    return letters[i-1][j] == 'M' and letters[i-2][j] == 'A' and letters[i-3][j] == 'S'

def diagonal(letters, i, j):
    if i+3 >= len(letters) or j+3 >= len(letters[i]):
        return False
    return letters[i+1][j+1] == 'M' and letters[i+2][j+2] == 'A' and letters[i+3][j+3] == 'S'

def revDiagonal(letters, i, j):
    if i-3 < 0 or j-3 < 0:
        return False
    return letters[i-1][j-1] == 'M' and letters[i-2][j-2] == 'A' and letters[i-3][j-3] == 'S'

def mirrorDiagonal(letters, i, j):
    if i+3 >= len(letters) or j-3 < 0:
        return False
    return letters[i+1][j-1] == 'M' and letters[i+2][j-2] == 'A' and letters[i+3][j-3] == 'S'

def revMirrorDiagonal(letters, i, j):
    if i-3 < 0 or j+3 >= len(letters[i]):
        return False
    return letters[i-1][j+1] == 'M' and letters[i-2][j+2] == 'A' and letters[i-3][j+3] == 'S'

def solve_2():
    sum = 0
    letters = read_input()
    for i, line in enumerate(letters):
        for j, letter in enumerate(line):
            if letter == 'A':
                sum += 1 if masDiagonal(letters, i, j) and masMirrorDiagonal(letters, i, j) else 0
    print(sum)

def masDiagonal(letters, i, j):
    if i-1 < 0 or j -1 < 0 or i+1 >= len(letters) or j+1 >= len(letters[i]):
        return False
    return (letters[i-1][j-1] == 'M' and letters[i+1][j+1] == 'S') or (letters[i-1][j-1] == 'S' and letters[i+1][j+1] == 'M')

def masMirrorDiagonal(letters, i, j):
    if i-1 < 0 or j -1 < 0 or i+1 >= len(letters) or j+1 >= len(letters[i]):
        return False
    return (letters[i-1][j+1] == 'M' and letters[i+1][j-1] == 'S') or (letters[i-1][j+1] == 'S' and letters[i+1][j-1] == 'M')

solve_1()
solve_2()