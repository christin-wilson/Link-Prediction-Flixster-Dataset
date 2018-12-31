import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import operator

fh=open("edges.csv", 'r')
G = nx.read_edgelist(fh, delimiter=',')

H = nx.to_numpy_matrix(G)

def D_cent(G1):
    deg_cent = np.sum(G1, axis=1)
    deg_cent = deg_cent /(len(G1) - 1)
    return list(deg_cent)

#print(D_centrality(H))

centrality_list = np.array(D_cent(H)).reshape(-1,).tolist()
print(centrality_list)
for c in centrality_list:
    print('%d' % c)
    
plt.figure()
plt.hist(centrality_list.values())
plt.show()
