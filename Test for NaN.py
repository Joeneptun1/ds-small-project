# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-GJxKQKzdxk1pdiGtZ9SgZTzoUmkdnQB
"""

import numpy as np

a = np.array([4, 8, np.nan, np.inf])
print("Original array: ", a)

print("Test element-wise for NaN:")
print(np.isnan(a))