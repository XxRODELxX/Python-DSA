#!/usr/bin/python3

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def print_graph(self):
        for vertex, edges in self.adjacency_list.items():
            print(vertex, ": ", edges)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
            self.adjacency_list[v1].append(v1)
            self.adjacency_list[v2].append(v2)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[v1].remove(v1)
                self.adjacency_list[v2].remove(v2)
            except:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for vertex_edges in self.adjacency_list[vertex]:
                self.adjacency_list[vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
        

# Test add_vertex method
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.print_graph()
print("-------")
my_graph.add_vertex("B")
my_graph.print_graph()
print("-------")

# Test add_edge method
my_graph.add_edge("A", "B")
my_graph.print_graph()
print("-------")

# Test remove_edge method
my_graph.remove_edge("A", "B")
my_graph.print_graph()
print("-------")

# Test remove_vertex method
my_graph.remove_vertex("B")
my_graph.print_graph()