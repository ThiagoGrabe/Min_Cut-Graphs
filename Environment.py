class Graph:

    def __init__(self, entry):
        self.entry = str(entry)
        self.vertex = None
        self.edges = None
        self.graph = None
        self.sink = None

        with open(str(self.entry)) as file:
            self.load = [[int(num) for num in line.split()] for line in file]

            self.vertex = self.load[0][0]
            self.row = self.load[0][0]
            self.column = self.load[0][0]
            self.edges = self.load[0][1]
            self.initial_config = self.load[1:]
            # self.vertex_list = [i for i in range(self.vertex)]

            # Initialize graph
            self.graph = [[0 for x in range(self.vertex)] for y in range(self.vertex)]

            # Edges values
            for line in self.initial_config:
                self.graph[line[0]][line[1]] = int(line[2])
                self.graph[line[1]][line[0]] = int(line[2])
            self.source = 0
            self.sink = [i for i in range(1, self.vertex)]
            # self.sink.remove(self.source)

            self.graph_ = [i[:] for i in self.graph]
            self.base = [i[:] for i in self.graph]

    def reset(self):
        self.graph = [i[:] for i in self.base]
