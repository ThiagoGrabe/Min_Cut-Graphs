class BFS:

    def bfs(self, graph, source, terminal, family):

        seen = [False] * len(graph)
        fifo = []
        fifo.append(source)
        seen[source] = True

        while fifo:
            u = fifo.pop(0)

            for idx, value in enumerate(graph[u]):
                if value > 0 and seen[idx] == False:
                    fifo.append(idx)
                    seen[idx] = True
                    family[idx] = u
        return True if seen[terminal] else False
