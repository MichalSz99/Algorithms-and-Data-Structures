import random
import re


class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.matrix = []
        for i in range(self.vertex):
            self.matrix.append([])
            for j in range(self.vertex):
                self.matrix[i].append(0)

    def __str__(self):
        out = ""
        for i in range(self.vertex):
            pom = ""
            for j in range(self.vertex):
                pom = pom + str(self.matrix[i][j]) + " "
            out = out + "\n" + pom
        return out

    def clear(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                self.matrix[i][j] = 0

    def random_fill(self, density):
        self.clear()
        for i in range(self.vertex):
            for j in range(i + 1, self.vertex):
                if j == i + 1 or (random.random() + 2 / self.vertex) < (density / 100):
                    self.matrix[i][j] = 1
        for i in range(self.vertex):
            x = random.randint(0, self.vertex - 1)
            y = random.randint(0, self.vertex - 1)
            if x != y:
                self.matrix[x], self.matrix[y] = self.matrix[y], self.matrix[x]
                for j in range(self.vertex):
                    self.matrix[j][x], self.matrix[j][y] = self.matrix[j][y], self.matrix[j][x]

    def from_file(self, file_name):
        self.clear()
        file = open(file_name, "r")
        input_data = file.read()
        data = re.findall(r"\d+", input_data)
        for i in range(0, len(data), 2):
            predecessor = int(data[i])
            successor = int(data[i+1])
            self.matrix[predecessor][successor] = 1

    def __start(self):
        for i in range(len(self.matrix)):
            full = True
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == 1:
                    full = False
                    break
            if full:
                return i

    def __ts(self, visited, sort, current_vertex):
        visited[current_vertex] = 1
        for i in range(self.vertex):
            if visited[i] == 0 and self.matrix[current_vertex][i] != 0:
                self.__ts(visited, sort, i)
        sort.insert(0, current_vertex)

    def ts(self):
        start = self.__start()
        visited = [0] * self.vertex
        sort = []
        self.__ts(visited, sort, start)
        return sort


graph = Graph(10)
graph.random_fill(70)
print(graph)
print(graph.ts())
graph.from_file("TopologicalSortData.txt")
print(graph)
print(graph.ts())
