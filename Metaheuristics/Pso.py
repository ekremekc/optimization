from numpy import arange,Inf,array
from numpy.random import uniform,random as rand
import matplotlib.pyplot as plt





#########   PROBLEM DEFINITION    #####################

def f(x1, x2, x3, x4, x5):                          #SPHERE FUNCTION
    return x1**2 + x2**2 + x3**2 + x4**2 + x5**2

xmin = -10
xmax =  10


#########   PARAMETERS OF PSO    #####################
    
Iteration_Number = 100

nPop = 50              #Population Size (Swarm Size)

w = 1                   #Inertia Coefficent
w_damp = 0.99           #Damping Intertia Coefficient           
c1 = 2                  #Personal Acceleration Coefficent
c2 = 2                  #Global(Social) Acceleration Coefficent


#########   INITIALIZATION    #####################

  

particle = {}           #Population Array
pos = [Inf, Inf, Inf, Inf, Inf]
global_best = {'Position':pos,'Cost':Inf}

for i in range(1, nPop+1):
    
    x1 = uniform(xmin, xmax)
    x2 = uniform(xmin, xmax)
    x3 = uniform(xmin, xmax)
    x4 = uniform(xmin, xmax)
    x5 = uniform(xmin, xmax)
    
    particle[i] = {'Position':[x1, x2, x3, x4, x5],
                   'Velocity':[0, 0, 0, 0, 0],
                   'Cost':f(x1,x2,x3,x4,x5),
                   'Best':{ 'Position':[x1, x2, x3, x4, x5],'Cost':f(x1,x2,x3,x4,x5)} }
    
    #Update Global Best
    if particle[i]['Cost'] < global_best['Cost']:
        global_best = particle[i]['Best']

BestCosts = []

#########   MAIN LOOP OF PSO    #####################
    
for k in range(1, Iteration_Number+1):
    
    for i in range(1, nPop+1):
        #Update Velocity
        particle[i]['Velocity'] =  w  * particle[i]['Velocity']\
                                 + c1 * uniform(0, 1, 5)*(array(particle[i]['Best']['Position']-array(particle[i]['Position'])))\
                                 + c2 * uniform(0, 1, 5)*(array(global_best['Position']-array(particle[i]['Position'])))
        #Update Position 
        particle[i]['Position'] =  particle[i]['Position'] + particle[i]['Velocity']   
        #Apply Lower and Upper Bound Limits
        
        
        x1 = particle[i]['Position'][0]
        x2 = particle[i]['Position'][1]
        x3 = particle[i]['Position'][2]
        x4 = particle[i]['Position'][3]
        x5 = particle[i]['Position'][4]
        particle[i]['Cost'] = f(x1,x2,x3,x4,x5)
        
        if particle[i]['Cost'] < particle[i]['Best']['Cost']:
            particle[i]['Best']['Position'] = particle[i]['Position']
            particle[i]['Best']['Cost'] = particle[i]['Cost']
            #Update Global Best
            if particle[i]['Cost'] < global_best['Cost']:
                global_best = particle[i]['Best']
    w *= w_damp        
    BestCosts.append(global_best['Cost'])
    # print("Iteration: ",k,"\t Best Swarm: ",global_best['Cost'])


#########   RESULTS    #####################

iteration = arange(1,Iteration_Number+1)
plt.plot(iteration, BestCosts, label = r'$\sum_{i=1}^{5} x_i^{2}$')
plt.xlabel("Iteration Number")
plt.ylabel("Best Particle")
plt.title("Particle Swarm Optimization Implementation")
plt.legend()
plt.show()

print("Best Particle Parameteres:\n",
      "x1: ",global_best['Position'][0],"\n",
      "x2: ",global_best['Position'][1],"\n",
      "x3: ",global_best['Position'][2],"\n",
      "x4: ",global_best['Position'][3],"\n",
      "x5: ",global_best['Position'][4],"\n",
      "Fitness Evaluation: ",global_best['Cost']
      )
