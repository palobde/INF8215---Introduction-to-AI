import time
time.clock()

import queue as Q

from Graph import Graph
from Solution import Solution

def main():
    # Initialisation and input data
    g = Graph('N17.data')   #Graph
    opt_val=0
    max_iter=1000           #Max iterations allowed
    iter = 0                #Iteration indicator
    tabu = []
    town=0
    no_update=0
    heap = Q.PriorityQueue()
    history=[]

    # Initial solution:
    current_sol=Solution(g)
    for i in range(g.N)[0:-1]:
        current_sol.add_edge(i,i+1)
    current_sol.cost+=g.get_edge(g.N-1,0).cost
    best_solution = Solution(current_sol)
    print("Solution initale: ", current_sol.visited, "  Cout = ", current_sol.cost, '   f_Cout = ', eval_sol(current_sol))


    # -----Local search loop--------
    while current_sol.cost > opt_val and iter <= max_iter:

        #Find position of current switching town
        print(' ')
        print("Solution Courante: ", current_sol.visited, "  Cout = ", current_sol.cost)
        position = current_sol.visited.index(town)
        print('Ville a changer: ',town, '      A la position = ',position)


        # Explore and evaluate current solution neighbors
        del heap
        heap = Q.PriorityQueue()
        print('Q vide? : ',heap.empty())
        for i in range(len(current_sol.visited)):
            v = current_sol.visited[i]
            if v != town and v not in tabu: # explore all possible neighbors
                neighbor=Solution(current_sol)
                neighbor.visited=[]
                for j in range(len(current_sol.visited)):
                    if j !=i and j != position:
                        neighbor.visited.append(current_sol.visited[j])
                    else:
                        if j==position:
                            neighbor.visited.append(v)
                        else:
                            neighbor.visited.append(town)

                # Evaluate neighbor
                neighbor.cost = eval_sol(neighbor)
                heap.put((neighbor.cost,neighbor)) # Add neighbor to the priority queue
                print(' Neighnor ', i, ' : ',neighbor.visited, '    cost = ',neighbor.cost)

        # Get best neighbor
        best_neighbor = heap.get()[1]
        print(' Meilleur Voisin: ', best_neighbor.visited, '    cost = ', best_neighbor.cost)

        #Update new current solution
        if best_neighbor.cost < current_sol.cost:
            current_sol=Solution(best_neighbor)
            no_update=0
            if best_neighbor.cost < best_solution.cost:
                best_solution=Solution(best_neighbor)
                history.append([time.clock(), iter])
                print('NEW BEST SOLUTION !! ',best_solution.visited, 'COST = ', best_solution.cost)
        else:
            if no_update < g.N:
                no_update+=1
                print(' No update = ', no_update)
            else:
                current_sol=Solution(best_neighbor)
                no_update=0
                tabu = [town]
                print('Degradation: ',best_solution.cost, 'TABOU = ', tabu)

        # Update iteration counter
        town = (town+1)%g.N # new switching town
        iter+=1

    # PRINT
    print(' ')
    print('---- TERMINÉ ----')
    print('Meilleure Solution Trouvee: ', best_solution.visited, ' COUT = ', best_solution.cost)
    print('CPU Time (sec): ',time.clock(), '    Nb Iterations = ', iter)
    print('Meilleur trouvé à CPU Time (sec): ',history[-1][0], '    Et à nb Iterations = ', history[-1][1])



# Function that evaluates a solution
def eval_sol(sol):
    sol.cost=0
    for i in range(len(sol.visited)):
        sol.cost+=sol.g.get_edge(sol.visited[i-1],sol.visited[i]).cost
    return sol.cost



if __name__ == '__main__':
    main()
