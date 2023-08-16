import numpy as np
from scipy import stats

# Створення списку значень
values = [364, 373, 358, 394, 378, 379, 357, 364, 350, 363, 392, 368, 359, 375, 399, 365, 379, 357, 380]

# Перетворення списку на numpy масив
values_array = np.array(values)

# Отримання середнього значення
mean = np.mean(values_array)

# Обчислення медіани
median = np.median(values_array)

# Обчислення моди
mode = stats.mode(values_array).mode
count_mode = stats.mode(values_array).count

# Обчислення стандартного відхилення
std_deviation = np.std(values_array)

print("Вхідні дані:", values)
print("Середнє значення:", mean)
print("Медіана:", median)
print("Мода:", mode)
print("К-сть повторень моди:", count_mode)
print("Стандартне відхилення:", std_deviation)
