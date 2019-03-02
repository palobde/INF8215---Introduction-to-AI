# -*- coding: utf-8 -*-
import numpy as np

from Graph import Graph
from Solution import Solution

SOURCE = 0


class ACO(object):
    def __init__(self, q0, beta, rho, phi, K, data):
        self.parameter_q0 = q0
        self.parameter_beta = beta
        self.parameter_rho = rho
        self.parameter_phi = phi
        self.parameter_K = K

        self.graph = Graph(data)
        self.best = Solution(self.graph)
        self.best.cost = 99999999999999
        self.pheromone_init = np.ones((self.graph.N, self.graph.N))
        f = open(data + '_init', 'r')
        self.pheromone_init *= float(f.readline())
        self.pheromone = np.ones((self.graph.N, self.graph.N))

    # Fonction qui donne la prochaine ville a visiter par une fourmi k
    def get_next_city(self, sol):
#        print("*Recherche de la prochaine ville ")

        # Initialisation
        next_city = -9999999
        
        # Verifier qu'il existe une ville courante
        if (len(sol.visited) <= 0):
 #           print("  !! Please Give an Initiated Solution !!!")
            return next_city

        # Enlever la ville source (elle est la derniere visitee)
        sol.not_visited.remove(SOURCE)
        if len(sol.not_visited)==0: # S'il n'y a pas d'autres villes a visiter, la remettre
            sol.not_visited.append(SOURCE)
            next_city = 0
            return next_city


        # Ville courante
        i=sol.visited[-1]
 #       print("  Ville courante : ",i)
 #       print("  Villes non visitees : ",sol.not_visited)

        # Valeurs Calculées
        phero_value = self.pheromone[i, sol.not_visited]
        cost_valueBeta = np.array(self.graph.costs[i, sol.not_visited])**self.parameter_beta
        ratio = phero_value/cost_valueBeta
        D_Pk = ratio/sum(ratio) # Distribution

        q = np.random.uniform(0,1) # Choix aleatoire de q

        # Trouver l'indice de la prochaine ville
        if q <= self.parameter_q0:    # Cas 1
            indice=np.argmax(ratio)
        else:                         # Cas 2
            choice = np.random.choice(sol.not_visited, p=D_Pk)
            indice = np.argwhere(np.array(sol.not_visited)==choice)[0][0]
        
        # Convertir l'indice en prochaine ville
        next_city=sol.not_visited[indice]
#        print("  *Prochaine ville: ",next_city)

        # Remettre la ville Source (elle est la derniere visitee)
        sol.not_visited.append(SOURCE)

        return next_city


    def heuristic2opt(self, sol):
#        print(" Solution courante: ",sol.visited)
        nb=len(sol.visited)

        if nb>3:
#            print(' Cout de : ',sol.cost)
            for i in range(nb-3): #On teste jusqu'a 2 villes avant la derniere
                for j in range(i+3, nb):
                    sol2=Solution(sol)
                    sol2.inverser_ville(sol.visited[i],sol.visited[j])
                    sol2.cost = sol2.get_cost(SOURCE)
                    if sol2.cost < sol.cost:
                        sol=Solution(sol2)
                        sol.cost = sol.get_cost(SOURCE)
#                        print(" **Une permutation effectuee !! ")
#                        print("     Solution nouvelle : ",sol.visited)
#                        print("     Cout de : ",sol.cost)
        else:
            print("     Pas assez de villes pour 2-Opt")

#        print(" Solution finale : ",sol.visited)
#        print(" Cout final de : ",sol.get_cost(SOURCE))

        return sol




    def global_update(self, best):
        # Calcul de la matrice Delta_Tau
        l_gb = 1/best.cost
        delta_Tau = np.zeros((self.graph.N,self.graph.N))
        for i in range(self.graph.N):
            a=best.visited[i]
            b=best.visited[i+1]
            delta_Tau[a][b] = l_gb
            delta_Tau[b][a] = l_gb
        # Mise a jour globale des pheromones
        self.pheromone = (1-self.parameter_rho)*self.pheromone + self.parameter_rho*delta_Tau


    def local_update(self, sol):
        # Mise a jour locale des pheromones
        for i in range(len(sol.visited)-1):
            a=sol.visited[i]
            b=sol.visited[i+1]
            value = (1.0 - self.parameter_phi)*self.pheromone[a][b] + self.parameter_phi*self.pheromone_init[a][b]
            self.pheromone[a][b] = value
            self.pheromone[b][a] = value

    def runACO(self, maxiteration):

        # Initialiser la meilleure solution globalement trouvee
        overall_best = Solution(self.graph)
        overall_best.cost = 9999999999999.0

        for iter in range(maxiteration): # Pour chaque iteration

            # Initialiser la meilleure solution pour cette iteration
            iter_best = Solution(self.graph)
            iter_best.cost = 9999999999999.0

            # Pour chacune des K fourmis
            for k in range(self.parameter_K):
                sk = Solution(self.graph) # construction de la solution de chaque fourmis

                # Execution de la recherche locale
                for step in range(self.graph.N): # Boucle chaque ville a visiter (il y en a N)
                    current_city = sk.visited[-1]
                    next_city = self.get_next_city(sk) # Trouver la prochaine ville
                    sk.add_edge(current_city, next_city)
                    # Mise a jour locale des pheromones
                    self.local_update(sk)

                # Mise a jour de la meilleure solution pour cette iteration (iter):
                if sk.cost < iter_best.cost:
                    iter_best = sk

            # Ameliorer la meilleure solution a l'aide de 2-Opt
            self.heuristic2opt(iter_best)

            # mise a jour globale de la pheromone
            self.global_update(iter_best)

            # Mise a jour de la meilleure solution trouvee a date (sur plusieurs iterations)
            if iter_best.cost < overall_best.cost:
                overall_best = iter_best

        #print('*** Meilleure Solution trouvee au cout de : ', overall_best.cost)
        #print(overall_best.visited)

        self.best = overall_best
        return overall_best


