# take random walk on the network
# increment point on each node 
# find nodes with highest number of points 

# NOTE: crawlers: take random walk on www network and rank the websites. 

# type of people voting also matters along with number of votes a person gets ,to win an election 

# nodes - website
# lines -links 

# Page rank - Random walk algorithm 

# if outdegree is zero then that node is called sink 
# if we get sink then next node is selected randomly from the remaining vertices 

import networkx as nx
import matplotlib.pyplot as plt
g=nx.barbell_graph(4,2)
nx.draw(g)
plt.show()
g=nx.barbell_graph(4,3)
#NOTE First parameter is the number of nodes in each community other param is number of nodes between community
nx.draw(g)
plt.show()

g=nx.complete_graph(4)
nx.draw(g)
plt.show()

g=nx.cycle_graph(5)
nx.draw(g)
plt.show()

g=nx.ladder_graph(4)
nx.draw(g)
plt.show()


import networkx as nx
import matplotlib.pyplot as plt
g=nx.path_graph(6)
nx.draw(g)
plt.show()

import networkx as nx
import matplotlib.pyplot as plt
g=nx.star_graph(6)  #6 sink nodes 1 hub node
nx.draw(g)
plt.show()

import networkx as nx
import matplotlib.pyplot as plt
g=nx.wheel_graph(6)  
nx.draw(g)
plt.show()


import networkx as nx
import matplotlib.pyplot as plt
g=nx.gnm_random_graph(5,0.5)
nx.draw(g)
plt.show()