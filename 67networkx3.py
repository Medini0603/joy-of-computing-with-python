# from platform import node


# edge
# node
# direct edge 
# path 
# shortest path
# connected graph 
# edge list repesentation

# NOTE:  ^ degrees of seperation means any two people in this world are seperated by a hop distance of 6 persons on an average
#i.e. say if i have 100 friends then say each of 100 friends have 100 friends each then i know 100000 persons in a gap of 1 hop so in avg of 6 hops entire world's population is covered 
import networkx as nx
import numpy
G=nx.read_edgelist(r"facebook_combined.txt")
N=list(G.nodes())
# print(N)
spll=[]  #shortest path lenght list 

for u in N:
    for v in N:
        if(u!=v):
            l=nx.shortest_path_length(G,u,v)
            print("Shortest Path Length between ",u, " and ",v ," is = ", l)
            spll.append(l)

min_spll=min(spll)
max_spll=max(spll)
avg_spll=numpy.average(spll)


print("Minimum shortest path length = ",min_spll)
print("Maximum shortest path length = ",max_spll)
print("Average shortest path length = ",avg_spll)


