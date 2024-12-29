from math import floor


def read_input():
    connections = {}
    with open("./day23_input.txt", "r", encoding="utf-8") as input:
        lines = input.readlines()
        for line in lines:
            split = line.strip().split('-')
            if split[0] in connections:
                connections[split[0]].append(split[1])
            else:
                connections[split[0]] = [split[1]]
            if split[1] in connections:
                connections[split[1]].append(split[0])
            else:
                connections[split[1]] = [split[0]]
    return connections

def solve_1():
    connections = read_input()
    interconnected = set()
    for computer_1 in connections:
        if not computer_1[0] == 't':
            continue

        computers_2 = connections[computer_1]
        for i in range(len(computers_2)):
            for j in range(i+1, len(computers_2)):
                if computers_2[i] in  connections[computers_2[j]]:
                    net = [computer_1, computers_2[i], computers_2[j]]
                    net.sort()
                    interconnected.add(tuple(net))
    print(len(interconnected))

def solve_2():
    connections = read_input()
    results = []
    bron_kerbosch(set(), set(connections.keys()), set(), connections, results)
    largest_clique = list(max(results, key=len))
    largest_clique.sort()
    print(','.join(largest_clique))

def bron_kerbosch(R, P, X, graph, results):
    if not P and not X:
        results.append(R)
        return
    for node in list(P):
        bron_kerbosch(R | {node}, 
                      P & set(graph[node]), 
                      X & set(graph[node]), 
                      graph, 
                      results)
        P.remove(node)
        X.add(node)


solve_1()
solve_2()