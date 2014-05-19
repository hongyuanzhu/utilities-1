from __future__ import division
import numpy as np
from numpy import exp
from numpy import trace
from numpy.linalg import det
from numpy.linalg import pinv
from numpy.linalg import cholesky

class Inverse_Wishart(self, W, v):
    self.W = W
    self.v = v
    self.n, self.p = W.shape
    
    assert v > self.p-1, 'v <= p-1'
    assert not False in (W>0), 'W is not > 0'

    def sample(self):
        chol = cholesky(self.W)


    def pdf(self, X):
            n, p = X.shape
            assert n==p
            assert self.P == p
            Z = 2**(-self.n*self.p/2.0)*det(self.W)**(-self.n/2.0)
            return Z*det(X)**((self.n-self.p-1)/2.0)*exp(-0.5*trace(pinv(W).dot(X)))


