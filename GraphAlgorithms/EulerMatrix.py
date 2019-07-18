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
        count = 0
        while count < max_edge:
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

    def check_euler(self):
        for i in range(self.vertex):
            check_sum = 0
            for j in self.matrix[i]:
                check_sum += self.matrix[i][j]
            if check_sum % 2 == 1:
                return False
        return True

    def euler(self, start_vertex):
        if self.check_euler():
            out = []
            stack = [start_vertex]
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
graph.random_fill(70)
print(graph)
print("\n")
print(graph.euler(0))
graph.from_file("EulerData.txt")
print(graph)
print("\n")
print(graph.euler(0))
