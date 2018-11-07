# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:22:30 2018

@author: shl12
"""

import numpy as np

z = np.array([[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]])

print(z.shape)

z=z.reshape(-1,1)
print(z.shape)