import heapq
import sys

def read_input():
    track = []
    with open("./day20_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for i,line in enumerate(lines):
            if 'S' in line:
                start = (i, line.index('S'), 1)
                line = line.replace('S', '.')
            if 'E' in line:
                end = (i, line.index('E'))
                line = line.replace('E', '.')
            track.append(list(line.strip()))
    return track, start, end

def solve_1():
    track, start, end = read_input()
    path = get_path(track, start, end)
    sum = 0
    for i, p in enumerate(path):
        for j in range(i+3, len(path)):
            if (abs(p[0] - path[j][0]) + abs(p[1] - path[j][1])) <= 2:
                if j - i - 2 >= 100:
                    sum += 1
    print(sum)

def solve_2():
    track, start, end = read_input()
    path = get_path(track, start, end)
    sum = 0
    for i, p in enumerate(path):
        for j in range(i+3, len(path)):
            diff = (abs(p[0] - path[j][0]) + abs(p[1] - path[j][1]))
            if diff <= 20:
                if j - i - diff >= 100:
                    sum += 1
    print(sum)

def get_path(track, start, end):
    path = []
    curr = start
    while True:
        path.append(curr)
        if curr == end:
            break

        if track[curr[0] - 1][curr[1]] == '.' and (curr[0]-1, curr[1]) not in path:
            curr = (curr[0]-1, curr[1])
        elif track[curr[0]][curr[1] + 1] == '.' and (curr[0], curr[1] + 1) not in path:
            curr = (curr[0],curr[1]+1)
        elif track[curr[0] + 1][curr[1]] == '.' and (curr[0]+1, curr[1]) not in path:
            curr = (curr[0]+1,curr[1])
        elif (curr[0], curr[1]-1) not in path:
            curr = (curr[0], curr[1] - 1)
    
    return path

solve_1()
solve_2()