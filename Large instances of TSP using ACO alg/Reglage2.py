from ACO import ACO
from Solution import Solution
import copy
import time
time.clock()


if __name__ == '__main__':


    """*********** REGLAGE Q0 ************* """
    Param = 'Reglage_q0' #<-------------------------------------------
    Reglages = []

    Param_values = [0.95, 0.9, 0.75, 0.5, 0.25] #<-------------------------------------------

    for value in Param_values:

        costs_list = []
        cpu_lists = []

        for case in range(5):

            start_time = time.time()

            aco = ACO(value, 2, 0.1, 0.1, 10, 'qatar') #<-------------------------------------------
            aco.runACO(100)

            costs_list.append(aco.best.cost)

            end_time = time.time()
            cpu_time = end_time - start_time

            cpu_lists.append(cpu_time)

            mean_cost = sum(costs_list)/len(costs_list)
            mean_cpu = sum(cpu_lists)/len(cpu_lists)

        Reglages.append([aco.parameter_q0, mean_cost, mean_cpu]) #<-------------------------------
        print(Param+'= '+ str(aco.parameter_q0)+ ' val= '+ str(value)+ ' CoutMoy= '+ str(mean_cost)+ ' TempsMoy(s)= '+ str(mean_cpu)) #<-------------------------------

    file1 = open(Param + '.dat', 'w')
    for line in  Reglages:
        file1.write(str(line) +'\n')
    file1.close()





    """*********** REGLAGE BETA *************"""
    Param = 'Reglage_beta' #<-------------------------------------------
    Reglages = []

    Param_values = [0.25, 0.5, 1.0, 2.0, 5.0, 7.0, 10.0] #<-------------------------------------------

    for value in Param_values:

        costs_list = []
        cpu_lists = []

        for case in range(5):

            start_time = time.time()

            aco = ACO(0.9, value, 0.1, 0.1, 10, 'qatar') #<-------------------------------------------
            aco.runACO(100)

            costs_list.append(aco.best.cost)

            end_time = time.time()
            cpu_time = end_time - start_time

            cpu_lists.append(cpu_time)

            mean_cost = sum(costs_list)/len(costs_list)
            mean_cpu = sum(cpu_lists)/len(cpu_lists)

        Reglages.append([aco.parameter_beta, mean_cost, mean_cpu]) #<-------------------------------
        print(Param+'= '+ str(aco.parameter_beta)+ ' val= '+ str(value)+ ' CoutMoy= '+ str(mean_cost)+ ' TempsMoy(s)= '+ str(mean_cpu)) #<-------------------------------

    file1 = open(Param + '.dat', 'w')
    for line in  Reglages:
        file1.write(str(line) +'\n')
    file1.close()



    """*********** REGLAGE RHO *************"""
    Param = 'Reglage_rho' #<-------------------------------------------
    Reglages = []

    Param_values = [0.05, 0.1, 0.25, 0.5, 0.9] #<-------------------------------------------

    for value in Param_values:

        costs_list = []
        cpu_lists = []

        for case in range(5):

            start_time = time.time()

            aco = ACO(0.9, 2, value, 0.1, 10, 'qatar') #<-------------------------------------------
            aco.runACO(100)

            costs_list.append(aco.best.cost)

            end_time = time.time()
            cpu_time = end_time - start_time

            cpu_lists.append(cpu_time)

            mean_cost = sum(costs_list)/len(costs_list)
            mean_cpu = sum(cpu_lists)/len(cpu_lists)

        Reglages.append([aco.parameter_rho, mean_cost, mean_cpu]) #<-------------------------------
        print(Param+'= '+ str(aco.parameter_rho)+ ' val= '+ str(value)+ ' CoutMoy= '+ str(mean_cost)+ ' TempsMoy(s)= '+ str(mean_cpu)) #<-------------------------------

    file1 = open(Param + '.dat', 'w')
    for line in  Reglages:
        file1.write(str(line) +'\n')
    file1.close()



    """*********** REGLAGE PHI *************"""
    Param = 'Reglage_phi' #<-------------------------------------------
    Reglages = []

    Param_values = [0.05, 0.1, 0.25, 0.5, 0.9] #<-------------------------------------------

    for value in Param_values:

        costs_list = []
        cpu_lists = []

        for case in range(5):

            start_time = time.time()

            aco = ACO(0.9, 2, 0.1, value, 10, 'qatar') #<-------------------------------------------
            aco.runACO(100)

            costs_list.append(aco.best.cost)

            end_time = time.time()
            cpu_time = end_time - start_time

            cpu_lists.append(cpu_time)

            mean_cost = sum(costs_list)/len(costs_list)
            mean_cpu = sum(cpu_lists)/len(cpu_lists)

        Reglages.append([aco.parameter_phi, mean_cost, mean_cpu]) #<-------------------------------
        print(Param+'= '+ str(aco.parameter_phi)+ ' val= '+ str(value)+ ' CoutMoy= '+ str(mean_cost)+ ' TempsMoy(s)= '+ str(mean_cpu)) #<-------------------------------

    file1 = open(Param + '.dat', 'w')
    for line in  Reglages:
        file1.write(str(line) +'\n')
    file1.close()



    """*********** REGLAGE K *************"""
    Param = 'Reglage_K' #<-------------------------------------------
    Reglages = []

    Param_values = [1, 10, 50, 100, 500] #<-------------------------------------------

    for value in Param_values:

        costs_list = []
        cpu_lists = []

        for case in range(5):

            start_time = time.time()

            aco = ACO(0.9, 2, 0.1, 0.1, value, 'qatar') #<-------------------------------------------
            aco.runACO(100)

            costs_list.append(aco.best.cost)

            end_time = time.time()
            cpu_time = end_time - start_time

            cpu_lists.append(cpu_time)

            mean_cost = sum(costs_list)/len(costs_list)
            mean_cpu = sum(cpu_lists)/len(cpu_lists)

        Reglages.append([aco.parameter_K, mean_cost, mean_cpu]) #<-------------------------------
        print(Param+'= '+ str(aco.parameter_K)+ ' val= '+ str(value)+ ' CoutMoy= '+ str(mean_cost)+ ' TempsMoy(s)= '+ str(mean_cpu)) #<-------------------------------

    file1 = open(Param + '.dat', 'w')
    for line in  Reglages:
        file1.write(str(line) +'\n')
    file1.close()
