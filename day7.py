def read_input():
    equations = []
    with open("./day7_input.txt", "r", encoding="utf-8") as input:
        for line in input:
            equations.append(line.strip())

    return equations

def solve_1():
    equations = read_input()
    sum = 0
    for equation in equations:
        split = equation.split()
        result = int(split[0].replace(':', ''))
        numbers = list(map(lambda n: int(n), split[1:]))
        sum += result if check_equation(result, numbers, False) else 0
    print(sum)

def solve_2():
    equations = read_input()
    sum = 0
    for equation in equations:
        split = equation.split()
        result = int(split[0].replace(':', ''))
        numbers = list(map(lambda n: int(n), split[1:]))
        sum += result if check_equation(result, numbers, True) else 0
    print(sum)

def check_equation(result, numbers, concat):
    queue = [(numbers[0], 0)]
    while len(queue) > 0:
        curr = queue.pop()
        if curr[1] == len(numbers) - 1:
            if curr[0] == result:
                return True
            else:
                continue

        queue.append((curr[0] * numbers[curr[1]+1], curr[1] + 1))
        queue.append((curr[0] + numbers[curr[1]+1], curr[1] + 1))
        if concat:
           queue.append((int(str(curr[0]) + str(numbers[curr[1]+1])), curr[1] + 1)) 

solve_1()
solve_2()