import pandas as pd
from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np

df = pd.read_csv('Cliamte Group/BSh.csv')

def ET(X):
    return ((((0.408 * ((2503.06*np.exp(17.27*(((X[:,0]+X[:,1])/2))/(((X[:,0]+X[:,1])/2)+237.3)))/(((X[:,0]+X[:,1])/2)+237.3)**2) * (X[:,2]-X[:,3]))) + ((X[:,4]) * (900/(((X[:,0]+X[:,1])/2) + 273))) * (X[:,5]*(X[:,6]-((X[:,7]/100)*((0.6108*np.exp((17.27*X[:,0])/(X[:,0]+237.3))) + (0.6108*np.exp((17.27*X[:,1])/(X[:,1]+237.3))))/2)))) / ((((2503.06*np.exp(17.27*(((X[:,0]+X[:,1])/2))/(((X[:,0]+X[:,1])/2)+237.3)))/(((X[:,0]+X[:,1])/2)+237.3)**2)) + X[:,4] * (1 + 0.34 * X[:,5])))

problem = {'num_vars': 8,
           'names': ['Tmax', 'Tmin', 'Rn', 'G', 'gama', 'u2', 'es', 'Rhmean'],
           'bounds': [[8.12, 48.48],
                     [-2.72, 34.54],
                     [-5.66, 19.43],
                     [-1.95, 1.12],
                     [0.06, 0.07],
                     [0.5, 3.87],
                     [0.79, 8.43],
                     [8.5, 85.4]]
           } 



# Generate samples
param_values = saltelli.sample(problem, 10000000, calc_second_order=False)
print(param_values)

# Run model (example)
Y = ET(param_values)

# Perform analysis
Si = sobol.analyze(problem, Y, calc_second_order=False)
# , print_to_console=True
print(Si)