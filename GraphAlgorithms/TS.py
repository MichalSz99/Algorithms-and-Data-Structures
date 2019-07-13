import random

class GraphMatrix :

    def __init__ (self, n, g): # making random DAG with n vertices
        self.matrix = []       # and concentration g% as Adjacency Matrix
        for i in range (n):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(0)
        for i in range(n):
            for j in range(i+1, n):
                if j == i+1 or  (random.random() + 2/n) < (g/100):
                    self.matrix[i][j] = 1
        for i in range(n):
            x = random.randint(0,n-1)
            y = random.randint(0,n-1)
            if x != y:
                self.matrix[x], self.matrix[y] =  self.matrix[y],  self.matrix[x]
                for i in range(n):
                    self.matrix[i][x], self.matrix[i][y] = self.matrix[i][y], self.matrix[i][x]
                
    def __str__(self):
        out = ""
        for i in range (len(self.matrix)):
            pom = ""
            for j in range(len(self.matrix)):
                pom = pom + str(self.matrix[i][j]) + " "
            out = out + "\n" + pom
        return out

    def _TS(self, Visited, Sort, v): #Topological Sort
        Visited[v] = 1
        for  i in range(len(self.matrix)):
            if Visited[i] == 0 and self.matrix[v][i] != 0:
                self._TS(Visited, Sort, i)
        Sort.insert(0,v)

    def TS(self,start):
        Visited = [0]*len(self.matrix)
        Sort = []
        self._TS(Visited, Sort, start)
        return Sort


class GraphList:
    def __init__ (self, matrix): # making Incidence List based on Adjacency matrix
        self.list = []
        l = len(matrix.matrix)
        for  i in range(l):
            self.list.append([])
            for j in range(l):
                val = matrix.matrix[i][j]
                if  val != 0:
                   self.list[i].append(j)

    def __str__(self):
        l = len(self.list)
        out = ""
        for i in range (l):
            pom = str(i)+ ":  "
            li = len(self.list[i])
            for j in range(li):
                pom = pom + str(self.list[i][j]) + " "
            out = out + "\n" + pom
        return out

    def _TS(self,Visited, Sort, v): #Topological Sort
        Visited[v] = 1
        for  i in range(len(self.list[v])):
            if Visited[self.list[v][i]] == 0:
               self._TS(Visited, Sort, self.list[v][i])
        Sort.insert(0,v)

    def TS(self,start):
        Visited = [0]*len(self.list)
        Sort = []
        self._TS(Visited, Sort, start)
        return Sort

    
graphM = GraphMatrix(10,60)
print(graphM)
graphL = GraphList(graphM)
print(graphL)

print(graphM.TS(0))
print(graphL.TS(0))
