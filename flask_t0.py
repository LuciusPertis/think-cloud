from flask import Flask, render_template
from pyvis.network import Network

app = Flask(__name__)

# Define a route to serve the PyVis visualization
@app.route('/network')
def network():
    # Create a PyVis visualization of your graph
    net = Network()
    net.add_node(1)
    net.add_node(2)
    net.add_edge(1, 2)

    # Render the PyVis visualization in an HTML template
    return net.generate_html('network.html')

if __name__ == '__main__':
    app.run(debug=True)
