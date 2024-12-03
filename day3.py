import re

def read_input():
    with open("./day3_input.txt", "r", encoding="utf-8") as input:
        memory = input.read()
    return memory

def solve_1():
    sum = 0
    memory = read_input()
    muls = re.findall('mul\(\d+,\d+\)', memory, re.DOTALL)
    for mul in muls:
        sum += getMul(mul)
    print(sum)

def solve_2():
    sum = 0
    memory = read_input()
    muls = re.finditer('mul\(\d+,\d+\)', memory)
    dos = list(re.finditer('do\(\)', memory))
    donts = list(re.finditer('don\'t\(\)', memory))
    do = True
    for mul in muls:
        if do:
            if len(donts) == 0:     
                sum += getMul(mul.group())
            else:
                nextDont = donts[0]
                if mul.start() > nextDont.start():
                    do = False
                    donts.pop(0)
                    while True:
                        if len(dos) == 0:
                            break;
                        if mul.start() > dos[0].start():
                            dos.pop(0)
                        else:
                            break;
                else:
                    sum += getMul(mul.group())
        else:
            if len(dos) > 0:
                nextDo = dos[0]
                if mul.start() > nextDo.start():
                    do = True
                    dos.pop(0)
                    sum += getMul(mul.group())
                    while True:
                        if len(donts) == 0:
                            break;
                        if mul.start() > donts[0].start():
                            donts.pop(0)
                        else:
                            break;
    print(sum)

def getMul(string):
    nums = re.findall('\d+', string, re.DOTALL)
    return int(nums[0]) * int(nums[1])

solve_1()
solve_2()