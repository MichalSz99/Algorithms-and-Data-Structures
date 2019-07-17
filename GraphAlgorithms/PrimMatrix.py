import random
import re
import heapq


class Edge:
    def __init__(self, x, y, val):
        self.val = val
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        out = "[(" + str(self.x) + "," + str(self.y) + ");" + str(self.val) + "]"
        return out


class GraphM:

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
                pom = pom + '{:>4}'.format(str(self.matrix[i][j]) )+ " "
            out = out + "\n" + pom
        return out

    def clear(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                self.matrix[i][j] = 0

    def randomFill(self, density, valueMin, valueMax):
        self.clear()
        for i in range(self.vertex):
            for j in range(i + 1, self.vertex):
                if random.random() < (density / 100):
                    self.matrix[i][j] = random.randint(valueMin, valueMax)
                    self.matrix[j][i] = self.matrix[i][j]

    def fromFile(self, fileName):
        self.clear()
        file = open(fileName, "r")
        input = file.read()
        vertex = re.findall(r"\d+", input)
        for i in range(0, len(vertex), 3):
            predecessor = int(vertex[i])
            successor = int(vertex[i + 1])
            value = int(vertex[i + 2])
            self.matrix[predecessor][successor] = value
            self.matrix[successor][predecessor] = value

    def prim(self, start):
        listOfVertex = [False] * self.vertex
        listOfVertex[start] = True
        outEdge = []
        processedEdge = []
        for i in range(self.vertex):
            if self.matrix[start][i] != 0:
                heapq.heappush(processedEdge, Edge(start, i, self.matrix[start][i]))
        while len(outEdge) < self.vertex - 1:
            while processedEdge:
                E = heapq.heappop(processedEdge)
                if not (listOfVertex[E.y]):
                    break

            if not processedEdge:
                break

            listOfVertex[E.y] = True
            outEdge.append(E)

            for i in range(len(self.matrix)):
                if not (listOfVertex[i]) and self.matrix[E.y][i] != 0:
                    heapq.heappush(processedEdge, Edge(E.y, i, self.matrix[E.y][i]))
        return outEdge


graphM = GraphM(10)
graphM.randomFill(50, 1, 1000)
graphM.fromFile("PrimData.txt")
print(graphM)
print("\n")
out = graphM.prim(0)
for i in out:
    print(i)
