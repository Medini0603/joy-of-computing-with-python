from cv2 import sort
import networkx as nx
import matplotlib.pyplot as plt
import random

G=nx.gnp_random_graph(10,0.5,directed="True")
nx.draw(G,with_labels="True")
plt.show()

#x is a random source node
x=random.choice([i for i in range(G.number_of_nodes())])

dict_count={}
for i in range(G.number_of_nodes()):
    dict_count[i]=0
print(dict_count)
dict_count[x]+=1

for i in range(100000):
    list_n=list(G.neighbors(x))
    list_n=list(G.neighbors(x))
    #check for sink
    #if sink choose node randomly from neighbours of x
    if(len(list_n)==0):
        x=random.choice([i for i in range(G.number_of_nodes())])
        dict_count[x]+=1
    else:
        x=random.choice(list_n)
        dict_count[x]+=1


p=nx.pagerank(G) #default function to get page rank value in python

import operator
sorted_p=sorted(p.items(),key=operator.itemgetter(1))
sorted_dict=sorted(dict_count.items(),key=operator.itemgetter(1))
print(sorted_p)
print(sorted_dict)
# print(p)
# print(dict_count)