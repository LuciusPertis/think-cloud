import networkx as nx
from pyvis.network import Network
import json

# create a graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# create the PyVis visualization
net = Network()
net.from_nx(G)

# get the graph data in JSON format
graph_data = json.dumps(net.get_network_data())


import tkinter as tk
import webview
import json

# create a Tkinter window
root = tk.Tk()

# create a custom HTML template that includes the PyVis graph data
template = f"""
<html>
  <head>
    <script src="https://cdn.jsdelivr.net/npm/vis-network@9.2.6/dist/vis-network.min.js"></script>
  </head>
  <body>
    <div id="mynetwork"></div>
    <script type="text/javascript">
      var graph_data = {json.dumps(graph_data)};
      var container = document.getElementById("mynetwork");
      var data = {{
        nodes: graph_data.nodes,
        edges: graph_data.edges
      }};
      var options = {{}};
      var network = new vis.Network(container, data, options);
    </script>
  </body>
</html>
"""

# create a new webview window and load the HTML template
window = webview.create_window("My Graph", html=template)

# start the webview event loop
webview.start()
