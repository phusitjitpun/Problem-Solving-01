import networkx as nx
import matplotlib.pylab as plt

G = nx.Graph()

G.add_edges_from([('A','B'),('A','M'),('A','L'),('B','C'),('B','D'),
                  ('B','N'),('B','O'),('C','D'),('D','E'),('D','O'),
                  ('E','F'),('F','G'),('F','N'),('G','H'),('H','N'),
                  ('H','I'),('H','P'),('P','O'),('P','I'),('P','M'),
                  ('I','J'),('J','K'),('K','M'),('K','L'),])

Alist = nx.all_neighbors(G,'A')
Elist = nx.all_neighbors(G,'E')
Ilist = nx.all_neighbors(G,'I')

A = []
E = []
I = []

for a in Alist :
    A.append(a)
    for n in nx.all_neighbors(G,a) :
        A.append(n)

for e in Elist :
    E.append(e)
    for m in nx.all_neighbors(G,e) :
        E.append(m)

for i in Ilist :
    I.append(i)
    for j in nx.all_neighbors(G,i) :
        I.append(j)

for q in A :
    for k in E :
        for p in I :
            if q == k == p :
                print(q)
print(A)
print(E)
print(I)
