import tkinter as tk
import networkx as nx
from pyvis.network import Network

class GraphEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph Editor")

        # create a graph
        self.G = nx.Graph()

        # create the PyVis visualization
        self.net = Network(width="100%", height="500px", directed=False)
        self.net.from_nx(self.G)
        self.net.show("mygraph.html", notebook=False)

        # create the Tkinter widgets
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.add_node_button = tk.Button(self.master, text="Add Node", command=self.add_node)
        self.add_node_button.pack()
        self.add_edge_button = tk.Button(self.master, text="Add Edge", command=self.add_edge)
        self.add_edge_button.pack()

        # bind the canvas events
        self.canvas.bind("<Button-1>", self.canvas_click)

    def add_node(self):
        # add a new node to the graph
        new_node = len(self.G) + 1
        self.G.add_node(new_node)
        self.net.from_nx(self.G)
        self.net.show("mygraph.html", notebook=False)

    def add_edge(self):
        # add a new edge to the graph
        self.G.add_edge(1, 2)
        self.net.from_nx(self.G)
        self.net.show("mygraph.html", notebook=False)

    def canvas_click(self, event):
        # handle canvas click events
        print("Canvas clicked at:", event.x, event.y)

if __name__ == "__main__":
    root = tk.Tk()
    editor = GraphEditor(root)
    root.mainloop()