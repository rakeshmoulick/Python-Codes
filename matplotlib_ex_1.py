# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:13:45 2022

@author: Dr. Rakesh Moulick
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)

plt.figure(1)
plt.plot(x,y,'o-',x,z,'^-')
plt.xlabel('x')
plt.ylabel('y and z')
plt.legend(('sine','cosine'),loc=0)
plt.grid(True)

plt.savefig('test_1.png',format='png',dpi=300)
plt.show()

