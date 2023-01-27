####Test sin and cos
import numpy as np
import matplotlib.pyplot as plt

from goph619_examples.function import (cos, sin)

def main():
    x = np.linspace(-10,10,30)

    yc = cos(x)
    yc_num = np.cos(x)
    ys = sin(x)
    ys_num = np.sin(x)

    #Plot sin and cos
    #Plot cos
    plt.subplot(2,1,1)
    plt.plot(x,yc,'.',markersize = 12,label = "Series solution")
    plt.plot(x,yc_num,'r-.', label = "Numpy")
    plt.ylabel(f"Cos(x)")
    plt.legend()
    #Plot sin
    plt.subplot(2,1,2)
    plt.plot(x,ys,'.',markersize = 12,label = "Series solution")
    plt.plot(x,ys_num,'r-.', label = "Numpy")
    plt.legend()
    plt.xlabel("Length")
    plt.ylabel(f"Sin(x)")
    plt.suptitle("Cos and Sin test")
    plt.show()

if __name__ == '__main__':
    main()

