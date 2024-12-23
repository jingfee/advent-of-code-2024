def read_input():
    codes = []
    with open("./day21_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for line in lines:
            split = list(line.strip())
            code = []
            for s in split:
                code.append(s)
            codes.append(code)
    return codes

def solve_1():
    codes = read_input()
    solve(codes, 2)

def solve_2():
    codes = read_input()
    solve(codes, 25)


def solve(codes, maxDepth):
    sum = 0
    numpad_map = build_numpad_map()
    directional_map = build_directional_map()
    for code in codes:
        result = get_robot(code, numpad_map)
        min_arr = []
        for r in result:
            min_arr.append(shortest_rec(r, maxDepth, {}, directional_map))
        sum += min(min_arr) * int(''.join(code[:3]))
    print(sum)


def get_robot(code, key_map):
    queue = [('', 'A', 0)]
    found = []
    while len(queue) > 0:
        curr = queue.pop()
        if curr[2] == len(code):
            found.append(curr[0])
            continue
        paths = key_map[curr[1]][code[curr[2]]]
        for path in paths:
            queue.append((curr[0] + path + 'A', code[curr[2]], curr[2] + 1))
    return tuple(found)

def shortest_rec(keys, depth, cache, key_map):
    if depth == 0:
        return len(keys)
    if (keys, depth) in cache:
        return cache[(keys, depth)]
    split = keys.split('A')
    sum = 0
    for s in split[:-1]:
        result = get_robot(s + 'A', key_map)
        min_arr = []
        for r in result:
            min_arr.append(shortest_rec(r, depth - 1, cache, key_map))
        sum += min(min_arr)
    cache[(keys, depth)] = sum
    return sum
        


def build_numpad_map():
    numpad_map = {}

    numpad_map['A'] = {}
    numpad_map['A']['A'] = ['']
    numpad_map['A']['0'] = ['<']
    numpad_map['A']['1'] = ['^<<']
    numpad_map['A']['2'] = ['^<', '<^']
    numpad_map['A']['3'] = ['^']
    numpad_map['A']['4'] = ['^^<<']
    numpad_map['A']['5'] = ['^^<', '<^^']
    numpad_map['A']['6'] = ['^^']
    numpad_map['A']['7'] = ['^^^<<']
    numpad_map['A']['8'] = ['^^^<', '<^^^']
    numpad_map['A']['9'] = ['^^^']

    numpad_map['0'] = {}
    numpad_map['0']['A'] = ['>']
    numpad_map['0']['0'] = ['']
    numpad_map['0']['1'] = ['^<']
    numpad_map['0']['2'] = ['^']
    numpad_map['0']['3'] = ['^>']
    numpad_map['0']['4'] = ['^^<']
    numpad_map['0']['5'] = ['^^']
    numpad_map['0']['6'] = ['^^>', '>^^']
    numpad_map['0']['7'] = ['^^^<']
    numpad_map['0']['8'] = ['^^^']
    numpad_map['0']['9'] = ['^^^>', '>^^^']

    numpad_map['1'] = {}
    numpad_map['1']['A'] = ['>>v']
    numpad_map['1']['0'] = ['>v']
    numpad_map['1']['1'] = ['']
    numpad_map['1']['2'] = ['>']
    numpad_map['1']['3'] = ['>>']
    numpad_map['1']['4'] = ['^']
    numpad_map['1']['5'] = ['^>', '>^']
    numpad_map['1']['6'] = ['>>^', '^>>']
    numpad_map['1']['7'] = ['^^']
    numpad_map['1']['8'] = ['^^>', '>^^']
    numpad_map['1']['9'] = ['^^>>', '>>^^']

    numpad_map['2'] = {}
    numpad_map['2']['A'] = ['>v', 'v>']
    numpad_map['2']['0'] = ['v']
    numpad_map['2']['1'] = ['<']
    numpad_map['2']['2'] = ['']
    numpad_map['2']['3'] = ['>']
    numpad_map['2']['4'] = ['<^', '^<']
    numpad_map['2']['5'] = ['^']
    numpad_map['2']['6'] = ['>^', '^>']
    numpad_map['2']['7'] = ['^^<', '<^^']
    numpad_map['2']['8'] = ['^^']
    numpad_map['2']['9'] = ['^^>', '>^^']

    numpad_map['3'] = {}
    numpad_map['3']['A'] = ['v']
    numpad_map['3']['0'] = ['<v', 'v<']
    numpad_map['3']['1'] = ['<<']
    numpad_map['3']['2'] = ['<']
    numpad_map['3']['3'] = ['']
    numpad_map['3']['4'] = ['<<^', '^<<']
    numpad_map['3']['5'] = ['<^', '^<']
    numpad_map['3']['6'] = ['^']
    numpad_map['3']['7'] = ['^^<<', '<<^^']
    numpad_map['3']['8'] = ['^^<', '<^^']
    numpad_map['3']['9'] = ['^^']

    numpad_map['4'] = {}
    numpad_map['4']['A'] = ['>>vv']
    numpad_map['4']['0'] = ['>vv']
    numpad_map['4']['1'] = ['v']
    numpad_map['4']['2'] = ['>v', 'v>']
    numpad_map['4']['3'] = ['v>>', '>>v']
    numpad_map['4']['4'] = ['']
    numpad_map['4']['5'] = ['>']
    numpad_map['4']['6'] = ['>>']
    numpad_map['4']['7'] = ['^']
    numpad_map['4']['8'] = ['^>', '>^']
    numpad_map['4']['9'] = ['^>>', '>>^']

    numpad_map['5'] = {}
    numpad_map['5']['A'] = ['>vv', 'vv>']
    numpad_map['5']['0'] = ['vv']
    numpad_map['5']['1'] = ['<v', 'v<']
    numpad_map['5']['2'] = ['v']
    numpad_map['5']['3'] = ['v>', '>v']
    numpad_map['5']['4'] = ['<']
    numpad_map['5']['5'] = ['']
    numpad_map['5']['6'] = ['>']
    numpad_map['5']['7'] = ['^<', '<^']
    numpad_map['5']['8'] = ['^']
    numpad_map['5']['9'] = ['^>', '>^']

    numpad_map['6'] = {}
    numpad_map['6']['A'] = ['vv']
    numpad_map['6']['0'] = ['vv<', '<vv']
    numpad_map['6']['1'] = ['<<v', 'v<<']
    numpad_map['6']['2'] = ['v<', '<v']
    numpad_map['6']['3'] = ['v']
    numpad_map['6']['4'] = ['<<']
    numpad_map['6']['5'] = ['<']
    numpad_map['6']['6'] = ['']
    numpad_map['6']['7'] = ['^<<', '<<^']
    numpad_map['6']['8'] = ['<^', '^<']
    numpad_map['6']['9'] = ['^', '^']

    numpad_map['7'] = {}
    numpad_map['7']['A'] = ['>>vvv']
    numpad_map['7']['0'] = ['>vvv']
    numpad_map['7']['1'] = ['vv']
    numpad_map['7']['2'] = ['vv>', '>vv']
    numpad_map['7']['3'] = ['vv>>', '>>vv']
    numpad_map['7']['4'] = ['v']
    numpad_map['7']['5'] = ['>v', 'v>']
    numpad_map['7']['6'] = ['>>v', 'v>>']
    numpad_map['7']['7'] = ['']
    numpad_map['7']['8'] = ['>']
    numpad_map['7']['9'] = ['>>']

    numpad_map['8'] = {}
    numpad_map['8']['A'] = ['>vvv', 'vvv>']
    numpad_map['8']['0'] = ['vvv']
    numpad_map['8']['1'] = ['vv<', '<vv']
    numpad_map['8']['2'] = ['vv']
    numpad_map['8']['3'] = ['vv>', '>vv']
    numpad_map['8']['4'] = ['v<', '<v']
    numpad_map['8']['5'] = ['v']
    numpad_map['8']['6'] = ['>v', 'v>']
    numpad_map['8']['7'] = ['<']
    numpad_map['8']['8'] = ['']
    numpad_map['8']['9'] = ['>']

    numpad_map['9'] = {}
    numpad_map['9']['A'] = ['vvv']
    numpad_map['9']['0'] = ['vvv<', '<vvv']
    numpad_map['9']['1'] = ['vv<<', '<<vv']
    numpad_map['9']['2'] = ['vv<', '<vv']
    numpad_map['9']['3'] = ['vv']
    numpad_map['9']['4'] = ['v<<', '<<v']
    numpad_map['9']['5'] = ['v<', '<v']
    numpad_map['9']['6'] = ['v']
    numpad_map['9']['7'] = ['<<']
    numpad_map['9']['8'] = ['<']
    numpad_map['9']['9'] = ['']

    return numpad_map

def build_directional_map():
    directional_map = {}

    directional_map['A'] = {}
    directional_map['A']['A'] = ['']
    directional_map['A']['^'] = ['<']
    directional_map['A']['>'] = ['v']
    directional_map['A']['v'] = ['v<', '<v']
    directional_map['A']['<'] = ['v<<']

    directional_map['^'] = {}
    directional_map['^']['A'] = ['>']
    directional_map['^']['^'] = ['']
    directional_map['^']['>'] = ['v>', '>v']
    directional_map['^']['v'] = ['v']
    directional_map['^']['<'] = ['v<']

    directional_map['>'] = {}
    directional_map['>']['A'] = ['^']
    directional_map['>']['^'] = ['^<', '<^']
    directional_map['>']['>'] = ['']
    directional_map['>']['v'] = ['<']
    directional_map['>']['<'] = ['<<']

    directional_map['v'] = {}
    directional_map['v']['A'] = ['^>', '>^']
    directional_map['v']['^'] = ['^']
    directional_map['v']['>'] = ['>']
    directional_map['v']['v'] = ['']
    directional_map['v']['<'] = ['<']

    directional_map['<'] = {}
    directional_map['<']['A'] = ['>>^']
    directional_map['<']['^'] = ['>^']
    directional_map['<']['>'] = ['>>']
    directional_map['<']['v'] = ['>']
    directional_map['<']['<'] = ['']

    return directional_map


solve_1()
solve_2()