import networkx as nx
from pyvis.network import Network

# create a graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# visualize the graph using PyVis
net = Network()
net.from_nx(G)
net.show("mygraph.html",notebook=False)
