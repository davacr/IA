#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:01:50 2021

@author: neo
"""

import numpy as np
import random

class GA: 
    def __init__(self, individuals, n_selection, generations, chrom, crosspoint, minimizar):
        self.individuals = individuals
        self.n_selection = n_selection
        self.generations = generations
        self.chrom = chrom
        self.crosspoint = crosspoint
        self.minimizar = minimizar
        
    def create_population(self):
        return [np.random.randint(0, self.chrom) for _ in range (self.individuals)]
    
    def fitness(self, x):
        return x ** 2
    
    def fit_bin(self, x): 
        return [(x[i], bin(x[i])[2:].zfill(self.chrom), self.fitness(x[i])) for i in x]
    
    def selection(self, pop, pos):
        pop = sorted(pop, key=lambda fit:fit[pos], reverse=self.minimizar)
        return pop[len(pop) -  self.n_selection:]
    
    def reproduction(self, n_population, selected, pos):
        father = []
        new_pop = [] 
        ind_muta = np.random.randint(0, n_population)
        
        for i in range(n_population):
            father = random.sample(selected, 2)
            
            children = list()
            children[:self.crosspoint] = father[0][pos][:self.crosspoint]
            children[self.crosspoint:] = father[1][pos][self.crosspoint:]
            if i == ind_muta:
                bit = np.random.randint(0, self.chrom)
                if children[bit] == '0': 
                    children[bit] = '1' 
                else:
                    children[bit] = '0'
            children = "".join(children)
            
            new_pop.append(children)
        return new_pop
    
    def newgeneration(self, pop, pos):
        return [(int(pop[i], 2), pop[i], self.fitness(int(pop[i], 2))) for i in range(self.individuals)]
    
    def printg(self, pop, i):
        print('=================================')
        print('Generación', i)
        print('=================================')
        print('Población')
        print(pop)  
        
ag = GA (
    individuals = 4,
    n_selection = 2,
    generations = 5,
    chrom = 4,
    crosspoint = 2,
    minimizar = False
)

pop = ag.create_population()
pop = ag.fit_bin(pop)

for i in range(ag.generations):
    sel = ag.selection(pop, 1)
    pop = ag.reproduction(len(pop), sel, 1)
    pop = ag.newgeneration(pop, 0)
    ag.printg(pop, i + 1)  

