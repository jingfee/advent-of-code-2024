def read_input():
    stones = []
    with open("./day11_input.txt", "r", encoding="utf-8") as input:
        line = input.readline()
        stones = list(map(lambda l: int(l), line.split()))
    return stones

def solve_1():
    stones = read_input()
    blinks = 25
    for i in range(blinks):
        newStones = []
        for stone in stones:
            if stone == 0:
                newStones.append(1)
            elif len(str(stone)) % 2 == 0:
                stringed = str(stone)
                newStones.append(int(stringed[:len(stringed)//2]))
                newStones.append(int(stringed[len(stringed)//2:]))
            else:
                newStones.append(stone*2024)
        stones = newStones

    print(len(stones))

def solve_2():
    stones = read_input()
    dict = {}
    for stone in stones:
        add_to_dict(dict, stone, 1)
    blinks = 75
    for i in range(blinks):
        newDict = {}
        for stone in dict:
            if stone == 0:
                new = 1
                add_to_dict(newDict, new, dict[stone])
            elif len(str(stone)) % 2 == 0:
                stringed = str(stone)
                new1 = int(stringed[:len(stringed)//2])
                new2 = int(stringed[len(stringed)//2:])
                add_to_dict(newDict, new1, dict[stone])
                add_to_dict(newDict, new2, dict[stone])
            else:
                new = stone*2024
                add_to_dict(newDict, new, dict[stone])
        dict = newDict
    sum = 0
    for stone in dict:
        sum += dict[stone]
    print(sum)

def add_to_dict(dict, stone, number):
    if stone in dict:
        dict[stone] += number
    else:
        dict[stone] = number

solve_1()
solve_2()