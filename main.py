import graphviz as gv
import numpy as np
import numpy.random as rnd


def find_shortest_path(size: int, start: int, end: int):
    explored = []
    queue = [[start]]

    if start == end:
        print("Выбран один и тот же узел")
        return

    while queue:
        path = queue.pop(0)
        node = path[-1]


        if node not in explored:
            neighbours = dictionary[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == end and len(new_path) == size:
                    print("Shortest path = ", *new_path)
                    print(len(new_path))
                    return
            explored.append(node)
    print("Нет пути размера L")


n = int(input("Введите размерность матрицы: "))

nodes = [i for i in range(1, n + 1)]
edges = []

matrix1 = np.zeros((n,n), dtype=int)


for i in range(0, n):
    for j in range(0+i, n):
        matrix1[i, j] = rnd.randint(2)
        if j == i:
            matrix1[i,j] = 1

print(matrix1)
print()
print()

matrix2 = np.transpose(matrix1).copy()

for i in range(n):
    matrix2[i,i] = 0

matrix1 = matrix2 + matrix1


print(matrix1)
dictionary = {}
temp = []
for i in range(0, n):
    for j in range(0, n):
        if matrix1[i, j] == 1:
            temp.append(j+1)
            edges.append((str(i+1), str(j+1)))
    dictionary[i+1] = temp
    temp = []


print(dictionary)
find_shortest_path(4, 3, 15)

grah = gv.Digraph(format='png')
grah.edges(edges)
grah.view()