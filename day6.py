def read_input():
    map = []
    guard_position = ()
    with open("./day6_input.txt", "r", encoding="utf-8") as input:
        for i, line in enumerate(input):
            map.append(list(line.strip()))
            if '^' in line:
                guard_position = (i, line.index('^'))

    return map, guard_position

def solve_1():
    map, guard_position = read_input()
    direction = 0

    visited = {guard_position}
    
    while True:
        next = get_next_position(guard_position, direction)
        if next[0] < 0 or next[1] < 0 or next[0] >= len(map) or next[1] >= len(map[0]):
            break;

        next_tile = map[next[0]][next[1]]

        if next_tile == '#':
            direction = (direction + 1) % 4
        else:
            guard_position = next
            visited.add(guard_position)

    print(len(visited))

def solve_2():
    map, guard_position_start = read_input()
    direction = 0

    possible_obstructions = set()
    guard_position = guard_position_start
    
    while True:
        next = get_next_position(guard_position, direction)
        if next[0] < 0 or next[1] < 0 or next[0] >= len(map) or next[1] >= len(map[0]):
            break;

        next_tile = map[next[0]][next[1]]

        if next_tile == '#':
            direction = (direction + 1) % 4
        else:
            guard_position = next
            possible_obstructions.add(guard_position)

    sum = 0
    for possible_obstruction in possible_obstructions:
        guard_position = guard_position_start
        direction = 0
        visited = {(guard_position[0], guard_position[1], direction)}

        while True:
            next = get_next_position(guard_position, direction)

            if (next[0], next[1], direction) in visited:
                sum += 1
                break

            if next[0] < 0 or next[1] < 0 or next[0] >= len(map) or next[1] >= len(map[0]):
                break;

            next_tile = map[next[0]][next[1]]

            if next_tile == '#' or (next[0] == possible_obstruction[0] and next[1] == possible_obstruction[1]):
                direction = (direction + 1) % 4
            else:
                guard_position = next
                visited.add((guard_position[0], guard_position[1], direction))
    
    print(sum)


def get_next_position(guard_position, direction):
    match direction:
        case 0:
            return (guard_position[0] - 1, guard_position[1])
        case 1:
            return (guard_position[0], guard_position[1] + 1)
        case 2:
            return (guard_position[0] +1, guard_position[1])
        case 3:
            return (guard_position[0], guard_position[1] -1)

solve_1()
solve_2()