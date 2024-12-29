from math import floor

def read_input():
    values = {}
    operations = []
    with open("./day24_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        read_init = True
        for i,line in enumerate(lines):
            if line == '\n':
                read_init = False
                continue
            
            if read_init:
                split = line.split(': ')
                values[split[0]] = int(split[1])
            else:
                split = line.split(' ')
                operation = (split[0], split[2], split[1], split[4].strip())
                operations.append(operation)

    return values, operations

def solve_1():
    values, operations = read_input()
    val = calc(values, operations)
    print(val)

def solve_2():
    values, operations = read_input()

    faulty_1 = list(filter(lambda x: x[3].startswith('z') and x[3] != 'z45' and x[2] != 'XOR', operations))
    faulty_2 = list(filter(lambda x: not x[3].startswith('z') and not x[0].startswith('x') and not x[0].startswith('y') and x[2] == 'XOR', operations))
    for a in faulty_2:
        b = next((x for x in faulty_1 if x[3] == first_rec(operations, a[3])))
        
        index_a = next((i for i, item in enumerate(operations) if item[3] == a[3]), -1)
        index_b = next((i for i, item in enumerate(operations) if item[3] == b[3]), -1)
        operations[index_a] = (a[0], a[1], a[2], b[3])
        operations[index_b] = (b[0], b[1], b[2], a[3])
    falseCarry = str(count_trailing_zero_bits((get_wires_as_long(values, 'x') + get_wires_as_long(values, 'y') ^ calc(values, operations))))
    faulty_3 = list(filter(lambda x: x[0].endswith(falseCarry) or x[1].endswith(falseCarry), operations))
    print(','.join(sorted(map(lambda x: x[3], (faulty_1 + faulty_2 + faulty_3)))))

    
def calc(values, operations):
    queue = list(operations)
    while len(queue) > 0:
        operation = queue.pop(0)
        if operation[0] not in values or operation[1] not in values:
            queue.append(operation)
            continue

        val_1 = values[operation[0]]
        val_2 = values[operation[1]]
        out = operation[3]
        operator = operation[2]
        match operator:
            case 'AND':
                values[out] = 1 if val_1 and val_2 else 0
            case 'OR':
                values[out] = 1 if val_1 or val_2 else 0
            case 'XOR':
                values[out] = 1 if val_1 != val_2 else 0
    return get_wires_as_long(values, 'z')

def first_rec(operations, output):
    filtered = list(filter(lambda x: x[0] == output or x[1] == output, operations))
    result = next((it for it in filtered if it[3].startswith('z')), None)
    if result:
        return "z" + str(int(result[3][1:]) - 1).zfill(2)
    return next((first_rec(operations, operation[3]) for operation in filtered), None)

def get_wires_as_long(values, type):
    return int(''.join(map(lambda x: str(x), dict(sorted({k: v for k, v in values.items() if k.startswith(type)}.items(), reverse=True)).values())), 2)

def count_trailing_zero_bits(n):
    return (n & -n).bit_length() - 1 if n != 0 else 0

solve_1()
solve_2()