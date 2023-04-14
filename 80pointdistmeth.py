# points distribution method 
# So initially all the nodes are given equal points you can also consider it as some gift items or gold coins anything some item is given to all the three people something equally has been given and they have been ask to play a sort of a game something like that the rule of this game is whatever you are having you should share it equally with all your out edges so we had collected the data of who all you like right

# eg :- A ->B and A->C
#     B->C
#     C->A

# all have 100 each 
# A gives 50 to each B and C
# B gives 100 to C
# C gives 100 to A

# so C-150
# A-100
# B-50

# continue this process  for many iterations...

#After some times it converges
#i.e. diffrence between currrent iteration and previous iteration is 0 or negligible 
#but total sum always remains constant i.e.300
import networkx as nx
import random
import matplotlib.pyplot as plt
def addedges(G):
    nodes=list(G.nodes())

    for s in nodes:
        for t in nodes:
            if(s!=t):
                #add edge with probability 0.5
                r=random.random()
                if(r<=0.5):
                    G.add_edge(s,t)
    return G

def assignpoints(G):
    nodes=list(G.nodes())
    p=[]
    for each in nodes:
        p.append(100)
    return p


def distributepoints(G,points):
    nodes=list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
    for n in nodes:
        out=list(G.out_edges(n))
        if(len(out)==0):
            new_points[n]+=points[n]
        else:
            share=points[n]/len(out)
            for (src,target) in out:
                new_points[target]+=share
    return new_points


def keepdistributing(points,G):
    while(1):
        newpoints=distributepoints(G,points)
        print(newpoints)
        points=newpoints
        stop=input("Enter # to stop other symbol to continue")
        if(stop=='#'):
            break
    return newpoints

def rankbypoints(finalpoints):
    d={}
    for i in range(len(finalpoints)):
        d[i]=finalpoints[i]
    print(sorted(d.items(),key=lambda f:f[1]))



G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G=addedges(G)

nx.draw(G,with_labels="True")
plt.show()

# Assign initial points 
points=assignpoints(G)

# Keep distributing the points 
finalpoints=keepdistributing(points,G)

#rank by points
rankbypoints(finalpoints)
result=nx.pagerank(G)
print(sorted(result.items(),key=lambda f:f[1]))