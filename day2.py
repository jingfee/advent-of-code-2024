def read_input():
    levels = []
    with open("./day2_input.txt", "r", encoding="utf-8") as input:
        for line in input:
            split = line.split()
            levels.append(list(map(lambda s: int(s), split)))
    return levels

def solve_1():
    levels = read_input()

    count = 0
    for level in levels:
        safe = is_safe(level)
        if safe:
            count += 1
    print(count)

def solve_2():
    levels = read_input()

    count = 0
    for level in levels:
        safe = is_safe(level)
        if safe:
            count += 1
        else:
            for i,a in enumerate(level):
                dampened = list(level)
                del dampened[i]
                safe = is_safe(dampened)
                if safe:
                    count += 1
                    break
    print(count)

def is_safe(level):
    prev = level[0]
    unsafe = False
    increasing = level[1] > level[0]
    for curr in level[1:]:
        diff = abs(curr-prev)
        if (diff == 0 or diff > 3) or (increasing and curr < prev) or (not(increasing) and curr > prev):
            unsafe = True
            break
        prev = curr
    return not(unsafe)

solve_1()
solve_2()