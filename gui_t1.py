import tkinter as tk
from tkinterweb import HtmlFrame

import networkx as nx
import json


# create the Tkinter window
root = tk.Tk()
#root.geometry("800x600")

# create the WebView widget and load the PyVis visualization HTML file
webview = HtmlFrame(root)
webview.load_url("https://www.google.com")#"file:///C:/Users/luciu/dEV/think-cloud/mygraph.html")

# pack the widget into the window
webview.pack(expand=tk.YES, fill=tk.BOTH)

# start the Tkinter event loop
root.mainloop()