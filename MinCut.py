import sys
import time

from BFS import BFS
from Environment import Graph

# Global Variables
results = []


def MinCut(graph, source, terminal, search):
    global results
    parent = [-1] * graph.row

    maxFlow = 0

    while search.bfs(graph.graph, source, terminal, parent):
        t = terminal
        path = float('inf')

        while t != source:
            path = min(path, graph.graph[parent[t]][t])
            t = parent[t]

        maxFlow += path
        v = terminal

        while v != source:
            u = parent[v]
            graph.graph[u][v] -= path
            graph.graph[v][u] += path
            v = parent[v]
    j_list = list()
    i_list = list()
    for i in range(graph.row):
        for j in range(graph.column):
            if graph.graph[i][j] == 0 and graph.graph_[i][j] > 0:
                i_list.append(i)
                j_list.append(j)
    # print(i_list, '_', j_list)

    # print("S: ", (i_list))
    # print("S': ", (j_list))
    # print("S: ", list(dict.fromkeys(i_list)))
    # print("S': ", list(dict.fromkeys(j_list)))
    # print('Max Flow: ', maxFlow)
    # print('------------------')

    return i_list, j_list, maxFlow


def corteST(results, world):
    val = float('inf')
    for idx, answer in enumerate(results):
        if answer[2] < val and answer[0] != []:
            val = answer[2]
            id_ = idx
    return results[id_]


def main():
    results = []
    init = time.time()
    try:
        file = sys.argv[1]
    except:
        file = str('11.in')
    world = Graph(str(file))
    for sink in world.sink:
        answer = MinCut(world, world.source, sink, BFS())
        results.append(answer)
        world.reset()
    final_result = corteST(results, world)
    S = final_result[0]
    S_ = final_result[1]
    print('Qty Vertices: ', len(list(dict.fromkeys(S_))))
    print('Conjunto S:', list(dict.fromkeys(S_)))
    print('Conjunt -S ', list(dict.fromkeys(S)))
    print('Sum cut weights: ', final_result[-1])
    print('Time: ', time.time() - init)


if __name__ == '__main__':
    main()