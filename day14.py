from math import ceil, floor
import os
import re
import time

width = 101
height = 103

def read_input():
    robots = []
    with open("./day14_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for line in lines:
            a = re.search('p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
            robots.append((int(a.group(1)),int(a.group(2)),int(a.group(3)),int(a.group(4))))

    return robots

def solve_1():
    robots = read_input()
    robot_map = set_init(robots)

    for i in range(100):
        robot_map = move_robots(robot_map)
    
    s = safety_factor(robot_map)
    print(s)

def solve_2():
    robots = read_input()
    robot_map = set_init(robots)

    for i in range(100000):
        robot_map = move_robots(robot_map)
        print_robot(robot_map, i)
        time.sleep(0.5)    


def set_init(robots):
    robot_map = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append([])
        robot_map.append(row)

    for robot in robots:
        px,py,_,_ = robot
        robot_map[py][px].append(robot)
    return robot_map

def move_robots(robot_map):
    new_map = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append([])
        new_map.append(row)
    
    for i in range(height):
        for j in range(width):
            robots = robot_map[i][j]
            for robot in robots:
                _,_,vx,vy = robot
                new_map[(i+vy)%height][(j+vx)%width].append(robot)
    
    return new_map

def safety_factor(robot_map):
    quadrants = [list(map(lambda a: a[:floor(width/2)], robot_map[:floor(height/2)])),
               list(map(lambda a: a[ceil(width/2):], robot_map[:floor(height/2)])),
               list(map(lambda a: a[:floor(width/2)], robot_map[ceil(height/2):])),
               list(map(lambda a: a[ceil(width/2):], robot_map[ceil(height/2):]))]

    safety_factor = 1
    for quadrant in quadrants:
        sum = 0
        for row in quadrant:
            for cell in row:
                 sum += len(cell)
        safety_factor *= sum
    return safety_factor

def print_robot(robot_map, index):
    os.system('clear')
    print(index)
    for row in robot_map:
        string = ''
        for cell in row:
            if len(cell) > 0:
                string += '#'
            else:
                string += ' '
        print(string)



solve_1()
solve_2()