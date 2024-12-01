def read_input():
    left = []
    right = []
    with open("./day1_input.txt", "r", encoding="utf-8") as input:
        for line in input:
            split = line.split()
            left.append(int(split[0]))
            right.append(int(split[1]))
    left.sort()
    right.sort()
    return left, right

def solve_1():
    left, right = read_input()

    sum = 0
    for i, l in enumerate(left):
        sum += abs(l - right[i])
    
    print(sum)

def solve_2():
    left, right = read_input()

    sum = 0
    for l in left:
        count = right.count(l)
        sum += (l*count)

    print(sum)



solve_1()
solve_2()