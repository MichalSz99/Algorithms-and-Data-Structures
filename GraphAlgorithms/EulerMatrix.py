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

    def randomFill(self, density):
        self.clear()
        MAXedge = round(self.vertex * (self.vertex - 1) * (density / 100))
        count = 0
        while count < MAXedge:
            x = random.randint(0, self.vertex - 1)
            y = random.randint(0, self.vertex - 1)
            z = random.randint(0, self.vertex - 1)
            if z == x or x == y or z == y or self.matrix[x][y] == 1 or self.matrix[x][z] == 1 or self.matrix[y][z] == 1:
                continue
            else:
                self.matrix[x][y] = 1
                self.matrix[y][x] = 1
                self.matrix[x][z] = 1
                self.matrix[z][x] = 1
                self.matrix[z][y] = 1
                self.matrix[y][z] = 1
                count += 6

    def fromFile(self, fileName):
        self.clear()
        file = open(fileName, "r")
        input = file.read()
        vertex = re.findall(r"\d+", input)
        for i in range(0, len(vertex), 2):
            predecessor = int(vertex[i])
            successor = int(vertex[i + 1])
            self.matrix[predecessor][successor] = 1
            self.matrix[successor][predecessor] = 1

    def checkEuler(self):
        for i in range(self.vertex):
            sum = 0
            for j in self.matrix[i]:
                sum += self.matrix[i][j]
            if sum % 2 ==1:
                return False
        return True

    def Euler(self, startVertex):
        if self.checkEuler():
            out = []
            stack = [startVertex]
            while stack:
                v = stack[-1]
                is_edge = False
                for i in range(len(self.matrix)):
                    if self.matrix[v][i] == 1:
                        self.matrix[v][i] *= -1
                        self.matrix[i][v] *= -1
                        stack.append(i)
                        is_edge = True
                        break
                if is_edge:
                    continue
                stack.pop()
                out.append(v)
            for i in range(self.vertex):
                for j in range(self.vertex):
                    self.matrix[i][j] *= -1
            return out
        else:
            return False


graph = Graph(10)
graph.randomFill(70)
print(graph)
print("\n")
print(graph.Euler(0))
graph.fromFile("EulerData.txt")
print(graph)
print("\n")
print(graph.Euler(0))
