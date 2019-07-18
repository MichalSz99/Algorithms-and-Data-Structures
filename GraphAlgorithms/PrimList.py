import random
import heapq
import re


class DEdge:
    def __init__(self, y, val):
        self.val = val
        self.y = y

    def __str__(self):
        str_edge = "[(" + str(self.y) + ");" + str(self.val) + "]"
        return str_edge

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
        str_edge = "[(" + str(self.x) + "," + str(self.y) + ");" + str(self.val) + "]"
        return str_edge


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

    def random_fill(self, density, value_min, value_max):
        self.clear()
        max_edge = round(self.vertex * (self.vertex - 1) * (density / 100))
        count = 0
        while count < max_edge:
            repeat = False
            value = random.randint(value_min, value_max)
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
            self.list[predecessor].append(DEdge(successor, value))
            self.list[successor].append(DEdge(predecessor, value))
            count += 2

    def from_file(self, file_name):
        self.clear()
        file = open(file_name, "r")
        input_data = file.read()
        data = re.findall(r"\d+", input_data)
        for i in range(0, len(data), 3):
            predecessor = int(data[i])
            successor = int(data[i+1])
            value = int(data[i + 2])
            self.list[predecessor].append(DEdge(successor, value))
            self.list[successor].append(DEdge(predecessor, value))

    def prim(self, start):
        list_of_vertex = [False] * self.vertex
        list_of_vertex[start] = True
        out_edge = []
        processed_edge = []
        for i in range(len(self.list[start])):
            heapq.heappush(processed_edge, Edge(start, self.list[start][i].y, self.list[start][i].val))
        while len(out_edge) < self.vertex - 1:
            while processed_edge:
                current_edge = heapq.heappop(processed_edge)
                if not (list_of_vertex[current_edge.y]):
                    break

            if not processed_edge:
                break

            list_of_vertex[current_edge.y] = True
            out_edge.append(current_edge)

            for i in range(len(self.list[current_edge.y])):
                if not (list_of_vertex[self.list[current_edge.y][i].y]):
                    heapq.heappush(processed_edge, Edge(current_edge.y, self.list[current_edge.y][i].y,
                                   self.list[current_edge.y][i].val))
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
