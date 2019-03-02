import numpy as np

kruskal = None


class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parent = np.array(range(n))
        self.rnk = np.zeros(n)

    def reset(self):
        self.parent = np.array(range(self.n))
        self.rnk = np.zeros(self.n)

    def add(self, e):
        x = self.find(e.source)
        y = self.find(e.destination)

        if self.rnk[x] > self.rnk[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
        if self.rnk[x] == self.rnk[y]:
            self.rnk[y] += 1

    def makes_cycle(self, e):
        return self.find(e.source) == self.find(e.destination)

    def find(self, u):
        if u != self.parent[u]:
            return self.find(self.parent[u])
        else:
            return u

from Solution import Solution
from Graph import Graph, Edge

class Kruskal(object):
    def __init__(self, g):
        self.uf = UnionFind(g.N)
        self.g = g

    def getMSTCost(self, sol, source):
        if not isinstance(sol, Solution):
            print('ERREUR: Envoyer un objet Solution !')
        else:
            MST=[]
            costMST=0;

            for i in range(len(sol.visited)-1):
                E=self.g.get_edge(sol.visited[i],sol.visited[i+1])
                self.uf.add(E)
                MST.append((E.source,E.destination))


            for E in self.g.get_sorted_edges():
                if not self.uf.makes_cycle(E):# and (E.source not in sol.visited[1:-1] and E.destination not in sol.visited[1:-1] ):
                    self.uf.add(E)
                    MST.append((E.source,E.destination))
                    costMST+=E.cost
#            print('     New sol: ',sol.visited,' de cout g = ',sol.cost,'   Arbre MST: ',MST, ' de cout H = ',costMST,';  h+g = ',sol.cost+costMST)
            return costMST

