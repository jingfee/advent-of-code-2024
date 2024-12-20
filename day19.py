from functools import cache

def read_input():
    patterns = []
    with open("./day19_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        towels = lines[0].strip().split(', ')
        for line in lines[2:]:
            patterns.append(line.strip())

    return towels, patterns

def solve_1():
    towels, patterns = read_input()
    sum = 0
    for pattern in patterns:
        a = check_pattern(pattern, towels)
        sum += a
    print(sum)

def solve_2():
    towels, patterns = read_input()
    sum = 0
    for pattern in patterns:
        a = check_pattern_rec(pattern, tuple(towels))
        sum += a
    print(sum)  

def check_pattern(pattern, towels):
    indexes = [0]
    visited = set()
    while len(indexes) > 0:
        index = indexes.pop()
        for towel in towels:
            match = True
            for i, c in enumerate(towel):
                if index + i == len(pattern) or c != pattern[index+i]:
                    match = False
                    break
            n = index + len(towel)
            if match and (n == len(pattern)):
                return True
            elif match and n not in visited:
                visited.add(n)
                indexes.append(n)
    return False

@cache
def check_pattern_rec(pattern: str, towels):   
    found = 0
    for towel in towels:
        if pattern == towel:
            found += 1
        elif pattern.startswith(towel):
            found += check_pattern_rec(pattern[len(towel):], towels)
    return found

solve_1()
solve_2()