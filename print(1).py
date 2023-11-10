from linear_regression import linear_regression
import numpy as np

pressure = np.array([1.033, 1.113, 1.193, 1.273, 1.353, 1.433, 1.513])  # p, кгс/см^2
voltage = np.array([11.14, 12.18, 13.22, 14.27, 15.31, 16.01, 16.35])  # V, вольт

print(linear_regression(pressure, voltage))