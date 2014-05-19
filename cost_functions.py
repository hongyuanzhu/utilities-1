import numpy as np
from numpy.linalg import norm
from numpy import sqrt

def squared_loss(x,y):
    assert len(x)==len(y)
    return 0.5*norm(y-x)**2

def RMSE(x,y):
    N = len(x)
    assert N==len(y)
    return sqrt(norm(y-x)**2/float(N))

def MSE(x,y):
    N = len(x)
    assert N==len(y)
    return norm(y-x)**2/float(N)


def get_cost_function(func_name):
    functions = { 
                    'squared_loss': squared_loss,
                    'RMSE'        : RMSE,
                    'MSE'         : MSE,
    }
    return functions[func_name]


