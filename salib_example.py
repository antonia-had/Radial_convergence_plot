from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
from graph import drawgraphs

# Define the model inputs
problem = {
    'num_vars': 3,
    'names': ['x1', 'x2', 'x3'],
    'bounds': [[-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359]]
}

# Generate samples
param_values = saltelli.sample(problem, 1000)

# Run model (example)
Y = Ishigami.evaluate(param_values)

# Perform analysis
Si = sobol.analyze(problem, Y, print_to_console=True)

'''
Function to convert S2 output for graph generation. Taken from 
https://github.com/Project-Platypus/Rhodium/blob/master/rhodium/sa.py
'''
def S2_to_dict(matrix, problem):
    result = {}
    names = list(problem["names"])
    
    for i in range(problem["num_vars"]):
        for j in range(i+1, problem["num_vars"]):
            if names[i] not in result:
                result[names[i]] = {}
            if names[j] not in result:
                result[names[j]] = {}
                
            result[names[i]][names[j]] = result[names[j]][names[i]] = float(matrix[i][j])
            
    return result

result = {} #create dictionary to store new
result['S1']={k : float(v) for k, v in zip(problem["names"], Si["S1"])}
result['S1_conf']={k : float(v) for k, v in zip(problem["names"], Si["S1_conf"])}
result['S2'] = S2_to_dict(Si['S2'], problem)
result['S2_conf'] = S2_to_dict(Si['S2_conf'], problem)
result['ST']={k : float(v) for k, v in zip(problem["names"], Si["ST"])}
result['ST_conf']={k : float(v) for k, v in zip(problem["names"], Si["ST_conf"])}

drawgraphs(result)
