import random
import re


class GraphMatrix:

    def __init__(self, vertex):
        self.vertex = vertex
        self.matrix = []
        for i in range(self.vertex):
            self.matrix.append([])
            for j in range(self.vertex):
                self.matrix[i].append(0)

    def __str__(self):
        out = ""
        for i in range(len(self.matrix)):
            pom = ""
            for j in range(len(self.matrix)):
                pom = pom + str(self.matrix[i][j]) + " "
            out = out + "\n" + pom
        return out

    def clear(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                self.matrix[i][j] = 0

    def randomFill(self, density):
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

    def fromFile(self, fileName):
        self.clear()
        file = open(fileName, "r")
        input = file.read()
        vertex = re.findall(r"\d+", input)
        for i in range(0, len(vertex), 2):
            predecessor = int(vertex[i])
            successor = int(vertex[i+1])
            self.matrix[predecessor][successor] = 1

    def start(self):
        for i in range(len(self.matrix)):
            full = 1
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == 1:
                    full = 0
                    break
            if full == 1:
                return i

    def _TS(self, visited, sort, currentVertex): 
        visited[currentVertex] = 1
        for i in range(self.vertex):
            if visited[i] == 0 and self.matrix[currentVertex][i] != 0:
                self._TS(visited, sort, i)
        sort.insert(0, currentVertex)

    def TS(self):
        start = self.start()
        visited = [0] * self.vertex
        sort = []
        self._TS(visited, sort, start)
        return sort


graphM = GraphMatrix(10)
graphM.randomFill(70)
graphM.fromFile("data.txt")
print(graphM)
print(graphM.TS())
