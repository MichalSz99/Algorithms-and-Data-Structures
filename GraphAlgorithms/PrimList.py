import random
import heapq
import re

class dEdge:
    def __init__(self, y, val):
        self.val = val
        self.y = y

    def __str__(self):
        out = "[(" + str(self.y) + ");" + str(self.val) + "]"
        return out

    def __lt__(self, other):
        return self.val < other.val


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

    def randomFill(self, density, valueMin, valueMax):
        self.clear()
        MAXedge = round(self.vertex * (self.vertex - 1) * (density / 100))
        count = 0
        while count < MAXedge:
            repeat = False
            value = random.randint(valueMin, valueMax)
            predecessor = random.randint(0, self.vertex - 1)
            successor = random.randint(0, self.vertex - 1)
            if predecessor == successor:
                continue
            for edge in self.list[predecessor]:
                if edge.y == successor:
                    repeat = True
                    break
            if repeat:
                continue
            self.list[predecessor].append(dEdge(successor, value))
            self.list[successor].append(dEdge(predecessor, value))
            count += 2

    def fromFile(self, fileName):
        self.clear()
        file = open(fileName, "r")
        input = file.read()
        vertex = re.findall(r"\d+", input)
        for i in range(0, len(vertex), 3):
            predecessor = int(vertex[i])
            successor = int(vertex[i+1])
            value = int(vertex[i + 2])
            self.list[predecessor].append(dEdge(successor, value))
            self.list[successor].append(dEdge(predecessor, value))

    def prim(self, start):
        listOfVertex = [False] * self.vertex
        listOfVertex[start] = True
        outEdge = []
        processedEdge = []
        for i in range(len(self.list[start])):
            heapq.heappush(processedEdge, Edge(start, self.list[start][i].y, self.list[start][i].val))
        while len(outEdge) < self.vertex - 1:
            while processedEdge:
                currentEdge = heapq.heappop(processedEdge)
                if not (listOfVertex[currentEdge.y]):
                    break

            if not processedEdge:
                break

            listOfVertex[currentEdge.y] = True
            outEdge.append(currentEdge)

            for i in range(len(self.list[currentEdge.y])):
                if not (listOfVertex[self.list[currentEdge.y][i].y]):
                    heapq.heappush(processedEdge, Edge(currentEdge.y, self.list[currentEdge.y][i].y,
                                                       self.list[currentEdge.y][i].val))
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
