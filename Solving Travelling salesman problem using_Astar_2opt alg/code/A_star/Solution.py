import copy

from Graph import Graph


class Solution(object):
    def __init__(self, s):
        if isinstance(s, Graph):
            self.g = s
            self.cost = 0
            self.visited =[0] #[SOURCE] #
            self.not_visited = [x for x in range(s.getN())]
        elif isinstance(s, Solution):
            self.g = s.g
            self.cost = s.cost
            self.visited = [node for node in s.visited]
            self.not_visited = [node for node in s.not_visited]
        else:
            raise ValueError('you should give a graph or a solution')

    def add_edge(self, v, u):
        self.cost += self.g.get_edge(v,u).cost
        self.visited.append(u)
        self.not_visited.remove(u)

    def print_solution(self):
        for node in self.visited:
            print(node)
        print("COST = {}".format(self.cost))

    def __lt__(self, other):
        if isinstance(other, Solution):
            isN2betterThanN1(other, self)
        else:
            raise ValueError('you should give a Solution for comparison')



# Overload ineq function for priorityQ
def isN2betterThanN1(N1, N2):
    if N2.cost <= N1.cost:
        return True
    else:
        return False

