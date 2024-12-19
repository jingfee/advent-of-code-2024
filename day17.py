from math import floor

def read_input():
    with open("./day17_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        reg_a = int(lines[0].split(': ')[1])
        reg_b = int(lines[1].split(': ')[1])
        reg_c = int(lines[2].split(': ')[1])
        program = list(map(lambda a: int(a), lines[4].split(': ')[1].split(',')))

    return reg_a,reg_b,reg_c,program

def solve_1():
    reg_a,reg_b,reg_c,program = read_input()
    output = run_program(reg_a,reg_b,reg_c,program)
    print(','.join(map(lambda a: str(a), output)))

def solve_2():
    reg_a,reg_b,reg_c,program = read_input()
    a = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    i = 0
    j = 0
    while i < 16:
        while j < 8:
            found = False
            if i == 0 and j == 0:
                j += 1
                continue
            a[i] = j
            dec = int(''.join(map(lambda b: str(b), a)), 8)
            output = run_program(dec, reg_b, reg_c, program)
            if output[15-i] == program[15-i]:
                found = True
                break
            j += 1
        if found:
            i += 1
            j = 0
        else:
            i -= 1
            j = a[i] + 1
    print(int(''.join(map(lambda b: str(b), a)), 8))

def run_program(reg_a,reg_b,reg_c,program):
    pointer = 0
    output = []
    while True:
        if pointer > len(program) - 2:
            break
        opcode = program[pointer]
        operand = program[pointer+1]
        jump = False
        match opcode:
            case 0:
                reg_a = floor(reg_a / pow(2, get_combo(operand, reg_a, reg_b, reg_c)))
            case 1:
                reg_b = reg_b ^ operand
            case 2:
                reg_b = get_combo(operand, reg_a, reg_b, reg_c) % 8
            case 3:
                if reg_a != 0:
                    pointer = operand
                    jump = True
            case 4:
                reg_b = reg_b ^ reg_c
            case 5:
                output.append(get_combo(operand, reg_a, reg_b, reg_c) % 8)
            case 6:
                reg_b = floor(reg_a / pow(2, get_combo(operand, reg_a, reg_b, reg_c)))
            case 7:
                reg_c = floor(reg_a / pow(2, get_combo(operand, reg_a, reg_b, reg_c)))
        if not jump:
            pointer += 2
    return output



def get_combo(operand, reg_a, reg_b, reg_c):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c
    else:
        print('Error')
        return -1

solve_1()
solve_2()