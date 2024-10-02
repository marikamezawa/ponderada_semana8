import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matriz = np.array(list).reshape(3, 3)
    
  
    funcs = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    
    
    calculations = {key: [func(matriz, axis=0).tolist(), func(matriz, axis=1).tolist(), func(matriz).tolist()]
                    for key, func in funcs.items()}
    
    return calculations


