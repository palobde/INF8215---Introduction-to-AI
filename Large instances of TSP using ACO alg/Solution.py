import numpy as np

from Graph import Graph


class Solution(object):
    def __init__(self, s=None):
        if isinstance(s, Graph):
            self.g = s
            self.cost = 0
            self.visited = []
            self.not_visited = list(range(s.N))
            # Rajout a Solution de la ville SOURCE de depart (0)
            self.visited.append(0)

        elif isinstance(s, Solution):
            self.g = s.g
            self.cost = s.cost
            self.visited = s.visited[:]
            self.not_visited = s.not_visited[:]
        else:
            raise ValueError('you should give a graph or a solution')

    def add_edge(self, v, u):
        # print(u)
        self.cost += self.g.get_edge(v, u).cost
        self.visited.append(u)
        self.not_visited.remove(u)

    def printer(self):
        s = '['
        for i in self.visited:
            s += str(i) + ', '
        s = s[:-2]
        s += ']'
        print(s)
        print('cost: ' + str(self.cost))

    def inverser_ville(self, i, j):
        vis = np.array(self.visited)
        pos_i=np.argwhere(np.array(self.visited)==i)[0][0]
        pos_j=np.argwhere(np.array(self.visited)==j)[0][0]
        if pos_j < pos_i:
            return self.inverser_ville(j, i)
        vis[range(pos_i + 1, pos_j)] = vis[range(pos_j-1, pos_i, -1)]
        self.visited = list(vis)

    def get_cost(self, Source):
        v = Source
        c = 0
        for i in self.visited:
            c += self.g.costs[v, i]
            v = i
        return c


"""
    def inverser_ville(self, i, j): # !!! i et j ne sont pas des villes mais des positions de villes dans la liste des visites
        if j < i:
            return self.inverser_ville(j, i)
        vis = np.array(range(len(self.visited)))
        print("etape 1 :  ",vis)
        print("etape 1.5 :  ", vis[range(i+1, j)])
        print("etape 1.6 :  ", vis[range(j-1, i, -1)])
        vis[range(i+1, j)] = vis[range(j-1, i, -1)]
        #print("etape 2 :  ",vis)
        A = [self.visited[ind] for ind in vis]
        self.visited=A
        print("etape 3 :  ",self.visited)

        """