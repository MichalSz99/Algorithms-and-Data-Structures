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

    def random_fill(self, density):
        self.clear()
        max_edge = round(self.vertex * (self.vertex - 1) * (density / 100))
        list_of_vertex = list(range(self.vertex))
        random.shuffle(list_of_vertex)
        for i in range(self.vertex - 1):
            self.list[list_of_vertex[i]].append(list_of_vertex[i+1])
            self.list[list_of_vertex[i+1]].append(list_of_vertex[i])
        self.list[list_of_vertex[0]].append(list_of_vertex[-1])
        self.list[list_of_vertex[-1]].append(list_of_vertex[0])
        count = 2 * self.vertex
        while count < max_edge:
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

    def __hamilton(self, out, start_vertex, current_vertex, end):
        if not end:
            for i in range(len(self.list[current_vertex])):
                successor = self.list[current_vertex][i]
                if not (successor in out):
                    out.append(successor)
                    out, end = self.__hamilton(out, start_vertex, successor, end)
                    if end:
                        return out, end
            if len(out) == self.vertex and start_vertex in self.list[current_vertex]:
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
