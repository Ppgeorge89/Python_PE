from My_module import Timer
import re
import numpy as np

@Timer.timeit
def main():
    class Graph(object):

        def __init__(self, vertices, edges, weights):
            self.vertices = vertices
            self.edges = edges
            self.weights = weights

        def neighbours(self, vertex_1, vertex_2, flag=False):
            if [vertex_1, vertex_2] in self.edges:
                flag = True
            return flag

        def are_neighbours(self, vertex_1, vertex_2):
            if self.neighbours(vertex_1, vertex_2):
                return "Vertices {0} and {1} are neighbours".format(vertex_1, vertex_2)
            else:
                return "Vertices {0} and {1} are not neighbours".format(vertex_1, vertex_2)

        def all_neighbours(self, vertex):
            all_neighbours = []
            for i in self.vertices:
                if self.neighbours(vertex, i):
                    all_neighbours.append(i)
            return all_neighbours

        def find_path(self, start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            for i in self.all_neighbours(start):
                if i not in path:
                    new_path = self.find_path(i, end, path)
                    if new_path: return new_path
            return None

        def find_all_paths(self, start, end, path=[]):
            path = path + [start]
            if start == end:
                return [path]
            paths = []
            for i in self.all_neighbours(start):
                if i not in path:
                    new_paths = self.find_all_paths(i, end, path)
                    for new_path in new_paths:
                        paths.append(new_path)
            return paths

        def weight_of_path(self, path):
            weight = 1
            for i in range(0, len(path)):
                weight *= self.weights[i]
            return weight

        def find_shortest_path(self, start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            shortest = None
            for i in self.all_neighbours(start):
                if i not in path:
                    new_path = self.find_shortest_path(i, end, path)
                    if new_path:
                        if not shortest or len(new_path) < len(shortest):
                            shortest = new_path
            return shortest

        def find_optimal_path(self, start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            shortest = None
            for i in self.all_neighbours(start):
                if i not in path:
                    new_path = self.find_shortest_path(i, end, path)
                    if new_path:
                        if not shortest or self.weight_of_path(new_path) < self.weight_of_path(shortest):
                            shortest = new_path
            return shortest


    def matrix_graph(_matrix, directions):
        vertices = []
        edges = []
        weights = []
        for i in range(0, _matrix.shape[0]):
            for j in range(0, _matrix.shape[1]):
                vertices.append((i, j))
                for k in range(0, len(directions)):
                    if (i, j) != (i + directions[k][0], j + directions[k][1]):
                        if not (i + directions[k][0] < 0 or j + directions[k][1] < 0 or
                                i + directions[k][0] > _matrix.shape[0] + 1 or j
                                + directions[k][1] > _matrix.shape[1] + 1):
                            edges.append([(i, j), (i + directions[k][0], j + directions[k][1])])
                weights.append(_matrix[i, j])
        graph_of_matrix = Graph(vertices, edges, weights)
        return graph_of_matrix

    filename = "p081_matrix.txt"
    file = open(filename, "r")
    pattern = re.compile(",|\n")
    x = pattern.split(file.read())
    x = list(map(int, x[0:6400]))
    matrix = np.array(x).reshape(80, 80)
    gm = matrix_graph(np.array(matrix), [[0, 1], [1, 0], [-1, 0], [0, -1]])
    print(gm.weight_of_path(gm.find_optimal_path((0, 0), (6399, 6399))))

if __name__ == '__main__':
    main()
