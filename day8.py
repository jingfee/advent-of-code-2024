def read_input():
    antennas = {}
    with open("./day8_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        boundY = len(lines)
        boundX = len(lines[0].strip())
        for i, line in enumerate(lines):
            for j, char in enumerate(line.strip()):
                if char != '.':
                    if char not in antennas:
                        antennas[char] = [(i, j)]
                    else:
                        a = antennas.get(char)
                        a.append((i, j))
                        antennas[char] = a
    return antennas, (boundY, boundX)

def solve_1():
    antennas, bounds = read_input()
    antinodes = set()
    for antenna in antennas:
        for first in antennas[antenna]:
            for second in antennas[antenna]:
                if first == second:
                    continue

                distY = first[0] - second[0]
                distX = first[1] - second[1]

                antinode_1 = (first[0] + distY, first[1] + distX)
                antinode_2 = (second[0] - distY, second[1] - distX)

                if antinode_1[0] >= 0 and antinode_1[0] < bounds[0] and antinode_1[1] >= 0 and antinode_1[1] < bounds[1]:
                    antinodes.add(antinode_1)
                if antinode_2[0] >= 0 and antinode_2[0] < bounds[0] and antinode_2[1] >= 0 and antinode_2[1] < bounds[1]:
                    antinodes.add(antinode_2)
    
    print(len(antinodes))

def solve_2():
    antennas, bounds = read_input()
    antinodes = set()
    for antenna in antennas:
        for first in antennas[antenna]:
            for second in antennas[antenna]:
                if first == second:
                    continue

                distY = first[0] - second[0]
                distX = first[1] - second[1]

                count = 0
                while True:
                    antinode = (first[0] + count*distY, first[1] + count*distX)
                    if antinode[0] >= 0 and antinode[0] < bounds[0] and antinode[1] >= 0 and antinode[1] < bounds[1]:
                        antinodes.add(antinode)
                        count += 1
                    else:
                        break

                count = 0
                while True:
                    antinode = (second[0] - count*distY, second[1] - count*distX)
                    if antinode[0] >= 0 and antinode[0] < bounds[0] and antinode[1] >= 0 and antinode[1] < bounds[1]:
                        antinodes.add(antinode)
                        count += 1
                    else:
                        break
    
    print(len(antinodes))

solve_1()
solve_2()