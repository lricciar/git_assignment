# Assignment 1

from matplotlib import pyplot as mp
import numpy as np

def sincos(x,y,z):
  if __name__ == '__main__':
    x = np.arange(0,2*np.pi,.1)
    y = np.sin(x)
    z = np.cos(x)
    mp.plot(x,y,x,z)
    mp.show()
  
  
