import random
import re


class Object:
    amount = 0

    def __init__(self, weight, value):
        Object.amount += 1
        self.number = Object.amount
        self.weight = weight
        self.value = value

    def __str__(self):
        object_str = "Item's number: " + str(self.number) + "  "
        object_str += "Item's weight: " + str(self.weight) + "  "
        object_str += "Item's value: " + str(self.value)
        return object_str

    def __del__(self):
        Object.amount -= 1


class Knapsack:
    def __init__(self, capacity=0, object_list=None):
        if object_list is None:
            self.object_list = []
        else:
            self.object_list = object_list
        self.rows = len(self.object_list)
        self.columns = capacity
        self.matrix = []

    def __str__(self):
        out = ""
        for i in range(self.rows+1):
            pom = ""
            for j in range(self.columns+1):
                pom = pom + '{:>2}'.format(str(self.matrix[i][j])) + " "
            out = out + "\n" + pom
        return out

    def from_file(self, file_name):
        self.object_list = []
        self.rows = 0
        file = open(file_name, "r")
        file_data = file.read()
        data = re.findall(r"\d+", file_data)
        for i in range(0, len(data), 2):
            weight = int(data[i])
            value = int(data[i + 1])
            self.object_list.append(Object(weight, value))
            self.rows += 1

    def random_object(self, object_number, min_weight, max_weight, min_value, max_value):
        self.object_list = []
        self.rows = 0
        for i in range(object_number):
            weight = random.randint(min_weight, max_weight)
            value = random.randint(min_value, max_value)
            self.object_list.append(Object(weight, value))
            self.rows += 1

    def fill(self):
        for i in range(self.rows+1):
            self.matrix.append([])
            for j in range(self.columns+1):
                if i == 0:
                    self.matrix[i].append(0)
                elif j == 0:
                    self.matrix[i].append(0)
                elif j < self.object_list[i-1].weight:
                    self.matrix[i].append(self.matrix[i-1][j])
                else:
                    self.matrix[i].append(max(self.matrix[i-1][j], self.matrix[i-1][j - self.object_list[i-1].weight]
                                              + self.object_list[i-1].value))

    def search(self, current_row=None, current_col=None):
        if current_row is None:
            current_row = self.rows
        if current_col is None:
            current_col = self.columns
        if self.matrix[current_row][current_col] != 0:
            current_max = -1
            while self.matrix[current_row][current_col] >= current_max and current_row != 0:
                current_max = self.matrix[current_row][current_col]
                current_row -= 1
            if current_row > 0 and current_col - self.object_list[current_row].weight >= 0:
                result = self.search(current_row, current_col - self.object_list[current_row].weight)
                result.append(self.object_list[current_row].number)
            else:
                result = [self.object_list[current_row].number]
            return result
        else:
            return []

    def show_items(self, items=None):
        if items is None:
            items = self.search()
        print("Items in Knapsack:")
        for i in items:
            print(self.object_list[i-1])


matrix = Knapsack(10)
matrix.from_file("KnapsackData.txt")
matrix.fill()
print(matrix)
print("Numbers of items in Knapsack: " + str(matrix.search()))
matrix.show_items()
matrix.random_object(10, 1, 10, 1, 10)
matrix.fill()
print(matrix)
print("Numbers of items in Knapsack: " + str(matrix.search()))
matrix.show_items()
