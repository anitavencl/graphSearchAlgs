#!/usr/bin/env python
# coding: utf-8

# In[8]:


import networkx as nx
import matplotlib.pylab as plt

graph = {
    'A': ['B', 'S'],
    'B': ['A'],
    'C': ['D', 'E', 'F', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['C', 'G'],
    'G': ['F', 'S'],
    'H': ['E', 'G'],
    'S': ['A', 'C', 'G']
}

G = nx.Graph(graph)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)

plt.show()

# In[39]:


closed = []
status = {}
parent = {}
goal = "D"
path = []
for node in graph:
    status[node] = "W"
    parent[node] = None


def traverseDFS(n):
    global goal
    status[n] = "G"
    closed.append(n)

    for m in graph[n]:

        if status[m] == "W":
            parent[m] = n
            traverseDFS(m)
        if m == goal:
            path.append(n)
            goal = n
    status[n] = "B"


# In[40]:


traverseDFS("A")

print(path)

# In[ ]:




