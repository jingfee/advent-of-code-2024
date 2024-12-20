import heapq
import sys

num_bytes = 12
space = 6


def read_input():
    bytes = []
    with open("./day18_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for line in lines:
            split = line.strip().split(',')
            bytes.append((int(split[0]), int(split[1])))

    return bytes

def solve_1():
    bytes = read_input()
    bytes = bytes[:num_bytes]
    byte_map = []
    for i in range(space+1):
        row = []
        for j in range(space+1):
            try:
                index = bytes.index((j,i))
            except ValueError:
                index = -1
            if index == -1:
                row.append('.')
            else:
                row.append('#')
        byte_map.append(row)

    min = dijkstra(byte_map, (0,0), (space,space))

    print(min)

def solve_2():
    bytes = read_input()
    for n in range(num_bytes, len(bytes)):
        new_bytes = bytes[:n]
        byte_map = []
        for i in range(space+1):
            row = []
            for j in range(space+1):
                try:
                    index = new_bytes.index((j,i))
                except ValueError:
                    index = -1
                if index == -1:
                    row.append('.')
                else:
                    row.append('#')
            byte_map.append(row)

        min = dijkstra(byte_map, (0,0), (space,space))
        if min == sys.maxsize:
            print(bytes[n-1])
            break

def dijkstra(byte_map, start, end):
    distances = {}
    for i,row in enumerate(byte_map):
        for j,col in enumerate(row):
            distances[(i,j)] = sys.maxsize

    distances[start] = 0

    visited = set()
    queue = []
    heapq.heappush(queue, (0, start))

    while len(queue) > 0:
        priority, current = heapq.heappop(queue)
        if current in visited:
            continue

        visited.add(current)

        neighbors = []
        if current[0] > 0 and byte_map[current[0] - 1][current[1]] == '.':
            neighbors.append((current[0] - 1, current[1]))
        if current[1] < space and byte_map[current[0]][current[1] + 1] == '.':
            neighbors.append((current[0], current[1] + 1))
        if current[0] < space and byte_map[current[0] + 1][current[1]] == '.':
            neighbors.append((current[0] + 1, current[1]))
        if current[1] > 0 and byte_map[current[0]][current[1] - 1] == '.':
            neighbors.append((current[0], current[1] - 1))

        for neighbor in neighbors:
            tentative_distance = distances[current] + 1
            if tentative_distance < distances[neighbor]:
               distances[neighbor] = tentative_distance
            heapq.heappush(queue, (distances[neighbor], neighbor))

    return distances[end]

solve_1()
solve_2()