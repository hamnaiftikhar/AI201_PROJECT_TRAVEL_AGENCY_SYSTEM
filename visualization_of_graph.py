import networkx as nx
import matplotlib.pyplot as plt
   
  
# Defining a Class
class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          
   # function to visualize the graph
    def visualize(self):
        plt.figure(figsize=(18,20))
        G = nx.Graph()
        G.add_edges_from(self.visual)
        
        graph_pos = nx.spring_layout(G)
        nx.draw(G, graph_pos,with_labels=True, node_size=4000, node_color="skyblue", node_shape="o", alpha=1, linewidths=1, font_size=20, 
        font_color="black", font_weight="bold", width=1, edge_color="black")
        plt.show()
