# Functions.py
def exp(x):
    """
    """
    k = 0
    err = 1.
    tol = 1e-16   #About 16 digits of precision
    s = 1.
    fact_k = 1
    while err > tol:
        k += 1
        fact_k *= k
        t = (x ** k) / fact_k #Calculate term 
        s += t   #Sum increment        
        err = abs(t/s)  #Update error
    return s

if __name__ == '__main__':
    print(f'exp(0): {exp(0)}')
    print(f'exp(1): {exp(1)}')