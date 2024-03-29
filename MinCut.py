import sys
from BFS import BFS
from Environment import Graph

# Global Variables
results = []


def MinCut(graph, s, terminal, search):
    global results
    parent = [-1] * graph.row

    maxFlow = 0

    while search.bfs(graph.graph, s, terminal, parent):
        t = terminal
        path = float('inf')
        while t != s:
            t_ = parent[t]
            path = min(path, graph.graph[t_][t])
            t = parent[t]

        maxFlow += path
        v = terminal

        while v != s:
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


def corteST(results):
    val = float('inf')
    id_ = 0
    for idx, answer in enumerate(results):
        if answer[2] < val and answer[0] != []:
            val = answer[2]
            id_ = idx
    return results[id_]


def getSet(final_result, graph):
    list_of_v = []
    for i in range(graph.row):
        val = 0
        for j in range(graph.column):
            val += graph.graph_[i][j]
        if val == final_result[2]:
            list_of_v.append(i)
    return list_of_v


def write_output(length, set, max_flow, file):
    set_ = ' '.join(map(str, set))
    with open(str(file), 'w') as f:
        f.write(str(length)+' \n')
        f.write(str(set_) + ' \n')
        f.write(str(max_flow) +' \n')
        f.write('\n')
    f.close()


def main():
    global results
    input = sys.argv[1]
    output = sys.argv[2]
    world = Graph(str(input))
    for sink in world.sink:
        answer = MinCut(world, world.source, sink, BFS())
        results.append(answer)
        world.reset()
    final_result = corteST(results)
    vs = getSet(final_result, world)
    if len(vs) == 0 or len(vs) == world.vertex:
      vs = set(dict.fromkeys(final_result[1]))
    comprimento_s = len(vs)
    write_output(comprimento_s, vs, final_result[2], output)


if __name__ == '__main__':
    main()
