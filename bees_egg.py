from numpy import * 
import numpy
import random

"""Algorithm Parameters"""
itr_num = 100
pop_num = 100
el_sit  = 4
sel_sit = 10
el_bee  = 100
sel_bee = 40
ngh     = 20

"""Eggholder function"""
def egg(x1, x2):
    fx = -(x2 + 47) * sin(sqrt(abs(x2 + x1/2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))
    return fx

"""Neighborhood function"""
def ngh_func(x1, ngh):
    new_x1 = x1 + random.uniform(-ngh, ngh)
    if new_x1 < -512:
        new_x1 = -512
    elif new_x1 > 512:
        new_x1 = 512        
    return new_x1

"""First Population"""
matr = []
for nmb in range(0, pop_num):
    a = random.uniform(-512, 512)
    b = random.uniform(-512, 512)
    tot = egg(a, b)
    matr.append([a, b, tot])

pop_matr = reshape(matr,(pop_num, 3)) #Array to matrix

"""Sort population"""
population = pop_matr[numpy.argsort(pop_matr[:, 2])]
# print("First Population")
# print(population)

print("\nBest solution in every iteration.")

"""Algorithm"""
for it in range(0, itr_num):
    
    """Elite Site Search"""
    for enmb in range(0, el_sit):
        dumy_tot = Inf
        nmb1 = population[enmb][0]
        nmb2 = population[enmb][1]
        for ebnmb in range(0, el_bee):
            new_x1 = ngh_func(nmb1, ngh)
            new_x2 = ngh_func(nmb2, ngh)
            new_tot = egg(new_x1, new_x2)
            new_bee = [new_x1, new_x2, new_tot]
            if new_bee[2] < dumy_tot:
                dumy_tot = new_bee[2]
                bestnew_bee = new_bee
        if bestnew_bee[2] < population[enmb][2]:
            population[enmb] = bestnew_bee

    """Selected Site Search"""
    for snmb in range(el_sit, sel_sit):
        dumy_tot = Inf
        nmb1 = population[snmb][0]
        nmb2 = population[snmb][1]
        for sbnmb in range(0, sel_bee):
            new_x1 = ngh_func(nmb1, ngh)
            new_x2 = ngh_func(nmb2, ngh)
            new_tot = egg(new_x1, new_x2)
            new_bee = [new_x1, new_x2, new_tot]
            if new_bee[2] < dumy_tot:
                dumy_tot = new_bee[2]
                bestnew_bee = new_bee
        if bestnew_bee[2] < population[snmb][2]:
            population[snmb] = bestnew_bee

    """Global Search"""
    for gnmb in range(sel_sit, pop_num):
        a = population[gnmb][0] = random.uniform(-512, 512)
        b = population[gnmb][1] = random.uniform(-512, 512)
        population[gnmb][2] = egg(a, b)

    """Sort population"""
    population = population[numpy.argsort(population[:, 2])]
    
    """ngh Update"""
    ngh = ngh * 0.95
    
    """Best solution"""
    print(population[0])

# print("\nLast population")
# print(population)
print("\nBest solution.")
print(population[0])
# print("\nLast ngh size")
# print(ngh)