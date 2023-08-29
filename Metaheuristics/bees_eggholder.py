import random as rand
import matplotlib.pyplot as plt
from numpy import arange,Inf
from math import floor, sin, sqrt
import time
start = time.time()


xmin = -512.0
xmax =  512.0
tolerance =  10
difference = (xmax-xmin)/tolerance
r_damp = 0.95


iteration_number = 100

bee_population  = 100
elite_sites      = 4
selected_sites   = 10
sum_ef = elite_sites + selected_sites
non_elite_bees = bee_population - sum_ef

elite_bee     = 100
selected_bee  = 40


best_bee=[]

"""Eggholder function"""
def egg(x1, x2):
    fx = -(x2 + 47) * sin(sqrt(abs(x2 + x1/2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))
    return fx

def sorting(structure):             ######## DICTIONARY SORT FUNCTION
    structure = dict(sorted(structure.items(), key = lambda x : x[1]['f(x)']))
    sorted_structure = {}
    bee_key=1
    for key1 in structure.keys():
        sorted_structure[bee_key]=structure[key1]
        bee_key=bee_key+1
    structure = sorted_structure
    return structure

def bee_generate():
    global x1,x2
    x1 = rand.uniform(xmin, xmax)
    x2 = rand.uniform(xmin, xmax)

    
def bee_neighbour_generate():
    global x1,x2
    x1 = rand.uniform(x1_min, x1_max)
    x2 = rand.uniform(x2_min, x2_max)
    
def waggledance(i):
    global x1_min, x1_max 
    global x2_min, x2_max
    
    x1_min = population[i]['x1'] - (difference)
    x1_max = population[i]['x1'] + (difference)
    
    x2_min = population[i]['x2'] - (difference)
    x2_max = population[i]['x2'] + (difference)
    
    if x1_min<xmin :
    	x1_min = xmin
    elif x2_min<xmin:
    	x2_min = xmin
    elif x1_max>xmax:
    	x1_max = xmax
    elif x2_max>xmax:
    	x2_max = xmax
    	
def show_bees():
    for i in range(1, bee_population+1):
        print('Bee ',i, ' : ', population[i]['f(x)'] )
     
######## RANDOM INITILIZATION  
    
population = {}

for i in range(1,bee_population+1):
    bee_generate()
    population[i] = {'x1':x1, 'x2':x2,  'f(x)':egg(x1,x2)}
    
population = sorting(population)

for k in range(1,iteration_number+1):
    
    ######## ELITE BEES
    
    for i in range(1,elite_sites+1):              
        
        bestbee = {'x1':Inf, 'x2':Inf, 'f(x)':Inf}
        
        for j in range(1,elite_bee+1):
            waggledance(i)
            bee_neighbour_generate()
            new_elite = {'x1':x1, 'x2':x2, 'f(x)':egg(x1,x2)}
            
            if new_elite['f(x)'] < bestbee['f(x)']:    
                bestbee = new_elite
                
        if bestbee['f(x)']<population[i]['f(x)']:          
            population[i] = bestbee
    

     ######## SELECTED BEES 
    
    for i in range(elite_sites+1,sum_ef+1):              
        
        bestbee = {'x1':Inf, 'x2':Inf, 'f(x)':Inf}
        
        for j in range(1,selected_bee+1):
            waggledance(i)
            bee_neighbour_generate()
            new_selected = {'x1':x1, 'x2':x2, 'f(x)':egg(x1,x2)}

            if new_selected['f(x)'] < bestbee['f(x)']:     
                 new_selected = bestbee
                 
        if bestbee['f(x)']<population[i]['f(x)']:          
            population[i] = bestbee
    
    ######## RANDOM BEES (NON-ELITE)
       
    for i in range(sum_ef+1,bee_population+1):          
        
        bee_generate()
        
        population[i] = {'x1':x1, 'x2':x2, 'f(x)':egg(x1,x2)}

    population = sorting(population)
    
    best_bee.append(population[1]['f(x)'])
    
    difference = difference *r_damp

#########################################################################################

print("\n\tBest Bee  ",2*"\n",
      " x1: ",population[1]['x1'],"\n",
      " x2: ",population[1]["x2"],"\n",
      " Cost Function: ",population[1]['f(x)'],"\n" )

########### GRAPH PLOTTING
x = arange(1,iteration_number+1,1)
y = best_bee

plt.xlabel("Iteration Number")
plt.ylabel("Cost Function")
plt.plot(x,y, label="f(x)")
plt.legend()
plt.show()

finish = time.time()

total = finish - start

print("Total execution time: ",floor(total/60), "min",int(total%60), "seconds.\n")

