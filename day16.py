import heapq
import sys

def read_input():
    reinder_map = []
    with open("./day16_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for i,line in enumerate(lines):
            if 'S' in line:
                start = (i, line.index('S'), 1)
            if 'E' in line:
                end = (i, line.index('E'))
            reinder_map.append(list(line.strip()))

    return reinder_map, start, end

def solve_1():
    reinder_map, start, end = read_input()
    best,path = dijkstra(reinder_map, start, end)
    print(best)

def solve_2():
    reinder_map, start, end = read_input()
    best,path = dijkstra(reinder_map, start, end)
    print(len(path))

def dijkstra(reinder_map, start, end):
    distances = {}
    prev = {}
    for i,row in enumerate(reinder_map):
        for j,col in enumerate(row):
            for direction in range(4):
                distances[(i,j,direction)] = sys.maxsize
                prev[(i,j,direction)] = []

    distances[start] = 0


    visited = set()
    queue = []
    heapq.heappush(queue, (0, start))

    while len(queue) > 0:
        priority, current = heapq.heappop(queue)
        if current in visited:
            continue

        visited.add(current)

        for action in range(3):
            next = get_next(current, action)
            next_tile = reinder_map[next[0]][next[1]]
            if next_tile == '#':
                continue

            tentative_distance = distances[current] + (1 if action == 0 else 1000)
            if tentative_distance <= distances[next]:
               distances[next] = tentative_distance
               prev[next].append(current)
            heapq.heappush(queue, (distances[next], next))

    minEnd = sys.maxsize
    for i in range(4):
        a = distances[(end[0],end[1],i)]
        if a < minEnd:
            minEnd = a
            minEndDirection = i

    curr_path = [(end[0],end[1],minEndDirection)]
    path = []
    path.append((end[0],end[1]))
    while len(curr_path) > 0:
        curr = curr_path.pop()
        if curr == start:
            continue
        for p in prev[curr]:
            path.append((p[0],p[1]))
            curr_path.append(p)

    s = set()
    for p in path:
        s.add((p[0],p[1]))

    return minEnd, s
                    
def get_next(current, action):
    y,x,direction = current

    if action == 0:
        if direction == 0:
            return (y-1,x,direction)
        elif direction == 1:
            return (y,x+1,direction)
        elif direction == 2:
            return (y+1,x,direction)
        elif direction == 3:
            return (y,x-1,direction)
    elif action == 1:
        return (y,x,(direction-1) % 4)
    elif action == 2:
        return (y,x,(direction+1) % 4)



solve_1()
solve_2()