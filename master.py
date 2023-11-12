from linear import linear_regression, chart_empty
import pandas as pd

#График для давления

pressure_voltage = pd.read_csv('data/pressure_voltage.csv')

pressure = pressure_voltage['pressure'].to_numpy()
voltage = pressure_voltage['voltage'].to_numpy()

linear_regression(pressure, voltage)

#График для мощности

R_P = pd.read_csv('data/R_P.csv')

R= R_P['R'].to_numpy()
P= R_P['P'].to_numpy()

chart_empty(R, P)