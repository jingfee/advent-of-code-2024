from math import floor

def read_input():
    ordering = {}
    pages = []
    with open("./day5_input.txt", "r", encoding="utf-8") as input:
        reading_order = True
        for line in input:
            if line == '\n':
                reading_order = False
            elif reading_order:
                split = line.split('|')
                if not(split[0] in ordering):
                    ordering[split[0]] = []
                ordering[split[0]].append(split[1].strip())
            else:
                pages.append(list(map(lambda s: s.strip(), line.split(','))))
    return (ordering, pages)

def solve_1():
    sum = 0
    ordering, pages = read_input()
    for p in pages:
        sum += correct(ordering, p)
    print(sum)

def solve_2():
    sum = 0
    ordering, pages = read_input()
    for p in pages:
        page = correct(ordering, p)
        if page > 0:
            continue
        else:
            sum += reorder(ordering, p)
    print(sum)

def correct(ordering, pages):
    for i, e in reversed(list(enumerate(pages))):
        if not(e in ordering):
            continue
        order = ordering[e]
        for j in range(i):
            if pages[j] in order:
                return 0
    return int(pages[floor(len(pages)/2)])

def reorder(ordering, pages):
    newOrder = {}
    for i, e in enumerate(pages):
        if not(e in ordering):
            newOrder[len(pages)-1]=e
            continue
        order = ordering[e]
        count = 0
        for j in range(len(pages)):
            if pages[j] in order:
                count += 1
        newOrder[len(pages) - 1 - count] = e
    return int(newOrder[floor(len(newOrder)/2)])


solve_1()
solve_2()