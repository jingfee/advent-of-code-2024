from math import floor

def read_input():
    locks = []
    keys = []
    with open("./day25_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        is_lock = lines[0][0] == '#'
        counter = [0,0,0,0,0]
        for i,line in enumerate(lines):
            if i == 0 or i % 8 == 0 or line == '\n':
                continue
            if  i == len(lines) - 1 or lines[i+1] == '\n':
                if is_lock:
                    locks.append(counter)
                else:
                    keys.append(counter)
                if i != len(lines) - 1:
                    is_lock = lines[i+2][0] == '#'
                    counter = [0,0,0,0,0]
                continue

            for j in range(5):
                counter[j] += 1 if line[j] == '#' else 0

    return locks, keys

def solve_1():
    locks, keys = read_input()
    sum = 0
    for lock in locks:
        for key in keys:
            overlap = False
            for i in range(5):
                if lock[i] + key[i] > 5:
                    overlap = True
                    break
            if not overlap:
                sum += 1
    print(sum)

solve_1()
#solve_2()