import time
time.clock()

import queue as Q


from Graph import Graph

SOURCE = 0
from Solution import Solution


class Node(object):
    def __init__(self, v, sol, heuristic_cost=0):
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
                new_node = Node(not_visited, new_solution, heuristic_cost=0)
                heap.put((new_node.solution.cost,new_node))
##                print('     Sol potentielle: ',new_node.solution.visited,' Cout (g) = ',new_node.solution.cost)

    def __lt__(self, other):
        if isinstance(other, Node):
            isN2betterThanN1(other, self)
        else:
            raise ValueError('you should give a Node for comparison')


def main():
    g = Graph('N12.data')
    import Kruskal
    Kruskal.kruskal = Kruskal.Kruskal(g)
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
##            print(' ')
##            print('Voici la solution courante: ', current_node.solution.visited)
##            print('     non-visites: ', current_node.solution.not_visited)
##            print('     Cout: ', current_node.solution.cost)
##            print('   Nb fils: ',len(current_node.solution.not_visited)-1,'   Nb noeuds crees: ',nCreated,'  Nb noeuds explores: ',nExplored)
            trial = trial + 1

    print(' ')
    print('TERMINE')
    print('Voici la solution finale: ', current_node.solution.visited)
    print(' ')
    print('SOLUTION PROPOSEE: ')
    current_node.solution.print_solution()
    print('Noeuds crees: ',nCreated,'   Noeuds explores: ',nExplored)
    print('CPU Time (sec): ',time.clock())


def isN2betterThanN1(N1, N2):
    if N2.solution.cost <= N1.solution.cost:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
