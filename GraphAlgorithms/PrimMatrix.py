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
                pom = pom + '{:>4}'.format(str(self.matrix[i][j]) )+ " "
            out = out + "\n" + pom
        return out

    def clear(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                self.matrix[i][j] = 0

    def randomFill(self, density, valueMin, valueMax):
        self.clear()
        MAXedge = round(self.vertex * (self.vertex - 1) * (density / 100))
        count = 0
        while count < MAXedge:
            value = random.randint(valueMin, valueMax)
            predecessor = random.randint(0, self.vertex - 1)
            successor = random.randint(0, self.vertex - 1)
            if self.matrix[predecessor][successor] != 0 or predecessor == successor:
                continue
            self.matrix[predecessor][successor] = value
            self.matrix[successor][predecessor] = value
            count += 2

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
                currentEdge = heapq.heappop(processedEdge)
                if not (listOfVertex[currentEdge.y]):
                    break

            if not processedEdge:
                break

            listOfVertex[currentEdge.y] = True
            outEdge.append(currentEdge)

            for i in range(len(self.matrix)):
                if not (listOfVertex[i]) and self.matrix[currentEdge.y][i] != 0:
                    heapq.heappush(processedEdge, Edge(currentEdge.y, i, self.matrix[currentEdge.y][i]))
        return outEdge

graph = Graph(10)
graph.randomFill(70, 1, 1000)
print(graph)
print("\n")
out = graph.prim(0)
for i in out:
    print(i)
graph.fromFile("PrimData.txt")
print(graph)
print("\n")
out = graph.prim(0)
for i in out:
    print(i)
 
