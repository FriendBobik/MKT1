#функция для линейной зависимости
def linear_regression(np_x, np_y):
    import numpy as np
    from scipy.stats import linregress
    import matplotlib.pyplot as plt

    pressure = np_x
    voltage = np_y

    slope, intercept, r_value, p_value, std_err = linregress(pressure, voltage)

    print(f"Коэффициент наклона (slope): {slope}")
    print(f"Ошибка аппроксимации (std_err): {std_err}")

    #print(f"Коэффициент корреляции (r_value): {r_value}")
    #print(f"Коэффициент корреляции (p_value): {p_value}")

    relative_error_percent = (std_err / slope) * 100
    print(f"Относительная ошибка (в процентах): {relative_error_percent:.2f}%")

    plt.figure(figsize=(10, 5))


    plt.scatter(pressure, voltage, color='red', label='Измеренные данные') 
    plt.plot(pressure, intercept + slope * pressure, label='Линейная аппроксимация', color='blue') 

    approximation_formula = f"V = {intercept:.2f} + {slope:.2f}p"
    plt.text(1.25, 16.5, approximation_formula, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

    plt.xlabel('Давление (кгс/см^2)')
    plt.ylabel('Напряжение (В)')
    plt.title('Зависимость напряжения от давления')
    plt.legend()
    plt.grid(True)
    plt.show()
