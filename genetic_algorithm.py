import numpy as np

def cal_pop_fitness(equation_inputs, pop):
    fitness = np.sum(equation_inputs*pop, axis=1)
    return fitness


def select_mating_pool(pop, fitness, num_parents):
    
    parents = np.empty((num_parents, pop.shape[1])) 
    
    for parent_num in range(num_parents):
        
        max_fitness_idx = np.where(fitness == np.max(fitness))
        
        max_fitness_idx = max_fitness_idx[0][0]
        
        parents[parent_num, :] = pop[max_fitness_idx, :]
        
        fitness[max_fitness_idx] = -99999999999
    
    return parents

def crossover(parents, offspring_size):
    
    offspring = np.empty(offspring_size)
    
    crossover_point = np.uint8(offspring_size[1]/2)
    
    for k in range(offspring_size[0]):
        
        parent1_idx = k%parents.shape[0]
        
        parent2_idx = (k+1)%parents.shape[0]

        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
        
    return offspring
    
def mutation(offspring_crossover):
    
    for idx in range(offspring_crossover.shape[0]):
        
        random_value = np.random.uniform(-1, 1, 1)
        
        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
    
    return offspring_crossover





import numpy as np

import matplotlib.pyplot as plt

num_x = 3

xmin = -5
xmax =  5

individual_size = 10

population_size = (individual_size, num_x)

parent_number = 5

offspring_number = individual_size - parent_number

new_population = np.random.uniform(xmin, xmax, population_size)

num_generations = 100

r_damp = 0.9

best_results = []

for generation in range(num_generations):
    
    fitness = np.sum(new_population**2,axis=1)

    ##### SELECTING PARENTS
    
    parents = np.empty((parent_number,new_population.shape[1]))
    
    for i in range(parent_number):
        
        best_id = np.where(fitness == np.min(fitness))
        
        parents[i,:] = new_population[best_id, :]
        
        fitness[best_id] = np.inf

    ##### CROSSOVER
    
    offspring = np.empty((offspring_number, num_x))
    
    crossover_point = np.random.randint(0,num_x)
    
    for k in range(individual_size-parent_number):
        
        p_1 = k%parents.shape[0]
        p_2 = (k+1)%parents.shape[0]
        
        offspring[k,0:crossover_point] = parents[p_1, 0:crossover_point]
        offspring[k,crossover_point:]  = parents[p_2, crossover_point:]
        
    #### MUTATION 
        
    for j in range(individual_size-parent_number):
        
        offspring[j,np.random.randint(0,num_x)] += r_damp*np.random.uniform(-1,1) 
    
    #### POPULATION ADJUSTMENT
    
    new_population[0:parent_number, :] = parents
    new_population[parent_number: , :] = offspring
    
    best_results.append(float(fitness[np.where(fitness==min(fitness))]))

print("Best fitness value: ",best_results[-1])

plt.plot(np.arange(0,num_generations),best_results) 
plt.show()  
















