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
            for j in range(len(self.list[i])):
                pom = pom + str(self.list[i][j]) + " "
            out = out + "\n" + pom
        return out

    def clear(self):
        for i in range(self.vertex):
            self.list[i] = []

    def randomFill(self, density):
        self.clear()
        MAXedge = round(self.vertex * (self.vertex - 1) * (density / 100))
        listOfVertex= list(range(self.vertex))
        random.shuffle(listOfVertex)
        for i in range(self.vertex - 1):
            self.list[listOfVertex[i]].append(listOfVertex[i+1])
            self.list[listOfVertex[i+1]].append(listOfVertex[i])
        self.list[listOfVertex[0]].append(listOfVertex[-1])
        self.list[listOfVertex[-1]].append(listOfVertex[0])
        count = 2 * self.vertex
        while count < MAXedge:
            x = random.randint(0, self.vertex - 1)
            y = random.randint(0, self.vertex - 1)
            if x == y or y in self.list[x]:
                continue
            else:
                self.list[x].append(y)
                self.list[y].append(x)
                count += 2
        for i in range(self.vertex):
            random.shuffle(self.list[i])

    def fromFile(self, fileName):
        self.clear()
        file = open(fileName, "r")
        input = file.read()
        vertex = re.findall(r"\d+", input)
        for i in range(0, len(vertex), 2):
            predecessor = int(vertex[i])
            successor = int(vertex[i + 1])
            self.list[predecessor].append(successor)
            self.list[successor].append(predecessor)

    def __Hamilton(self, out, startVertex, currentVertex, end):
        if not end:
            for i in range(len(self.list[currentVertex])):
                successor = self.list[currentVertex][i]
                if not (successor in out):
                    out.append(successor)
                    out, end = self.__Hamilton(out, startVertex, successor, end)
                    if end:
                        return out, end
            if len(out) == self.vertex and startVertex in self.list[currentVertex]:
                out.append(startVertex)
                end = True
            else:
                out.pop()
        return out, end

    def Hamilton(self, startVertex):
        out = [startVertex]
        end = False
        out, end = self.__Hamilton(out, startVertex, startVertex, end)
        return out


graph = Graph(10)
graph.randomFill(30)
print(graph)
print("\n")
print(graph.Hamilton(0))
graph.fromFile("HamiltonData.txt")
print(graph)
print("\n")
print(graph.Hamilton(0))
