import re
import numpy as np

def read_input():
    machines = []
    with open("./day13_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        machine = {}
        for line in lines:
            if line == '\n':
                machines.append(machine)
                machine = {}
            elif 'Button A' in line:
                s = re.search('Button A: X\+(\d+), Y\+(\d+)', line)
                machine['a'] = (int(s.group(1)), int(s.group(2)))
            elif 'Button B' in line:
                s = re.search('Button B: X\+(\d+), Y\+(\d+)', line)
                machine['b'] = (int(s.group(1)), int(s.group(2)))
            elif 'Prize' in line:
                s = re.search('Prize: X=(\d+), Y=(\d+)', line)
                machine['p'] = (int(s.group(1)), int(s.group(2)))

        machines.append(machine)
    return machines

def solve_1():
    machines = read_input()
    tokens = 0
    for machine in machines:
        s = get_tokens(machine, 0)
        tokens += s
    print(tokens)

def solve_2():
    machines = read_input()
    tokens = 0
    for machine in machines:
        s = get_tokens(machine, 10000000000000)
        tokens += s
    print(tokens)

def get_tokens(machine, offset):
    a = abs(((machine['p'][0]+offset)*machine['b'][1] - (machine['p'][1]+offset)*machine['b'][0])/(machine['a'][0]*machine['b'][1] - machine['a'][1]*machine['b'][0]))
    b = abs(((machine['p'][0]+offset)*machine['a'][1] - (machine['p'][1]+offset)*machine['a'][0])/(machine['a'][0]*machine['b'][1] - machine['a'][1]*machine['b'][0]))

    if not a.is_integer() or not b.is_integer():
        return 0
    return 3*round(a)+round(b)


solve_1()
solve_2()