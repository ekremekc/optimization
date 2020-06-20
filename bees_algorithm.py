import random as rand
import matplotlib.pyplot as plt
from numpy import arange,Inf
from math import floor
import time
start = time.time()


xmin = -5
xmax =  5
tolerance =  20
difference = (xmax-xmin)/tolerance
r_damp = 0.9


iteration_number = 20

bee_population  = 30
elite_sites      = 5
selected_sites   = 10
sum_ef = elite_sites + selected_sites
non_elite_bees = bee_population - sum_ef

elite_bee     = 30
selected_bee  = 15


best_bee=[]

def f(x1, x2, x3):                  ######## COST FUNCTION
    return x1**2 + x2**2 + x3**2

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
    global x1,x2,x3
    x1 = rand.uniform(xmin, xmax)
    x2 = rand.uniform(xmin, xmax)
    x3 = rand.uniform(xmin, xmax)
    
def bee_neighbour_generate():
    global x1,x2,x3
    x1 = rand.uniform(x1_min, x1_max)
    x2 = rand.uniform(x2_min, x2_max)
    x3 = rand.uniform(x3_min, x3_max)
    
def waggledance(i):
    global x1_min, x1_max 
    global x2_min, x2_max
    global x3_min, x3_max
    
    x1_min = population[i]['x1'] - (difference)
    x1_max = population[i]['x1'] + (difference)
    
    x2_min = population[i]['x2'] - (difference)
    x2_max = population[i]['x2'] + (difference)
    
    x3_min = population[i]['x3'] - (difference)
    x3_max = population[i]['x3'] + (difference)
    
def show_bees():
    for i in range(1, bee_population+1):
        print('Bee ',i, ' : ', population[i]['f(x)'] )
    
    
     
######## RANDOM INITILIZATION  
    
population = {}

for i in range(1,bee_population+1):
    bee_generate()
    population[i] = {'x1':x1, 'x2':x2, 'x3':x3, 'f(x)':f(x1,x2,x3)}
    
population = sorting(population)

for k in range(1,iteration_number+1):
    
    ######## ELITE BEES
    
    for i in range(1,elite_sites+1):              
        
        bestbee = {'x1':Inf, 'x2':Inf, 'x3':Inf, 'f(x)':Inf}
        
        for j in range(1,elite_bee+1):
            waggledance(i)
            bee_neighbour_generate()
            new_elite = {'x1':x1, 'x2':x2, 'x3':x3, 				'f(x)':f(x1,x2,x3)}
            
            if new_elite['f(x)'] < bestbee['f(x)']:    
                bestbee = new_elite
                
        if bestbee['f(x)']<population[i]['f(x)']:          
            population[i] = bestbee
    

     ######## SELECTED BEES 
    
    for i in range(elite_sites+1,sum_ef+1):              
        
        bestbee = {'x1':Inf, 'x2':Inf, 'x3':Inf, 'f(x)':Inf}
        
        for j in range(1,selected_bee+1):
            waggledance(i)
            bee_neighbour_generate()
            new_selected = {'x1':x1, 'x2':x2, 'x3':x3, 				'f(x)':f(x1,x2,x3)}

            if new_selected['f(x)'] < bestbee['f(x)']:
                
                 new_selected = bestbee
        if bestbee['f(x)']<population[i]['f(x)']:          
            population[i] = bestbee
    
    ######## RANDOM BEES (NON-ELITE)
       
    for i in range(sum_ef+1,bee_population+1):          
        
        bee_generate()
        
        population[i] = {'x1':x1, 'x2':x2, 'x3':x3, 'f(x)':f(x1,x2,x3)}

    population = sorting(population)
    
    best_bee.append(population[1]['f(x)'])
    
    difference=difference *r_damp

#########################################################################################

print("\n\tBest Bee  ",2*"\n",
      " x1: ",population[1]['x1'],"\n",
      " x2: ",population[1]["x2"],"\n",
      " x3: ",population[1]['x3'],"\n",
      " Cost Function: ",population[1]['f(x)'],"\n" )

########### GRAPH PLOTTING
x = arange(1,iteration_number+1,1)
y = best_bee

plt.xlabel("Iteration Number")
plt.ylabel("Cost Function")
plt.plot(x,y, label="f(x)=$x_1$$^{2}$+$x_2$$^{2}$+$x_3$$^{2}$ ")
plt.legend()
plt.show()

finish = time.time()

total = finish - start

print("Total execution time: ",floor(total/60), "min",int(total%60), "seconds.\n")
