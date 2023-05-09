from pyvis.network import Network
import random

class Node:
    def __init__(self, name, desc, tags, id=0):
        self.name = name
        self.desc = desc
        self.tags = tags

        if id:  self.node_id = id
        else:   self.node_id =  str(hex(random.randint(16**4, 16**6)))[2:]
    

class Edge:
    def __init__(self, source_id, target_id, desc=None, id=0):
        self.source_id = source_id
        self.target_id = target_id
        self.desc = desc
        
        if id:  self.node_id = id
        else:   self.node_id =  str(hex(random.randint(16**4, 16**6)))[2:]

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.adj_matrix = {}

        #will contain recent changes to be commited to net obj
        self.to_update = {}
        self.net = Network()
    

    def save_graph(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    def load_graph(filename):
        with open(filename, 'rb') as file:
            self = pickle.load(file)
            return self
    
    def list_tags(self):
        tags = set()
        for node in self.nodes.values():
            tags.update(node.tags)
        return list(tags)
    
    def add_node(self, name, desc, tags):
        node = Node(name, desc, tags)
        self.nodes[node.node_id] = node
        self.adj_matrix[node.node_id] = {}
    
    def delete_node(self, node_id):
        if node_id in self.nodes:
            del self.nodes[node_id]
            del self.adj_matrix[node_id]
            for neighbor_id in self.adj_matrix:
                if node_id in self.adj_matrix[neighbor_id]:
                    edge_id = self.adj_matrix[neighbor_id][node_id]
                    del self.adj_matrix[neighbor_id][node_id]
                    del self.edges[edge_id]
    
    def add_edges(self, edge_list):
        for edge in edge_list:
            source_id, target_id = edge
            if source_id in self.nodes and target_id in self.nodes:
                edge = Edge(source_id, target_id)
                self.edges[edge.edge_id] = edge
                self.adj_matrix[source_id][target_id] = edge.edge_id
                self.adj_matrix[target_id][source_id] = edge.edge_id
    
    def delete_edges(self, edge_list):
        for edge in edge_list:
            source_id, target_id = edge
            if source_id in self.nodes and target_id in self.nodes and target_id in self.adj_matrix[source_id]:
                edge_id = self.adj_matrix[source_id][target_id]
                del self.edges[edge_id]
                del self.adj_matrix[source_id][target_id]
                del self.adj_matrix[target_id][source_id]
    
    def describe_node(self, node_id):
        if node_id in self.nodes:
            node = self.nodes[node_id]
            print(f"Name: {node.name}")
            print(f"Description: {node.desc}")
            print(f"Tags: {', '.join(node.tags)}")
            neighbors = [edge.target_id for edge in self.edges.values() if edge.source_id == node_id] + \
                        [edge.source_id for edge in self.edges.values() if edge.target_id == node_id]
            print(f"Neighbors: {', '.join(str(neighbor) for neighbor in neighbors)}")
        else:
            print("Node not found.")
    
    def draw_graph(self):
        net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
        for node_id, node in self.nodes.items():
            net.add_node(node_id, label=node.name, title=node_id+' | '+node.desc, group=node.tags[0])
        for edge in self.edges.values():
            net.add_edge(edge.source_id, edge.target_id, title=edge.desc)
        net.show("graph.html", notebook=False)

# example usage
graph = Graph()

graph.draw_graph()
