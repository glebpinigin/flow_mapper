import networkx as nx
from shapely.geometry import LineString
import numpy as np
from shapely import wkt

class SpiralTree(nx.DiGraph):
    
    def __init__(self, root, bias):
        super().__init__()
        self.root = root
        self.add_node(self.root)
        self.bias = bias
    
    def insertLeaf(self, R):
        self.add_node(R)
        self.add_edge(self.root, R, type="root-connection", volume=R.volume)
    
    def insertSteinerNode(self, steiner_R=None, leaf1_R=None, leaf2_R=None):
        self.add_node(steiner_R)
        self.add_edge(self.root, steiner_R, type="root-connection")
        for leaf_R in (leaf1_R, leaf2_R):
          self.remove_edge(self.root, leaf_R)
          self.add_edge(steiner_R, leaf_R, type="st-connection", volume=leaf_R.volume)
    
    def repairUnderlying(self, close_R, far_R):
        self.remove_edge(self.root, far_R)
        self.add_edge(close_R, far_R, type="false-connection", volume=far_R.volume)
        nx.set_edge_attributes(self, {(self.root, close_R): close_R.volume}, name="volume")

def connectionsToWkt(T: SpiralTree):
    biasX, biasY = T.bias
    bias = np.array((biasX, biasY))
    for node1, node2, data in T.edges.data():
        if data["type"] == "root-connection":
            node1_crds = np.array(node1) + bias
            leaf = np.array(node2.leaf) + bias
            crds = (node1_crds, leaf)
            line = LineString(crds)
            wkt = line.wkt
            nx.set_edge_attributes(T, {(node1, node2): wkt}, name="Wkt")
        else:
            R = node2
            tp = R.tp
            crds = R.crds[f"{tp}_xy"]
            crds = np.column_stack(crds)
            crds = crds + bias
            line = LineString(crds)
            wkt = line.wkt
            nx.set_edge_attributes(T, {(node1, node2): wkt}, name="Wkt")

    # for node1, node2, data in T.edges.data():
    #     if data["type"] == "root-connection":
    #         xx = (node1[0], node2.leaf[0])
    #         yy = (node1[1], node2.leaf[1])
    #     else:
    #         R = node2
    #         tp = R.tp
    #         xx, yy = R.crds[f"{tp}_xy"]
    #     nx.set_edge_attributes(T, {(node1, node2): (xx, yy)}, name="loc")
    
    # for node, data in T.nodes.data():
    #     if node == T.root:
    #         x = T.root[0]
    #         y = T.root[1]
    #     else:
    #         x = node.leaf[0]
    #         y = node.leaf[1]
    #     nx.set_node_attributes(T, {node: (x, y)}, 'loc')

def spiraltreeToPandas(T):
    pdtb = nx.to_pandas_edgelist(T)
    pdtb["Wkt"] = pdtb["Wkt"].apply(wkt.loads)
    return pdtb