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
        max_edge = round(self.vertex * (self.vertex - 1) * (density / 100))
        for i in range(self.vertex - 1):
            self.matrix[i][i + 1] = 1
            self.matrix[i + 1][i] = 1
        self.matrix[0][self.vertex - 1] = 1
        self.matrix[self.vertex - 1][0] = 1
        count = 2 * self.vertex 
        while count < max_edge:
            x = random.randint(0, self.vertex - 1)
            y = random.randint(0, self.vertex - 1)
            if x == y or self.matrix[x][y] == 1:
                continue
            else:
                self.matrix[x][y] = 1
                self.matrix[y][x] = 1
                count += 2
        for j in range(self.vertex):
            x = random.randint(0, self.vertex - 1)
            y = random.randint(0, self.vertex - 1)
            if x != y:
                self.matrix[x], self.matrix[y] = self.matrix[y], self.matrix[x]
                for i in range(self.vertex):
                    self.matrix[i][x], self.matrix[i][y] = self.matrix[i][y], self.matrix[i][x]

    def from_file(self, file_name):
        self.clear()
        file = open(file_name, "r")
        input_data = file.read()
        data = re.findall(r"\d+", input_data)
        for i in range(0, len(data), 2):
            predecessor = int(data[i])
            successor = int(data[i + 1])
            self.matrix[predecessor][successor] = 1
            self.matrix[successor][predecessor] = 1

    def __hamilton(self, out, start_vertex, current_vertex, end):
        if not end:
            for i in range(len(self.matrix)):
                if self.matrix[current_vertex][i] == 1 and not (i in out):
                    out.append(i)
                    out, end = self.__hamilton(out, start_vertex, i, end)
                    if end:
                        return out, end
            if len(out) == self.vertex and self.matrix[current_vertex][start_vertex] == 1:
                out.append(start_vertex)
                end = True
            else:
                out.pop()
        return out, end

    def hamilton(self, start_vertex):
        out = [start_vertex]
        end = False
        out, end = self.__hamilton(out, start_vertex, start_vertex, end)
        return out


graph = Graph(10)
graph.random_fill(30)
print(graph)
print("\n")
print(graph.hamilton(0))
graph.from_file("HamiltonData.txt")
print(graph)
print("\n")
print(graph.hamilton(0))
