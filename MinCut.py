from BFS import BFS
from Environment import Graph

import sys, time

results = []


def MinCut(graph, source, terminal, search):
    global results
    parent = [-1] * graph.row

    maxFlow = 0

    while search.bfs(graph.graph, source, terminal, parent):
        s = terminal
        path = float('inf')

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
    # print(graph.graph)
    # print(graph.graph_)
    j_list = list()
    i_list = list()
    for i in range(graph.row):
        for j in range(graph.column):
            if graph.graph[i][j] == 0 and graph.graph_[i][j] > 0:
                i_list.append(i)
                j_list.append(j)


    # print("S': ", j_list)
    # print('Max Flow: ', maxFlow)
                # print(str(i) + " -", str(j), ' Max Flow: ', maxFlow)

    return i_list, j_list, maxFlow


def corteST(results, world):

    for answer in results:
        ans = answer
        L = [False] * world.vertex
        for element in answer[0]:
            if element in world.vertex_list:
                L[element] = True
            for element_ in answer[1]:
                if element in world.vertex_list:
                    L[element_] = True

        if all(element for element in L):
            break
    return ans


def main():
    results = []
    init = time.time()
    try:
        file = sys.argv[1]
    except:
        file = str('entrada_1')
    world = Graph(str(file))
    search = BFS()
    source = world.source
    terminal = world.sink
    for sink in terminal:
        # print('Source: ', source, 'Sink: ', sink)
        # print('----------------------------------')

        # source = 0
        # terminal = 1
        answer = MinCut(world, source, sink, search)
        results.append(answer)
        world.reset()
    final_result = corteST(results, world)
    print('Qty Vertices: ', len(list(dict.fromkeys(final_result[0]))))
    print('Conjunto S:', list(dict.fromkeys(final_result[0])))
    print('Conjunto S":', list(dict.fromkeys(final_result[1])))
    print('Max-Flow: ', final_result[-1])
    print('Time: ', time.time() - init)

if __name__ == '__main__':
    main()