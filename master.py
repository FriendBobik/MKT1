from linear import linear_regression, chart_empty, pressure
import pandas as pd

#График для давления

pressure_voltage = pd.read_csv('data/pressure_voltage.csv')

pressure_data = pressure_voltage['pressure'].to_numpy()
voltage = pressure_voltage['voltage'].to_numpy()
print('Зависимость V от P')
slope, intercept = linear_regression(pressure_data, voltage, name1='P (кгс/ cм^2)', name2='V (В)', name3='Зависимость V от P')


pressure(float(slope), float(intercept))


#График для мощности

R_P = pd.read_csv('data/R_P.csv')

R= R_P['R'].to_numpy()
P= R_P['P'].to_numpy()

chart_empty(R, P)

#График для мощности сгорания

t_m = pd.read_csv('data/t_m.csv')

time= t_m['t'].to_numpy()
mass= t_m['m'].to_numpy()
print('Зависимость m от t')
linear_regression(time, mass,name1='t (с)',name2='m (г)',name3='Зависимость m от t')
