import random
import re


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.list = []
        for i in range(self.vertex):
            self.list.append([])

    def __str__(self):
        out = ""
        for i in range(self.vertex):
            pom = str(i) + ":  "
            successor = len(self.list[i])
            for j in range(successor):
                pom = pom + str(self.list[i][j]) + " "
            out = out + "\n" + pom
        return out

    def clear(self):
        for i in range(self.vertex):
            self.list[i] = []

    def random_fill(self, density):
        self.clear()
        matrix = []
        for i in range(self.vertex):
            matrix.append([])
            for j in range(self.vertex):
                matrix[i].append(0)
        for i in range(self.vertex):
            for j in range(i + 1, self.vertex):
                if j == i + 1 or (random.random() + 2 / self.vertex) < (density / 100):
                    matrix[i][j] = 1
        for i in range(self.vertex):
            x = random.randint(0, self.vertex - 1)
            y = random.randint(0, self.vertex - 1)
            if x != y:
                matrix[x], matrix[y] = matrix[y], matrix[x]
                for j in range(self.vertex):
                    matrix[j][x], matrix[j][y] = matrix[j][y], matrix[j][x]
        for i in range(self.vertex):
            for j in range(self.vertex):
                if matrix[i][j] == 1:
                    self.list[i].append(j)

    def from_file(self, file_name):
        self.clear()
        file = open(file_name, "r")
        input_data = file.read()
        data = re.findall(r"\d+", input_data)
        for i in range(0, len(data), 2):
            predecessor = int(data[i])
            successor = int(data[i+1])
            self.list[predecessor].append(successor)

    def __start(self):
        for i in range(self.vertex):
            full = True
            for j in range(self.vertex):
                if i in self.list[j]:
                    full = False
                    break
            if full:
                return i

    def __ts(self, visited, sort, vertex):
        visited[vertex] = 1
        for i in range(len(self.list[vertex])):
            if visited[self.list[vertex][i]] == 0:
                self.__ts(visited, sort, self.list[vertex][i])
        sort.insert(0, vertex)

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
