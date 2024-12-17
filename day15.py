

def read_input():
    robot_map = []
    movements = []
    with open("./day15_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for i,line in enumerate(lines):
            if line == '\n':
                break
            if '@' in line:
                robot_pos = (i, line.index('@'))
            robot_map.append(list(line.strip()))
        
        for j in range(i+1, len(lines)):
            movements.extend(list(lines[j].strip()))

    return robot_map, robot_pos, movements

def read_input_wide():
    robot_map = []
    movements = []
    with open("./day15_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for i,line in enumerate(lines):
            row = []
            if line == '\n':
                break
            if '@' in line:
                robot_pos = (i, line.index('@')*2)
            for a in line.strip():
                match a:
                    case '#':
                        row.append('#')
                        row.append('#')
                    case 'O':
                        row.append('[')
                        row.append(']')
                    case '.':
                        row.append('.')
                        row.append('.')
                    case '@':
                        row.append('@')
                        row.append('.')

            robot_map.append(row)
        
        for j in range(i+1, len(lines)):
            movements.extend(list(lines[j].strip()))

    return robot_map, robot_pos, movements

def solve_1():
    robot_map, robot_pos, movements = read_input()
    for movement in movements:
        robot_pos = move_robot(robot_map, robot_pos, movement)
    gps = sum_gps(robot_map)
    print(gps)

def solve_2():
    robot_map, robot_pos, movements = read_input_wide()
    for movement in movements:
        robot_pos = move_robot_wide(robot_map, robot_pos, movement)
    gps = sum_gps_wide(robot_map)
    print(gps)

def move_robot(robot_map, robot_pos, movement):
    match movement:
        case '^':
            y_offset = -1
            x_offset = 0
        case '>':
            y_offset = 0
            x_offset = 1
        case 'v':
            y_offset = 1
            x_offset = 0
        case '<':
            y_offset = 0
            x_offset = -1

    next_map = robot_map[robot_pos[0]+y_offset][robot_pos[1]+x_offset]
    if next_map == '.':
        robot_map[robot_pos[0]+y_offset][robot_pos[1]+x_offset] = '@'
        robot_map[robot_pos[0]][robot_pos[1]] = '.'
        robot_pos = (robot_pos[0]+y_offset, robot_pos[1]+x_offset)
    elif next_map == 'O':
        boxes = 1
        while True:
            if robot_map[robot_pos[0]+boxes*y_offset][robot_pos[1]+boxes*x_offset] == 'O':
                boxes += 1
            if robot_map[robot_pos[0]+boxes*y_offset][robot_pos[1]+boxes*x_offset] == '.':
                robot_map[robot_pos[0]+boxes*y_offset][robot_pos[1]+boxes*x_offset] = 'O'
                robot_map[robot_pos[0]+y_offset][robot_pos[1]+x_offset] = '@'
                robot_map[robot_pos[0]][robot_pos[1]] = '.'
                robot_pos = (robot_pos[0]+y_offset, robot_pos[1]+x_offset)
                break
            if robot_map[robot_pos[0]+boxes*y_offset][robot_pos[1]+boxes*x_offset] == '#':
                break  
    return robot_pos

def move_robot_wide(robot_map, robot_pos, movement):
    match movement:
        case '^':
            y_offset = -1
            x_offset = 0
        case '>':
            y_offset = 0
            x_offset = 1
        case 'v':
            y_offset = 1
            x_offset = 0
        case '<':
            y_offset = 0
            x_offset = -1

    next_map = robot_map[robot_pos[0]+y_offset][robot_pos[1]+x_offset]
    if next_map == '.':
        robot_map[robot_pos[0]+y_offset][robot_pos[1]+x_offset] = '@'
        robot_map[robot_pos[0]][robot_pos[1]] = '.'
        robot_pos = (robot_pos[0]+y_offset, robot_pos[1]+x_offset)
    elif next_map == '[' or next_map == ']':
        boxes = 1
        if x_offset != 0:
            while True:
                if robot_map[robot_pos[0]][robot_pos[1]+boxes*x_offset] == '[' or robot_map[robot_pos[0]][robot_pos[1]+boxes*x_offset] == ']':
                    boxes += 1
                elif robot_map[robot_pos[0]][robot_pos[1]+boxes*x_offset] == '.':
                    robot_map[robot_pos[0]][robot_pos[1]] = '.'
                    robot_map[robot_pos[0]][robot_pos[1]+x_offset] = '@'
                    for i in range(1, boxes):
                        robot_map[robot_pos[0]][robot_pos[1]+x_offset*(i+1)] = '[' if i % 2 == (0 if x_offset < 0 else 1) else ']'
                    robot_pos = (robot_pos[0], robot_pos[1]+x_offset)
                    break
                elif robot_map[robot_pos[0]][robot_pos[1]+boxes*x_offset] == '#':
                    break
        if y_offset != 0:
            box_x = {robot_pos[0]+y_offset: [robot_pos[1]-1 if next_map == ']' else robot_pos[1]+1, robot_pos[1]]}
            while True:
                level_x = box_x[robot_pos[0]+boxes*y_offset]
                level_x_chars = []
                for i in level_x:
                    level_x_chars.append(robot_map[robot_pos[0]+(boxes+1)*y_offset][i])

                all_free = all(a == '.' for a in level_x_chars)
                any_wall = any(a == '#' for a in level_x_chars)

                if all_free:
                    for i in reversed(box_x):
                        for j in box_x[i]:
                            char = robot_map[i][j]
                            robot_map[i][j] = '.'
                            robot_map[i+y_offset][j] = char
                    robot_map[robot_pos[0]][robot_pos[1]] = '.'
                    robot_map[robot_pos[0]+y_offset][robot_pos[1]] = '@'
                    robot_pos = (robot_pos[0]+y_offset, robot_pos[1])
                    break
                elif any_wall:
                    break
                else:
                    boxes += 1     
                    next = set()
                    for i in level_x:
                        b = robot_map[robot_pos[0]+boxes*y_offset][i]
                        if b == '[' or b == ']':
                            next.add(i-1 if b == ']' else i+1)
                            next.add(i)
                    box_x[robot_pos[0]+boxes*y_offset] = next               

    return robot_pos 

def sum_gps(robot_map):
    sum = 0
    for i,r in enumerate(robot_map):
        for j,c in enumerate(r):
            if c == 'O':
                sum += 100*i + j
    return sum

def sum_gps_wide(robot_map):
    sum = 0
    for i,r in enumerate(robot_map):
        for j,c in enumerate(r):
            if c == '[':
                sum += 100*i + j
    return sum

solve_1()
solve_2()