import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([('A','B'),('A','C'),('A','D'),('C','K'),('K','G'),('G','H'),
                  ('B','H'),('B','G'),('D','E'),('E','Z'),('H','J'),('F','J'),('J','Z'),
                  ('B','K'),('H','E'),('H','F')])

D = set()
l = input('Enetr : ')
Alist = nx.neighbors(G,l)
for i in Alist :
  F = nx.neighbors(G,i)
  for j in F :
    if i in j :
      pass
    else :
      D.add(j)

for i in nx.neighbors(G,l) :
  if i in D :
    D.remove(i)
    
D.remove(l)
print(D)