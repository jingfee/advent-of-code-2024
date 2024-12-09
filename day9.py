from math import floor


def read_input():
    disk = []
    files = {}
    empty = {}
    with open("./day9_input.txt", "r", encoding="utf-8") as input:
        line = input.readline()
        for i,c in enumerate(line):
            if i%2 == 0:
                id = floor(i/2)
                for a in range(int(c)):
                    disk.append(id)
                files[id] = int(c)
            else:
                empty[len(disk)] = int(c)
                for a in range(int(c)):
                    disk.append(None)      
    return disk, files, empty

def solve_1():
    disk, files, empty = read_input()

    for i, a in enumerate(disk):
        if a is None:
            last = last_file_index(disk)
            if last < i:
                break
            disk[i] = disk[last]
            disk[last] = None

    print(checksum(disk))

def solve_2():
    disk, files, empty = read_input()

    i = len(disk) - 1
    moved = set()
    while i >= 0:
        a = disk[i]
        if a is not None:
            file_length = files[a]
            empty_index = None
            for b in sorted(empty):
                if empty[b] >= file_length:
                    empty_index = b
                    break
            if empty_index is not None and a not in moved and empty_index < i - file_length:
                for c in range(file_length):
                    disk[empty_index + c] = a
                    disk[i - c] = None
                if(empty[empty_index] > file_length):
                    empty[empty_index + file_length] = empty[empty_index] - file_length
                empty.pop(empty_index)
                moved.add(a)
            i -= file_length
        else:
            i -= 1
            
    print(checksum(disk))

def last_file_index(disk):
    for i, a in reversed(list(enumerate(disk))):
        if a is not None:
            return i
    return None

def checksum(disk):
    checksum = 0
    for i,a in enumerate(disk):
        if a is None:
            continue
        checksum += i*a
    return checksum

solve_1()
solve_2()