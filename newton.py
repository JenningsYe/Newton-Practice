def optimize(x0, fun):
    err=1
    x=x0
    h=0.1
    eps =1e-2;
    while abs(change) > 1e-6:
        xold=x
        x=x-eps*deriv(x, fun, h)/deriv2(x, fun, h)
        change = fun(x)-fun(xold)
    return [x, fun(x)]
    
def deriv(x, fun, h):
    return (fun(x+h)-fun(x-h))/2/h
    
def deriv2(x, fun, h):
    return (fun(x+h)-2*fun(x)+fun(x-h))/h**2