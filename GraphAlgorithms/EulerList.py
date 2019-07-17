import random
import re
import copy

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
                self.list[i] =[]

    def randomFill(self, density):
        self.clear()
        MAXedge = round(self.vertex * (self.vertex - 1) * (density / 100))
        count = 0
        while count < MAXedge:
            x = random.randint(0, self.vertex - 1)
            y = random.randint(0, self.vertex - 1)
            z = random.randint(0, self.vertex - 1)
            if z == x or x == y or z == y or x in self.list[y] or x in self.list[z] or y in self.list[z]:
                continue
            else:
                self.list[x].append(y)
                self.list[y].append(x)
                self.list[x].append(z)
                self.list[z].append(x)
                self.list[z].append(y)
                self.list[y].append(z)
                count += 6

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

    def checkEuler(self):
        for i in range(self.vertex):
            if len(self.list[i]) % 2 == 1:
                return False
        return True

    def Euler(self, startVertex): 
        if self.checkEuler():
            copyGraph = copy.copy(self.list)
            out = []
            stack = [startVertex]
            while stack:
                v = stack[-1]
                is_edge = False
                if self.list[v]:
                    stack.append(self.list[v][0])
                    is_edge = True
                    self.list[self.list[v][0]].remove(v)
                    self.list[v].remove(self.list[v][0])
                if is_edge:
                    continue
                stack.pop()
                out.append(v)
            self.list = copy.copy(copyGraph)
            return out
        else:
            return False


graph = Graph(10)
graph.randomFill(30)
graph.fromFile("EulerData.txt")
print(graph)
print("\n")
print(graph.Euler(0))
