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
        """
            Calculer le cout minimal de l'arbre couvrant minimal
            :param sol:
            :param source:
            :return:
            """
    # Initialiser le unionfind
    self.uf.reset()
    mst_cost = 0

    if A_star.WITH_IMPROVEMENT == False :
    for i in range(len(sol.visited)-1):
        E = self.g.get_edge(sol.visited[i],sol.visited[i+1])
    self.uf.add(E)

    if A_star.MST_WITH_NOT_VISITED_TOWN:
        last_visited_town = sol.visited[len(sol.visited) - 1]
    near_town = last_visited_town
    near_town_min_distance = math.inf
    for t in range(sol.g.getN()):
        if t != last_visited_town:
            near_town_min_distance = min(near_town_min_distance, sol.g.get_edge(last_visited_town, t).cost)
    near_town = t
    E = self.g.get_edge(last_visited_town, t)
    if not self.uf.makes_cycle(E):
        self.uf.add(E)
    mst_cost += E.cost

    if A_star.MST_WITH_MIN_DISTANCE_FROM_SOURCE:
        min_distance_from_source = math.inf
        near_town_from_source = A_star.SOURCE
    for t in sol.not_visited:
        if t != A_star.SOURCE:
            min_distance_from_source = min(min_distance_from_source, sol.g.get_edge(near_town_from_source, t).cost)
            near_town_from_source = t
    E = self.g.get_edge(A_star.SOURCE, near_town_from_source)
    if not self.uf.makes_cycle(E):
        self.uf.add(E)
    mst_cost += E.cost

    for edges in self.g.get_sorted_edges():
        if not self.uf.makes_cycle(edges):
        self.uf.add(edges)
    mst_cost += edges.cost

    else :
    for edges in self.g.get_sorted_edges():
        # Verifier si le sommet courant n'est pas dans la solution
        if (edges.source not in sol.visited[1:-1] and edges.destination not in sol.visited[1:-1]):
    if not self.uf.makes_cycle(edges):
        self.uf.add(edges)
    mst_cost += edges.cost
