import random
import re


class GraphList:
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

    def randomFill(self, density):
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

    def fromFile(self, fileName):
        self.clear()
        file = open(fileName, "r")
        input = file.read()
        vertex = re.findall(r"\d+", input)
        for i in range(0, len(vertex), 2):
            predecessor = int(vertex[i])
            successor = int(vertex[i+1])
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

    def __TS(self, visited, sort, vertex):  # Topological Sort
        visited[vertex] = 1
        for i in range(len(self.list[vertex])):
            if visited[self.list[vertex][i]] == 0:
                self._TS(visited, sort, self.list[vertex][i])
        sort.insert(0, vertex)

    def TS(self):
        start = self.start()
        visited = [0] * self.vertex
        sort = []
        self._TS(visited, sort, start)
        return sort


graphL = GraphList(10)
graphL.randomFill(70)
graphL.fromFile("TopologicalSortData.txt")
print(graphL)
print(graphL.TS())
