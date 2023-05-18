from collections import deque
import Heap
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_directed_edge(self, u, v):
        self.adj_matrix[u][v] = 1

    def add_undirected_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def add_undirected_edge(self, u, v,weight):
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight

    def add_directed_edge(self, u, v,weight):
        self.adj_matrix[u][v] = weight

    def get_neighbors(self,x):
        neighbors=[]
        for i in range (self.num_vertices):
            if self.adj_matrix[x][i] != 0 and i != x:
                neighbors.append(i)
        return neighbors

    def display(self):

        for i in range (self.num_vertices):
            print(self.adj_matrix[i])


    def BFT(self, start):
        visited = [False] * self.num_vertices
        queue = deque([start])
        result = []
        while queue:
            x = queue.popleft()
            visited[x] = True
            result.append(x)
            neighbors = self.get_neighbors(x)
            for i in range (len(neighbors)):
                if visited[neighbors[i]] == False :
                    queue.append(neighbors[i])
                    visited[neighbors[i]] = True
        return result

    def DFT(self, start):
        visited = [False] * self.num_vertices
        result = []

        def dft_recursion(vertex):
            visited[vertex] = True
            result.append(vertex)
            neighbors = self.get_neighbors(vertex)
            for i in range(len(neighbors)):
                if visited[neighbors[i]] == False:
                    dft_recursion(neighbors[i])

        dft_recursion(start)
        return result

    def MST(self, start):

        result = Graph(self.num_vertices)
        visited = [False] * self.num_vertices
        weight = [99999] * self.num_vertices

        visited[start] = True
        weight[start] = 0

        neighbors = self.get_neighbors(start)
        parent = start
        P = []
        for j in range (self.num_vertices-1):

            for i in range (len(neighbors)):

                new_weight = self.adj_matrix[parent][neighbors[i]]
                if weight[neighbors[i]] > new_weight and visited[neighbors[i]] == False:
                    P=Heap.delete(P, neighbors[i])
                    weight[neighbors[i]] = new_weight
                    P.append(Heap.Node(neighbors[i],new_weight,parent))


            if len(P) >= 1:
                Heap.heaport(P)
                new = Heap.delete_min(P)

                visited[(new.num)]= True

                result.add_weighted_undirected_edge(new.num, new.parent, new.key)
                parent = new.num
                neighbors = self.get_neighbors(parent)
        return result

    def SP (self, start):
        result = Graph(self.num_vertices)
        visited = [False] * self.num_vertices
        weight = [99999] * self.num_vertices

        visited[start] = True
        weight[start] = 0

        neighbors = self.get_neighbors(start)
        parent = start
        P = []

        for j in range (self.num_vertices-1):
            for i in range (len(neighbors)):

                new_weight = self.adj_matrix[parent][neighbors[i]] + weight[parent]
                if weight[neighbors[i]] > new_weight and visited[neighbors[i]] == False:
                    P=Heap.delete(P, neighbors[i])
                    weight[neighbors[i]] = new_weight
                    P.append(Heap.Node(neighbors[i],new_weight,parent))
            if len(P) >= 1:
                Heap.heaport(P)
                new = Heap.delete_min(P)

                visited[(new.num)]= True
                result.add_directed_edge(new.parent, new.num, new.key-weight[new.parent])
                parent = new.num
                neighbors = self.get_neighbors(parent)

        for i in range (self.num_vertices):
            if visited[i] == False:
                print("**The Graph is not Connected!!**")
                return
        result.display()
        return result







'Undirected MST'
#g = Graph(9)
#g.add_undirected_edge(0, 1, 4)
#g.add_undirected_edge(0, 7, 8)
#g.add_undirected_edge(1, 2, 8)
#g.add_undirected_edge(1, 7, 11)
#g.add_undirected_edge(2, 3, 7)
#g.add_undirected_edge(2, 5, 4)
#g.add_undirected_edge(2, 8, 2)
#g.add_undirected_edge(3, 4, 9)
#g.add_undirected_edge(3, 5, 14)
#g.add_undirected_edge(4, 5, 10)
#g.add_undirected_edge(5, 6, 2)
#g.add_undirected_edge(6, 7, 1)
#g.add_undirected_edge(6, 8, 6)
#g.add_undirected_edge(7, 8, 7)

#res = g.MST(0)
#g.display()
#print()
#res.display()



'Directer SP'
g = Graph(5)
g.add_directed_edge(0, 1, 10)
g.add_directed_edge(0, 4, 5)
g.add_directed_edge(1, 2, 1)
g.add_directed_edge(1, 4, 2)
g.add_directed_edge(2, 3, 4)
g.add_directed_edge(3, 2, 6)
g.add_directed_edge(3, 0, 7)
g.add_directed_edge(4, 1, 3)
g.add_directed_edge(4, 3, 2)
g.add_directed_edge(4, 2, 9)

res = g.SP(0)



