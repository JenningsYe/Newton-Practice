import numpy as np
import numdifftools as nd

def optimize(x0, fun):
    change = 1
    x = x0
    eps = 1e-2
    while abs(change) > 1e-6:
        grad = nd.Gradient(fun)
        hess = nd.Hessian(fun)
        x_old = x;
        x = x - eps*np.linalg.solve(hess(x), grad(x))
        change = pow(np.sum(x-x_old)**2,0.5)
    return [x, fun(x)]