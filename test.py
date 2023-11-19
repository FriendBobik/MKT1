import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



file_path = 'data/New_File3.csv'  # обновленный файл
df = pd.read_csv(file_path)




# Преобразование данных в столбце "CH1" в числа
df['CH1'] = pd.to_numeric(df['CH1'].str[1:170], errors='coerce')  # Преобразование с обработкой ошибок

# Построение графика CH1 от V_t с корректировкой значений CH1
plt.figure(figsize=(10, 6))
plt.plot(df['V_t'], (df['CH1']-0.04)/1.13, label='CH1 vs V_t', linewidth=0, marker='o', markersize=2, color='blue')
plt.xlabel('V_t')
plt.ylabel('CH1')
plt.title('График зависимости CH1 от V_t')
plt.legend()
plt.grid(True)
plt.show()
