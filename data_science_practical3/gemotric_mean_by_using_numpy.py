import numpy as np
def g_mean(x):
    a = np.log(x)
    print("gemotric mean =",np.exp(a.mean()))
    
g_mean([1,4,5,6,7,8])