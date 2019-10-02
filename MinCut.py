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
    # print(graph.graph)
    # print(graph.graph_)
    j_list = list()
    i_list = list()
    for i in range(graph.row):
        for j in range(graph.column):
            if graph.graph[i][j] == 0 and graph.graph_[i][j] > 0:
                # getNeibours(graph, i, j)
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

# def getNeibours(graph, i, j):



def corteST(results, world):
    val = float('inf')
    for idx, answer in enumerate(results):
        if answer[2] < val and answer[0] != []:
            val = answer[2]
            id_ = idx
    return results[id_]

    # for answer in results:
    #     L = list(dict.fromkeys(answer[0]+answer[1]))
    #     a = world.vertex_list
    #     b = answer[2]
    #     res = all(elem in L for elem in world.vertex_list)
    #     if res:
    #         return answer
    #     else:
    #         continue

        # ans = answer
        # L = [False] * world.vertex
    #     for element in answer[0]:
    #         if element in world.vertex_list:
    #             L[element] = True
    #         for element_ in answer[1]:
    #             if element in world.vertex_list:
    #                 L[element_] = True
    #
    #     if all(element for element in L):
    #         break
    # return ans


def main():
    results = []
    init = time.time()
    try:
        file = sys.argv[1]
    except:
        file = str('4.in')
    world = Graph(str(file))
    search = BFS()
    source = world.source
    terminal = world.sink
    # world.source_sink()
    # for source in world.source_:
    for sink in terminal:
        print('Source: ', source, 'Sink: ', sink)
        print('----------------------------------')

    # source = 0
    # terminal = 1
        answer = MinCut(world, source, sink, search)

        results.append(answer)
        world.reset()
    final_result = corteST(results, world)
    # print(final_result)
    # if final_result is None:
    #     for weight in results:
    #         idx, val = 0, float('inf')
    #         if weight[2] < val:
    #             final_result = weight
    #             val = weight[2]
    #         idx += 1
    # print(results)
    # S = set(list(dict.fromkeys(final_result[0])))
    # S_ = set(list(dict.fromkeys(final_result[1])))
    S = final_result[0]
    S_ = final_result[1]
    # t = S - S_

    # print('Qty Vertices: ', len(S))
    # print('Conjunto S:', S)
    print('Qty Vertices: ', len(list(dict.fromkeys(S_))))
    print('Conjunto S:', list(dict.fromkeys(S_)))
    print('Sum cut weights: ', final_result[-1])
    print('Time: ', time.time() - init)


if __name__ == '__main__':
    main()