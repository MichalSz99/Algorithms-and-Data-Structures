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
        self.new_rows = self.rows
        self.columns = capacity
        self.new_cols = capacity
        self.matrix = []

    def __str__(self):
        out = ""
        for i in range(self.rows+1):
            pom = ""
            for j in range(self.columns+1):
                pom = pom + '{:>2}'.format(str(self.matrix[i][j])) + " "
            out = out + "\n" + pom
        return out

    def clear(self):
        self.object_list = []
        self.rows = 0
        self.new_rows = 0
        self.matrix = []
        self.new_cols = 0

    def __add_from_file(self, file_name):
        file = open(file_name, "r")
        file_data = file.read()
        data = re.findall(r"\d+", file_data)
        for i in range(0, len(data), 2):
            weight = int(data[i])
            value = int(data[i + 1])
            self.object_list.append(Object(weight, value))
            self.rows += 1
            self.new_rows += 1

    def __add_random(self, object_number, min_weight, max_weight, min_value, max_value):
        for i in range(object_number):
            weight = random.randint(min_weight, max_weight)
            value = random.randint(min_value, max_value)
            self.object_list.append(Object(weight, value))
            self.rows += 1
            self.new_rows += 1

    def new_from_file(self, file_name):
        self.clear()
        self.__add_from_file(file_name)

    def append_from_file(self, file_name):
        self.__add_from_file(file_name)

    def new_random(self, object_number, min_weight, max_weight, min_value, max_value):
        self.clear()
        self.__add_random(object_number, min_weight, max_weight, min_value, max_value)

    def append_random(self, object_number, min_weight, max_weight, min_value, max_value):
        self.__add_random(object_number, min_weight, max_weight, min_value, max_value)

    def set_capacity(self, new_capacity):
        if self.matrix:
            self.new_cols = new_capacity - self.columns
        else:
            self.new_cols = new_capacity
        self.columns = new_capacity

    def __find_value(self, i, j):
        if i == 0:
            self.matrix[i].append(0)
        elif j == 0:
            self.matrix[i].append(0)
        elif j < self.object_list[i - 1].weight:
            self.matrix[i].append(self.matrix[i - 1][j])
        else:
            self.matrix[i].append(max(self.matrix[i - 1][j], self.matrix[i][j - 1],
                                      self.matrix[i - 1][j - self.object_list[i - 1].weight]
                                      + self.object_list[i - 1].value,
                                      self.matrix[i][j - self.object_list[i - 1].weight]
                                      + self.object_list[i - 1].value))

    def fill(self):
        if self.new_rows != 0:
            if self.rows == self.new_rows:
                for i in range(self.rows+1):
                    self.matrix.append([])
                    for j in range(self.columns - self.new_cols + 1):
                        self.__find_value(i, j)
            else:
                for i in range(self.rows - self.new_rows + 1, self.rows+1):
                    self.matrix.append([])
                    for j in range(self.columns - self.new_cols + 1):
                        self.__find_value(i, j)
        self.new_rows = 0

        if self.new_cols != 0:
            for i in range(self.rows + 1):
                self.matrix.append([])
                for j in range(self.columns - self.new_cols + 1, self.columns + 1):
                    self.__find_value(i, j)
        self.new_cols = 0

    def search(self, current_row=None, current_col=None):
        if current_row is None:
            current_row = self.rows
        if current_col is None:
            current_col = self.columns
        if self.matrix[current_row][current_col] != 0:
            current_max = -1
            while self.matrix[current_row][current_col] >= current_max:
                current_max = self.matrix[current_row][current_col]
                current_row -= 1
            current_row += 1
            while self.matrix[current_row][current_col] >= current_max:
                current_max = self.matrix[current_row][current_col]
                current_col -= 1
            current_col += 1
            result = self.search(current_row, current_col - self.object_list[current_row-1].weight)
            result.append(self.object_list[current_row-1].number)
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
matrix.new_from_file("KnapsackData.txt")
matrix.fill()
print(matrix)
print("Numbers of items in Knapsack: " + str(matrix.search()))
matrix.show_items()
matrix.append_random(10, 2, 10, 5, 10)
matrix.set_capacity(14)
matrix.fill()
print(matrix)
print("Numbers of items in Knapsack: " + str(matrix.search()))
matrix.show_items()
