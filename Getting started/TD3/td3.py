#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 19:25:06 2022

@author: steven
"""
import random
echec_dim = 8

# %% zone de la classe
class Individu:
    def __init__(self, vals = None):
        if vals == None:
            self.val = random.sample(range(echec_dim),echec_dim)
        else:
            self.val = vals
        self.nbconflict = self.fitness()
    def __str__(self):
        return ",".join([f"({i},{j})" for i,j in zip(range(echec_dim),self.val)])
    def conflict(p1,p2):
        return p1[0] == p2[0] or p1[1] == p2[1] or abs(p1[0] - p2[0]) == abs(p1[1] - p2[1])
    def fitness(self):
        nbconflict=0
        for i in range(echec_dim):
            for j in range(i+1,echec_dim):
                if Individu.conflict([i,self.val[i]],[j,self.val[j]]):
                    nbconflict+=1
        return nbconflict
    def create_rand_pop(count):
        return [Individu() for i in range(count)]
    def evaluate(pop):
        return list(sorted(pop, key = lambda ele: ele.fitness(),reverse=False))
    def selection(pop, hcount, lcount):
        return pop[hcount:] + pop[-lcount:]
    def croisement(ind1,ind2):
        return [Individu(ind1.val[:4] + ind2.val[:4]), Individu(ind2.val[:4] + ind1.val[4:])]
    def mutation(ind):
        a = random.choice(range(8))
        b = random.choice([i for i in range(8) if i != a])
        ind.val[a], ind.val[b] = ind.val[a], ind.val[b]
        return ind
# %% zone boucle
def algoloopSimple(x):
    pop = Individu.create_rand_pop(25)
    solution_retrouvee = False
    nb_iter = 0
    while not solution_retrouvee:
        print(f"itération numéro : {nb_iter}")
        nb_iter += 1
        evaluation = Individu.evaluate(pop)
        if evaluation[0].fitness() == 0:
            solution_retrouvee = True
        else:
            select = Individu.selection(evaluation,10,4)
            croises = []
            for i in range (0,len(select)-1,2):
                croises += Individu.croisement(select[i],select[i+1])
            mutes = []
            for i in select:
                mutes.append(Individu.mutation(i))
            newalea = Individu.create_rand_pop(x)
            pop = select[:] + croises[:] + mutes[:] + newalea[:]
    print(evaluation[0])
    
# %% zone boucle finale
def SolutionsPossibles(x):
    pop = Individu.create_rand_pop(25)
    solutions = []
    while True:
        solution_retrouvee = False
        nb_iter = 0
        while not solution_retrouvee:
            print(f"itération numéro : {nb_iter}")
            nb_iter += 1
            evaluation = Individu.evaluate(pop)
            if evaluation[0].fitness() == 0:
                solution_retrouvee = True
            else:
                select = Individu.selection(evaluation,10,4)
                croises = []
                for i in range (0,len(select)-1,2):
                    croises += Individu.croisement(select[i],select[i+1])
                mutes = []
                for i in select:
                    mutes.append(Individu.mutation(i))
                newalea = Individu.create_rand_pop(x)
                pop = select[:] + croises[:] + mutes[:] + newalea[:] 
                
        if evaluation[0] not in solutions:
            solutions.append(evaluation.pop(0))
        else:
            evaluation.pop(0)
        pop = evaluation
        print(len(solutions))
        print(*solutions)
# %% zone du main
if __name__ == '__main__' :
    x = input("Nombre d'individu a injecté en plus par génération : ")
    algoloopSimple(int(x))
    #SolutionsPossibles(int(x))
    