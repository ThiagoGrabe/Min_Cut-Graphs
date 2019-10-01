from BFS import BFS
from Environment import Graph

import sys, time

path = float('inf')
results = []


def MinCut(graph, source, terminal, search):
    global path, results
    parent = [-1] * graph.row

    maxFlow = 0

    while search.bfs(graph.graph, source, terminal, parent):
        s = terminal

        while s != source:
            path = min(path, graph.graph[parent[s]][s])
            s = parent[s]

        maxFlow += path
        v = terminal

        while v != source:
            u = parent[v]
            graph.graph[u][v] -= path
            graph.graph[v][u] += path
            v = parent[v]

    for i in range(graph.row):
        for j in range(graph.column):
            if graph.graph[i][j] == 0 and graph.graph_[i][j] > 0:
                print(str(i) + " -", str(j), ' Max Flow: ', maxFlow)


def main():
    init = time.time()
    try:
        file = sys.argv[1]
    except:
        file = str('entrada_3')
    world = Graph(str(file))
    search = BFS()
    source = world.source
    terminal = world.sink
    for sink in terminal:
        print('Source: ', source, 'Sink: ', sink)
        print('----------------------------------')

        # source = 0
        # terminal = 1
        MinCut(world, source, sink, search)
        world.reset()
        print('\n')


if __name__ == '__main__':
    main()