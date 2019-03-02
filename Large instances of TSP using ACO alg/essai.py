    def runACO(self, maxiteration):

        # Initialiser la meilleure solution globalement trouvee
        overall_best = Solution(self.graph)
        overall_best.cost = 9999999999999.0

        for iter in range(1,maxiteration+1): # Pour chaque iteration

            # Creation de K fourmis et construction de la solution de chaque fourmis
            sk_list = [Solution(self.graph) for k in range(self.parameter_K)]

            # Execution de la recherche locale
            for step in range(self.graph.N): # Boucle chaque ville a visiter (il y en a N)
                for sk in sk_list: # Boucle pour chaque fourmi
                    current_city = sk.visited[-1]
                    next_city = self.get_next_city(sk) # Trouver la prochaine ville
                    sk.add_edge(current_city, next_city)
                    # Mise a jour locale des pheromones
                    self.local_update(sk)

            # Rechercher la meilleure solution pour cette iteration (iter):
            sk_costs = np.array([sk.cost for sk in sk_list])
            indice = np.argmax(sk_costs)
            iter_best = sk_list[indice]

            # Ameliorer la meilleure solution a l'aide de 2-Opt
            self.heuristic2opt(iter_best)

            # mise a jour globale de la pheromone
            self.global_update(iter_best)

        # Mise a jour de la meilleure solution trouvee a date (sur plusieurs iterations)
        if iter_best.cost < overall_best.cost:
            overall_best = iter_best

        print('*** Meilleure Solution trouvee au cout de : ', overall_best.cost)
        print(overall_best.visited)

        self.best = overall_best
        return overall_best