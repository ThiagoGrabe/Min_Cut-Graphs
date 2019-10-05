class BFS:

    def bfs(self, graph, source, terminal, family):

        seen = [False] * len(graph)
        fifo = []
        fifo.append(source)
        seen[source] = True

        while fifo:
            vertex = fifo.pop(0)

            for idx, value in enumerate(graph[vertex]):
                if value > 0 and seen[idx] == False:
                    fifo.append(idx)
                    seen[idx] = True
                    family[idx] = vertex
        if seen[terminal]:
            return True
        else:
            return False
