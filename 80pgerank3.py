import networkx as nx
u=nx.Graph() #undirected graph

G=nx.DiGraph()
print(G.nodes())
G.add_nodes_from([i for i in range(5)])
print(G.nodes())

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)
G.add_edge(2,4)
G.add_edge(2,1)
G.add_edge(4,3)
G.add_edge(3,4)
G.add_edge(1,4)
print(G.out_edges(1))
print(G.in_edges(3))



