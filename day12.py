def read_input():
    garden = []
    with open("./day12_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for line in lines:
            garden.append(list(line.strip()))
    return garden

def solve_1():
    garden = read_input()
    plots = get_plots(garden)
    price = 0
    for plot in plots:
        price += len(plot[0]) * plot[1]
    print(price)

def solve_2():
    garden = read_input()
    plots = get_plots(garden)
    price = 0
    for plot in plots:
        sides = 0
        for edge in plot[0]:
            plant = garden[edge[0]][edge[1]]
            #outer corner
            #top left
            if (edge[0] == 0 or garden[edge[0]-1][edge[1]] != plant) and (edge[1] == 0 or garden[edge[0]][edge[1]-1] != plant):
                sides += 1
            #top right
            if (edge[0] == 0 or garden[edge[0]-1][edge[1]] != plant) and (edge[1] == len(garden[0]) - 1 or garden[edge[0]][edge[1]+1] != plant):
                sides += 1
            #bottom right
            if (edge[0] == len(garden) - 1 or garden[edge[0]+1][edge[1]] != plant) and (edge[1] == len(garden[0]) - 1 or garden[edge[0]][edge[1]+1] != plant):
                sides += 1
            #bottom left
            if (edge[0] == len(garden) - 1 or garden[edge[0]+1][edge[1]] != plant) and (edge[1] == 0 or garden[edge[0]][edge[1]-1] != plant):
                sides += 1

            #inner corner
            #bottom right
            if edge[0] > 0 and edge[1] > 0 and garden[edge[0]-1][edge[1]] == plant and garden[edge[0]][edge[1]-1] == plant and garden[edge[0]-1][edge[1]-1] != plant:
                sides += 1
            #bottom left
            if edge[0] > 0 and edge[1] < len(garden[0]) - 1 and garden[edge[0]-1][edge[1]] == plant and garden[edge[0]][edge[1]+1] == plant and garden[edge[0]-1][edge[1]+1] != plant:
                sides += 1
            #top left
            if edge[0] < len(garden) - 1 and edge[1] < len(garden[0]) - 1 and garden[edge[0]+1][edge[1]] == plant and garden[edge[0]][edge[1]+1] == plant and garden[edge[0]+1][edge[1]+1] != plant:
                sides += 1
            #top right
            if edge[0] < len(garden) - 1 and edge[1] > 0 and garden[edge[0]+1][edge[1]] == plant and garden[edge[0]][edge[1]-1] == plant and garden[edge[0]+1][edge[1]-1] != plant:
                sides += 1

        price += len(plot[0]) * sides
    print(price)


def get_plots(garden):
    assigned_plants = set()
    plots = []
    for (i, row) in enumerate(garden):
        for (j, plant) in enumerate(row):
            if (i, j) in assigned_plants:
                continue

            queue = [(i,j)]
            plot = []
            perimeter = 0
            while len(queue) > 0:
                curr = queue.pop()
                if(curr in assigned_plants):
                    continue
                assigned_plants.add(curr)
                plot.append(curr)
                curr_plant = garden[curr[0]][curr[1]]
                add_perimeter = 4

                if curr[0] > 0 and garden[curr[0]-1][curr[1]] == curr_plant:
                    queue.append((curr[0]-1, curr[1]))
                    add_perimeter -= 1
                if curr[1] < len(garden[0]) - 1 and garden[curr[0]][curr[1]+1] == curr_plant:
                    queue.append((curr[0], curr[1]+1))
                    add_perimeter -= 1
                if curr[0] < len(garden) - 1 and garden[curr[0]+1][curr[1]] == curr_plant:
                    queue.append((curr[0]+1, curr[1]))
                    add_perimeter -= 1
                if curr[1] > 0 and garden[curr[0]][curr[1]-1] == curr_plant:
                    queue.append((curr[0], curr[1]-1))
                    add_perimeter -= 1
            
                perimeter += add_perimeter
            
            plots.append((plot, perimeter))
    return plots

solve_1()
solve_2()