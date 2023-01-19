####exp_plot
import numpy as np
import matplotlib.pyplot as plt

#Import our own package
#import goph619_examples.function as goph
from goph619_examples.function import exp

#Example script
def main():

    x = np.linspace(-5.,5.,10)
    y = np.zeros(x.shape)
    for k, xk in enumerate(x):
        y[k] = exp(xk)
    
    plt.plot(x,y,'--.')
    plt.show()

if __name__ == '__main__':
    main()
