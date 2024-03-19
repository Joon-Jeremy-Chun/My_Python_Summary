# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:09:23 2024

@author: joonc
"""

import numpy as np

# Create a 3x3 matrix
matrix = np.array([[1, 1, 2],
                   [2, 3, 4],
                   [6, 6, 2]])

# Compute the inverse of the matrix
inverse_matrix = np.linalg.inv(matrix)

# Print the original matrix and its inverse
print("Original matrix:")
print(matrix)
print("\nInverse matrix:")
print(inverse_matrix)