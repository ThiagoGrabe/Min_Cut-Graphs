def bfs(graph, source, terminal, family):

    seen = [False] * len(graph)
    fifo = list()
    fifo.append(source)
    seen[source] = True

    while fifo:
        u = fifo.pop(0)

        for idx, value in enumerate(graph[u]):
            if seen[idx] == False and value > 0:
                fifo.append(idx)
                seen[idx] = True
                family[idx] = u
    return True if seen[terminal] else False