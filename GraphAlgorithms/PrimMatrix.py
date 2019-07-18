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
        str_edge = "[(" + str(self.x) + "," + str(self.y) + ");" + str(self.val) + "]"
        return str_edge


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
                pom = pom + '{:>4}'.format(str(self.matrix[i][j])) + " "
            out = out + "\n" + pom
        return out

    def clear(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                self.matrix[i][j] = 0

    def random_fill(self, density, value_min, value_max):
        self.clear()
        max_edge = round(self.vertex * (self.vertex - 1) * (density / 100))
        count = 0
        while count < max_edge:
            value = random.randint(value_min, value_max)
            predecessor = random.randint(0, self.vertex - 1)
            successor = random.randint(0, self.vertex - 1)
            if self.matrix[predecessor][successor] != 0 or predecessor == successor:
                continue
            self.matrix[predecessor][successor] = value
            self.matrix[successor][predecessor] = value
            count += 2

    def from_file(self, file_name):
        self.clear()
        file = open(file_name, "r")
        input_data = file.read()
        data = re.findall(r"\d+", input_data)
        for i in range(0, len(data), 3):
            predecessor = int(data[i])
            successor = int(data[i + 1])
            value = int(data[i + 2])
            self.matrix[predecessor][successor] = value
            self.matrix[successor][predecessor] = value

    def prim(self, start):
        list_of_vertex = [False] * self.vertex
        list_of_vertex[start] = True
        out_edge = []
        processed_edge = []
        for i in range(self.vertex):
            if self.matrix[start][i] != 0:
                heapq.heappush(processed_edge, Edge(start, i, self.matrix[start][i]))
        while len(out_edge) < self.vertex - 1:
            while processed_edge:
                current_edge = heapq.heappop(processed_edge)
                if not (list_of_vertex[current_edge.y]):
                    break

            if not processed_edge:
                break

            list_of_vertex[current_edge.y] = True
            out_edge.append(current_edge)

            for i in range(len(self.matrix)):
                if not (list_of_vertex[i]) and self.matrix[current_edge.y][i] != 0:
                    heapq.heappush(processed_edge, Edge(current_edge.y, i, self.matrix[current_edge.y][i]))
        return out_edge


graph = Graph(10)
graph.random_fill(70, 1, 1000)
print(graph)
print("\n")
result = graph.prim(0)
for i in result:
    print(i)
graph.from_file("PrimData.txt")
print(graph)
print("\n")
result = graph.prim(0)
for i in result:
    print(i)
