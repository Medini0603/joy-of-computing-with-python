import networkx as nx
import matplotlib.pyplot as plt
# to create graph
G=nx.Graph()

# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# print(G.nodes())

# G.add_edge(1,2)
# G.add_edge(1,3)
# G.add_edge(2,3)
# print(G.edges())

# nx.draw(G)
# plt.show()

# create list of nodes and add it 
l=[1,2,3]
G.add_nodes_from(l)

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,3)
print(G.edges())

nx.draw(G)
plt.show()

g1=nx.complete_graph(20)
nx.draw(g1)
plt.show()

# gnp_random_graph(n, p[, seed, directed])
# Returns a  random graph, also known as an Erdős-Rényi graph or a binomial graph.
# random graph 


# RAndom graph is a graph where an edge between each pair of nodes is generated randomly with a fixed probability .Also the indef=gree of each node is nearer to an average indegree calculated using probability and number of nodes
G2=nx.gnp_random_graph(20,0.2)
nx.draw(G2)
plt.show()