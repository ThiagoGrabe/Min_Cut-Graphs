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
            direita = []
            esquerda = []
            for line in self.initial_config:
                self.graph[line[0]][line[1]] = int(line[2])
                esquerda.append(line[0])
                direita.append(line[1])
            r = self.getUnique(esquerda, direita)
            self.source, self.sink = r[0][0], r[1][-1]
            # self.sink = self.getUnique(direita)[0]

            self.graph_ = [i[:] for i in self.graph]

            self.vertex_list = [i for i in range(self.vertex)]
            # self.source = 0
            # self.sink = [i for i in range(self.vertex)]
            # self.sink.remove(self.source)
            self.row, self.column = len(self.graph), len(self.graph[0])

    def getUnique(self, source, tink):
        s = set(dict.fromkeys(source))
        t = set(dict.fromkeys(tink))

        s_ = list(s.symmetric_difference(t))
        t_ = list(t.symmetric_difference(s))



        return s_, t_


        # self.unique_list = []
        # for x in list:
        #     if x not in self.unique_list:
        #         self.unique_list.append(x)
        # return self.unique_list

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

    # def source_sink(self):
    #
    #     self.source_ = [i[:] for i in self.vertex_list]
    #     self.source = random.randrange(self.source_)
    #     self.sink.remove(self.source)
    #
    #     self.source_.remove(self.source)