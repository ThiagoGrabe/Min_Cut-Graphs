import random

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
            self.edges = self.load[0][1]
            self.initial_config = self.load[1:]

            # Initialize graph
            self.graph = [[0 for x in range(self.vertex)] for y in range(self.vertex)]
            # Edges values
            for line in self.initial_config:
                self.graph[line[0]][line[1]] = int(line[2])

            self.graph_ = [i[:] for i in self.graph]

            self.vertex_list = [i for i in range(self.vertex)]
            self.sink = [i for i in range(self.vertex)]

            # self.source = random.randrange(self.vertex)
            self.source = 0
            self.sink.remove(self.source)

            self.row, self.column = len(self.graph), len(self.graph[0])

    def reset(self):
        with open(str(self.entry)) as file:
            self.load = [[int(num) for num in line.split()] for line in file]

            self.vertex = self.load[0][0]
            self.edges = self.load[0][1]
            self.initial_config = self.load[1:]

            # Initialize graph
            self.graph = [[0 for x in range(self.vertex)] for y in range(self.vertex)]
            # Edges values
            for line in self.initial_config:
                self.graph[line[0]][line[1]] = int(line[2])

            self.graph_ = [i[:] for i in self.graph]