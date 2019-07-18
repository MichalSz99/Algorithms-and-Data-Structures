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
            self.list[i] = []

    def random_fill(self, density):
        self.clear()
        max_edge = round(self.vertex * (self.vertex - 1) * (density / 100))
        count = 0
        while count < max_edge:
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

    def from_file(self, file_name):
        self.clear()
        file = open(file_name, "r")
        input_data = file.read()
        data = re.findall(r"\d+", input_data)
        for i in range(0, len(data), 2):
            predecessor = int(data[i])
            successor = int(data[i + 1])
            self.list[predecessor].append(successor)
            self.list[successor].append(predecessor)

    def check_euler(self):
        for i in range(self.vertex):
            if len(self.list[i]) % 2 == 1:
                return False
        return True

    def euler(self, start_vertex):
        if self.check_euler():
            copy_graph = copy.copy(self.list)
            out = []
            stack = [start_vertex]
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
            self.list = copy.copy(copy_graph)
            return out
        else:
            return False


graph = Graph(10)
graph.random_fill(30)
print(graph)
print("\n")
print(graph.euler(0))
graph.from_file("EulerData.txt")
print(graph)
print("\n")
print(graph.euler(0))
