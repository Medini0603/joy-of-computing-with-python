import networkx as nx
import matplotlib.pyplot as plt

# random graph 
# G=nx.gnp_random_graph(50,0.3)
# nx.draw(G)
# plt.show()
# print(G.nodes())
# print(G.edges())
# print(G.degree(0))

#scale free graph
# In starting there are very few nodes for example there are two nodes and then at each iteration a new node comes and whenever the new node comes it comes with two edges and these two edges get connected to those node which has higher degree so the probability of getting connected to already existing node is higher for that node whose degree is very high. So this how this process happens and at the end the node which is having higher degree at the end will have more degree so and there will be having few nodes of having high degree and very highnumber of nodes having very low degree so this is known as scale free graph

# preferantial attachment :- -- new nodes when they come they prefer to attach to old nodes which are having higher degree.
G=nx.barabasi_albert_graph(5,2)
nx.draw(G)
plt.show()
print(G.nodes())
print(G.edges())
print(G.degree(0))

nx.write_gexf(G,"analysis1.gexf")
