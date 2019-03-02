import time
time.clock()

import queue as Q

from Graph import Graph
from Solution import Solution

SOURCE = 0

class Node(object):
    def __init__(self, v, sol, heuristic_cost):
        self.v = v
        self.solution = sol
        self.heuristic_cost = heuristic_cost

    def explore_node(self, heap):
        for not_visited in self.solution.not_visited:
            if not_visited==SOURCE and len(self.solution.not_visited)>1:
                continue
            else:
                new_solution = Solution(self.solution)
                new_solution.add_edge(self.v, not_visited)
                import Kruskal
                Kruskal.kruskal = Kruskal.Kruskal(new_solution.g)
                heuristic_cost=Kruskal.kruskal.getMSTCost(new_solution,SOURCE)
                new_node = Node(not_visited, new_solution, heuristic_cost)
                heap.put((new_node.solution.cost+new_node.heuristic_cost,new_node))

    def __lt__(self, other):
        if isinstance(other, Node):
            isN2betterThanN1(other, self)
        else:
            raise ValueError('you should give a Node for comparison')


def main():
    g = Graph('N12.data')
    import Kruskal

    heap = Q.PriorityQueue()
    finish = 0
    current_node = Node(SOURCE, Solution(g), heuristic_cost=0)
    nCreated=1
    nExplored=0
    print('Debut: ',current_node.solution.visited)
    trial = 0
    while not finish and trial <= 1E9:
        if len(current_node.solution.visited)>=g.N + 1:
            finish = 1
            trial = trial + 1
        else:
            current_node.explore_node(heap)
            nExplored+=1
            nCreated+=(len(current_node.solution.not_visited)-1)
            current_node = heap.get()[1]
            """
            print(' ')
            print('Voici la solution courante: ', current_node.solution.visited)
            print('     non-visites: ', current_node.solution.not_visited)
            print('     Cout (g): ', current_node.solution.cost,'   Valeur (g+h): ',current_node.solution.cost+current_node.heuristic_cost)
            print('   Nb fils: ',len(current_node.solution.not_visited)-1,'   Nb noeuds crees: ',nCreated,'  Nb noeuds explores: ',nExplored)
            trial = trial + 1
            """""

    print(' ')
    print('TERMINE')
    print('Voici la solution finale: ', current_node.solution.visited)
    print(' ')
    print('SOLUTION PROPOSEE: ')
    current_node.solution.print_solution()
    print('Noeuds crees: ',nCreated,'   Noeuds explores: ',nExplored)
    print('CPU Time (sec): ',time.clock())


"""
def isN2betterThanN1(N1, N2):
    if (N2.solution.cost + N2.heuristic_cost) <= (N1.solution.cost + N1.heuristic_cost):
        if (N2.solution.cost + N2.heuristic_cost) == (N1.solution.cost + N1.heuristic_cost):
            vproche2=[N2.solution.g.get_edge(N2.v,x).cost for x in N2.solution.not_visited]
            vproche2.append(1E9)
            vproche1=[N1.solution.g.get_edge(N2.v,x).cost for x in N1.solution.not_visited]
            vproche1.append(1E9)
            min_vproche2 = min(vproche2)
            min_vproche1 = min(vproche1)
            return min_vproche2 <= min_vproche1
        return True
    else:
        return False
        """


""" Destination
def isN2betterThanN1(N1, N2):
    if (N2.solution.cost + N2.heuristic_cost) <= (N1.solution.cost + N1.heuristic_cost):
        if (N2.solution.cost + N2.heuristic_cost) == (N1.solution.cost + N1.heuristic_cost):
            vproche2=[N2.solution.g.get_edge(SOURCE,x).cost for x in N2.solution.not_visited]
            vproche2.append(1E9)
            vproche1=[N1.solution.g.get_edge(SOURCE,x).cost for x in N1.solution.not_visited]
            vproche1.append(1E9)
            min_vproche2 = min(vproche2)
            min_vproche1 = min(vproche1)
            return min_vproche2 <= min_vproche1
        return True
    else:
        return False
        """

#"""
def isN2betterThanN1(N1, N2):
    if (N2.solution.cost + N2.heuristic_cost) <= (N1.solution.cost + N1.heuristic_cost):
        return True
    else:
        return False
#"""



if __name__ == '__main__':
    main()
