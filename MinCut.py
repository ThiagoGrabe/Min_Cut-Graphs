import sys
import time
import os

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
    j_list = []
    i_list = []
    for i in range(graph.row):
        for j in range(graph.column):
            if graph.graph_[i][j] > 0 and graph.graph[i][j] == 0:
                i_list.append(i)
                j_list.append(j)
    return i_list, j_list, maxFlow


def corteST(results, world):
    val = float('inf')
    id_ = 0
    for idx, answer in enumerate(results):
        if answer[2] < val and answer[0] != []:
            val = answer[2]
            id_ = idx
    return results[id_]


def write_output(length, set, max_flow, file):
    set_ = ' '.join(map(str, set))
    with open(str(file), 'w') as f:
        f.write(str(length)+' \n')
        f.write(str(set_) + ' \n')
        f.write(str(max_flow) +' \n')
        f.write('\n')
    f.close()


def main():
    init = time.time()
    global results
    try:
        input = sys.argv[1]
        output = sys.argv[2]
    except:
        input = str('9.in')
        output = os.getcwd()+(str('/out/output_')+input)
    world = Graph(str(input))
    for sink in world.sink:
        answer = MinCut(world, world.source, sink, BFS())
        results.append(answer)
        world.reset()
    final_result = corteST(results, world)
    set_S = set(dict.fromkeys(final_result[0]))
    set_comp_S = set(dict.fromkeys(final_result[1]))
    # print('Total de vertices: ', world.vertex)
    # print('Faz sentido: ', len(world.vertex_list) - len(set_comp_S))
    # print('---------------------')
    comprimento_s = len(set_comp_S)
    print('Qty Vertices: ', comprimento_s)
    # print('Conjunto S:', set_S)
    print('Conjunt -S ', set_comp_S)
    print('Sum cut weights: ', final_result[2])
    # print(set(dict.fromkeys(final_result[3])))
    instance_time = time.time() - init
    print('Time: ', instance_time)
    # write_output(comprimento_s, list(set_comp_S), final_result[2], output)


if __name__ == '__main__':
    main()