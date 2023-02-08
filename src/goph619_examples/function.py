"""Module for implementing functions with series solution in Python

Contains functions: exp()
"""
import numpy as np
#######################
#Exp functinon
def exp(x, dtype = float):
    """Exponential function

    Parameters
    ----------
    x : array_like
        Arguments to exp functions
    
    Returns
    -------
    numpy.ndarray
        Result of exp function
    """
    x = np.array(x) #Convert x to numpy array to check array_like
    #Initalization
    k = 0
    fact_k = 1
    x_k = np.ones_like(x)
    s = np.ones_like(x)
    err = np.ones_like(x)
    tol = 1.e-16
    #Iteration
    while err.max() > tol:
        k +=1         # increment iteration counter
        fact_k *= k     #Update factorial 
        x_k *= x        # update X^k
        t = x_k / fact_k
        s = s+ t
        err = abs(t/s)

    return np.array(s, dtype=float)
#################################
#Cos function by Ben
# def cos(x):
#     """Compute the value of cosine
#     Parameters
#     ---------
#     Returns
#     ------
#     """
#     k = 1
#     err = 1.
#     tol = 1e-16
#     s = 0.
#     fact_k = 1
#     t = 0.
#     while err>tol:
#     #for i in range(0,4):
#         if (k%2 ==0):      #Calculate factorial
#             fact_k *= k 
#             #print(fact_k,k)
#             t = (-1) **k * (x **(2*k)) / (fact_k)
#             s += t
#             err = abs(t/s)  #Update error 
#             #print("S:", s,"t:", t, "fact of ", k, "is:", fact_k)
#             k+=1
#         else:
#             fact_k *= k 
#             k +=1          
#     return s
#######################
#Cos by Brandon
def cos(x):
    """Compute the cosine of a value

    Parameters
    ----------
    x : array_like
        The arguments to cos function

    Returns
    -------
    numpy.ndarray
        Result of cos function
    """
    x = np.array(x) # Try to convert x to numpy array and check array_like
    #Initialize
    k = 0
    fact_2k = 1
    sign = 1
    x_2 = x**2
    x_2k = np.ones_like(x)
    s = np.ones_like(x)
    err = np.ones_like(x)
    tol = 1.e-16
    #Iteration
    while err.max() > tol:
        k += 1
        two_k = 2*k
        fact_2k *= two_k * (two_k - 1)
        sign *= -1
        x_2k *= x_2
        t = sign * x_2k / fact_2k
        s = s +  t
        err = abs(t/s)
    return s

########################################
#Sin function By Ben
# def sin(x):
#     """Compute the value of cosine
#     Parameters
#     ---------
#     Returns
#     ------
#     """
#     k = 0
#     err = 1.
#     tol = 1e-16
#     s = 1.
#     fact_k = 1
#     t = 0.
#     #while err>tol:
#     for i in range(0,10):
#         k = 2*k+1
#         #print("k:",k,"i",i)
        
#     return s
####################
#Sin function by Brandon
def sin(x):
    """Compute value of Sin

    Parameters
    ---------
    x : array_like
        Arguments to the sin function
    
    Returns
    -------
    numpy.ndarray
        Result of sin function
    """
    x = np.array(x) # try to convert x to numpy array and check array like
    #Initialization
    k = 0
    fact_2kp1 =1
    sign = 1
    s = x
    err = np.ones_like(x)
    tol = 1.e-16
    #Iteration block
    while err.max() > tol:
        k += 1
        two_k = 2*k
        fact_2kp1 *= two_k * (two_k + 1)
        sign *= -1
        x_2kp1 = x ** (two_k + 1)
        t = sign * x_2kp1 /fact_2kp1
        s = s+ t
        err = abs(t/s[k])
    return s
####
#For Lab 1
##########################################
####Convert Decimal to mantissa and exponent
def decimal_2_mne(num):
    """
    """
    ########Convert decimal to base 2
    #Find if num is greater or less than 1
    n = 0
    while True:
        if num >1:
            num /= 2
            e = n+1
            n += 1
            #print(remainder,'if')
        else:
            num *= 2
            e = n-1
            n +=1
            #print(remainder,'else')
        if num>=0.5 and num <1:
            break
    #print("Mantissa #:", num, "Exponent #:", e)
    return num, e

#################################
####Convert mantissa and exponent to binary
def me_2_bin(m,e):
    import numpy as np
    """
    """
    ####### Converts mantissa to binary
    rem = m
    sb = np.zeros(53)
    i = 0
    for k in range(-1,-53,-1):
        if rem >= 2**k:
            #print("remainder:", rem, "2^k:", 2**k, "k:",k)
            sb[i] = 1
            rem -= 2**k
            i +=1
        else:
            sb[i]= 0   
            i +=1
    ########
    #Convert exponent to binary
    rem = e
    se = np.zeros(10)
    i = 0
    for k in range(9,0,-1):
        if rem >= 2**k:
            se[i] = 1
            rem -= 2**k
            i +=1
        else:
            se[i] = 0
            i +=1
    #print("Exponent:", se, "Mantissa:", sb)
    return sb,se
    
############################################
# if __name__ == '__main__':
#     print(f'exp(0): {exp(0)}') #A form of Verification, know e(0) by the series function
#     print(f'exp(1): {exp(1)}') #A form of Validation, need to look to find e(1)
    # m,e = decimal_2_mne(173)
    # print("Mantissa:",m,"Exponent:",e)
    # sb, se = me_2_bin(m,e)
    # print("Exponent:", se, "Mantissa:", sb)