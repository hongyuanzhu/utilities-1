import random
import numpy as np

class KModes:

    def __init__(self, K):
        '''
            k-modes clustering algorithm for categorical data


        ''' 
        assert K > 1, 'Choose more than 1 cluster'
        self.K = K
