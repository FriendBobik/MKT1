#функция для линейной зависимости
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
def linear_regression(data1, data2,name1,name2,name3):

    slope, intercept, r_value, p_value, std_err = linregress(data1, data2)

    print(f"Коэффициент наклона (slope): {slope}")
    print(f"Ошибка аппроксимации (std_err): {std_err}")

    #print(f"Коэффициент корреляции (r_value): {r_value}")
    #print(f"Коэффициент корреляции (p_value): {p_value}")

    relative_error_percent = (std_err / slope) * 100
    print(f"Относительная ошибка (в процентах): {relative_error_percent:.2f}%")

    plt.figure(figsize=(10, 5))


    plt.scatter(data1, data2, color='red', label='Измеренные данные') 
    plt.plot(data1, intercept + slope * data1, label='Линейная аппроксимация', color='blue') 

    approximation_formula = f"V = {intercept:.2f} + {slope:.2f}p"
    plt.text(1.25, 1.65, approximation_formula, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
    plt.xlabel(name1)
    plt.ylabel(name2)
    plt.title(name3)
    plt.legend()
    plt.grid(True)
    plt.show()
    return slope,intercept
#Для зависимости P от R
def chart_empty(R, P):

    plt.figure(figsize=(10, 5))
    plt.plot(R, P, marker='.', linestyle=' ', color='red', label='Измеренные данные')
    plt.xlabel('R + R_нагрузки (Ом)')
    plt.ylabel('P (вт)')
    plt.title('Зависимость P от R + R_нагрузки')
    plt.grid(True)
    plt.show()


def pressure(slope,intercept):

    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from matplotlib.ticker import FuncFormatter

    # Reading the CSV file
    file_path = 'data/NewFile3.csv'
    data = pd.read_csv(file_path)

    # Skip the first row and convert columns to numeric
    data = data.iloc[1:]
    data['X'] = pd.to_numeric(data['X'])*0.0005
    data['CH1'] = (pd.to_numeric(data['CH1'])-intercept)/slope


    # Plotting the graph
    plt.figure(figsize=(10, 6))
    plt.plot(data['X'], data['CH1'], label='CH1', linewidth=1, marker='o', markersize=2,color='blue')
    #plt.plot(data['X'], data['CH2'], label='CH2', linewidth=1, marker='o', markersize=2)

    plt.xlabel('t, с')
    plt.ylabel('Pressure, кгс/см^2')
    plt.title('Давление от времени')
    plt.legend()
    plt.grid(True)

    def custom_formatterx(x,pos):
        return f'{x:.2f}'
    def custom_formattery(x,pos):
        return f'{x:.2f}'

    # Setting the custom formatter for both axes
    plt.gca().xaxis.set_major_formatter(FuncFormatter(custom_formatterx))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(custom_formattery))



    # Setting the frequency of axis labels
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(0.05))  # Adjust this value as needed for X-axis
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.0625)) # Adjust this value as needed for Y-axis

    plt.show()