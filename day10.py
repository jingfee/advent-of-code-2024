def read_input():
    topography = []
    trailHeads = []
    with open("./day10_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for i, line in enumerate(lines):
            row = list(map(lambda l: int(l), list(line.strip())))
            topography.append(row)
            for j, c in enumerate(row):
                if c == 0:
                    trailHeads.append((i, j))
    return topography, trailHeads

def solve_1():
    topography, trailHeads = read_input()
    score = 0
    for head in trailHeads:
        head_score, head_rating = get_head_score_rating(topography, head)
        score += head_score
    print(score)

def solve_2():
    topography, trailHeads = read_input()
    rating = 0
    for head in trailHeads:
        head_score, head_rating = get_head_score_rating(topography, head)
        rating += head_rating
    print(rating)

def get_head_score_rating(topography, head):
    peaks = set()
    rating = 0
    queue = [head]
    while len(queue) > 0:
        currCoordinate = queue.pop()
        curr = topography[currCoordinate[0]][currCoordinate[1]]
        if curr == 9:
            rating += 1
            peaks.add(currCoordinate)
        else:
            nextCoordinates = []
            #up
            if currCoordinate[0] > 0:
                nextCoordinates.append((currCoordinate[0] - 1, currCoordinate[1]))
            #right
            if currCoordinate[1] < len(topography[0]) - 1:
                nextCoordinates.append((currCoordinate[0], currCoordinate[1] + 1))
            #down
            if currCoordinate[0] < len(topography) - 1:
                nextCoordinates.append((currCoordinate[0] + 1, currCoordinate[1]))
            #left
            if currCoordinate[1] > 0:
                nextCoordinates.append((currCoordinate[0], currCoordinate[1] - 1))

            for nextCoordinate in nextCoordinates:
                if topography[nextCoordinate[0]][nextCoordinate[1]] == (curr + 1):
                    queue.append(nextCoordinate)

    return len(peaks), rating

solve_1()
solve_2()