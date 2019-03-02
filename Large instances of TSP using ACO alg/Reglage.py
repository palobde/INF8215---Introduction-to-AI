from ACO import ACO
from Solution import Solution
import copy
import time
time.clock()


if __name__ == '__main__':


    """*********** REGLAGE Q0 ************* """
    Param = 'Reglage_q0' #<-------------------------------------------
 #   file1 = open(Param + '.dat', 'w')
 #   file2 = open(Param + '_sol.dat', 'w')

    Reglage = []

    Param_values = [0.95, 0.9, 0.75, 0.5, 0.25] #<-------------------------------------------
    for value in Param_values:

        costs_list = []
        cpu_lists = []

        for case in range(5):

            start_time = time.time()

            aco = ACO(value, 2, 0.1, 0.1, 10, 'qatar') #<-------------------------------------------
            aco.runACO(10)

            costs_list.append()

            end_time = time.time()
            cpu_time = end_time - start_time

            cpu_lists.append(cpu_time)

        Reglage.append([aco.parameter_q0, sum(costs_list)/len(costs_list), sum(cpu_lists)/len(cpu_lists)]) #<-------------------------------
        print(Param+'= '+ str(aco.parameter_q0)+ ' val= '+ str(value)+ ' Cout= '+ str(aco.best.cost) + ' Temps(s)= ' + str(cpu_time)) #<-------------------------------

    file1 = open(Param + '.dat', 'w')
    for line in  Reglage:
        file1.write(Param+'= '+ str(aco.parameter_q0)+ ' Cas= '+ str(case+1)+ ' Cout= '+ str(aco.best.cost) + ' Temps(s)= ' + str(cpu_time) +'\n') #<-------------------------------
    file1.close()





    """*********** REGLAGE BETA ************* """
    Param = 'Reglage_beta' #<-------------------------------------------
    file1 = open(Param + '.dat', 'w')
 #   file2 = open(Param + '_sol.dat', 'w')

    Param_values = [0.25, 0.5, 1.0, 2.0, 5.0] #<-------------------------------------------
    for value in Param_values:
        for case in range(5):

            start_time = time.time()

            aco = ACO(0.9, value, 0.1, 0.1, 10, 'qatar') #<-------------------------------------------
            aco.runACO(1000)

            end_time = time.time()
            cpu_time = end_time - start_time

            file1.write(Param+ '= '+ str(aco.parameter_beta)+ ' Cas= '+ str(case+1)+ ' Cout= '+ str(aco.best.cost) + ' Temps(s)= ' + str(cpu_time) +'\n') #<-------------------------------
            file2.write(Param+ '= '+ str(aco.parameter_beta)+ ' Cas= '+ str(case+1)+ ' Long= '+ str(len(aco.best.visited)-1) + ' Sol: ' + str(aco.best.visited)+'\n')#<--------------------

        file1.write('\n')
 #       file2.write('\n')

    file1.close()
 #   file2.close()



    """*********** REGLAGE RHO ************* """
    Param = 'Reglage_rho' #<-------------------------------------------
    file1 = open(Param + '.dat', 'w')
#    file2 = open(Param + '_sol.dat', 'w')

    Param_values = [0.05, 0.1, 0.25, 0.5, 0.9] #<-------------------------------------------
    for value in Param_values:
        for case in range(5):

            start_time = time.time()

            aco = ACO(0.9, 2, value, 0.1, 10, 'qatar') #<-------------------------------------------
            aco.runACO(1000)

            end_time = time.time()
            cpu_time = end_time - start_time

            file1.write(Param+'= '+ str(aco.parameter_rho)+ ' Cas= '+ str(case+1)+ ' Cout= '+ str(aco.best.cost) + ' Temps(s)= ' + str(cpu_time) +'\n') #<-------------------------------
#            file2.write(Param+'= '+ str(aco.parameter_rho)+ ' Cas= '+ str(case+1)+ ' Long= '+ str(len(aco.best.visited)-1) + ' Sol: ' + str(aco.best.visited)+'\n')#<--------------------

        file1.write('\n')
  #      file2.write('\n')

    file1.close()
  #  file2.close()



    """*********** REGLAGE PHI ************* """
    Param = 'Reglage_phi' #<-------------------------------------------
    file1 = open(Param + '.dat', 'w')
  #  file2 = open(Param + '_sol.dat', 'w')

    Param_values = [0.05, 0.1, 0.25, 0.5, 0.9] #<-------------------------------------------
    for value in Param_values:
        for case in range(5):

            start_time = time.time()

            aco = ACO(0.9, 2, 0.1, value, 10, 'qatar') #<-------------------------------------------
            aco.runACO(1000)

            end_time = time.time()
            cpu_time = end_time - start_time

            file1.write(Param+'= '+ str(aco.parameter_phi)+ ' Cas= '+ str(case+1)+ ' Cout= '+ str(aco.best.cost) + ' Temps(s)= ' + str(cpu_time) +'\n') #<-------------------------------
 #           file2.write(Param+'= '+ str(aco.parameter_phi)+ ' Cas= '+ str(case+1)+ ' Long= '+ str(len(aco.best.visited)-1) + ' Sol: ' + str(aco.best.visited)+'\n')#<--------------------

        file1.write('\n')
 #       file2.write('\n')

    file1.close()
  #  file2.close()



    """*********** REGLAGE K ************* """
    Param = 'Reglage_K' #<-------------------------------------------
    file1 = open(Param + '.dat', 'w')
 #   file2 = open(Param + '_sol.dat', 'w')

    Param_values = [1, 10, 50, 100, 500] #<-------------------------------------------
    for value in Param_values:
        for case in range(5):

            start_time = time.time()

            aco = ACO(0.9, 2, 0.1, 0.1, value, 'qatar') #<-------------------------------------------
            aco.runACO(1000)

            end_time = time.time()
            cpu_time = end_time - start_time

            file1.write(Param+'= '+ str(aco.parameter_K)+ ' Cas= '+ str(case+1)+ ' Cout= '+ str(aco.best.cost) + ' Temps(s)= ' + str(cpu_time) +'\n') #<-------------------------------
 #           file2.write(Param+'= '+ str(aco.parameter_K)+ ' Cas= '+ str(case+1)+ ' Long= '+ str(len(aco.best.visited)-1) + ' Sol: ' + str(aco.best.visited)+'\n')#<--------------------

        file1.write('\n')
 #       file2.write('\n')

    file1.close()
#    file2.close()
