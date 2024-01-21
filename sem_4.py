# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами). Можете использовать любую парадигму, 
# но рекомендую использовать функциональную, т.к. в этом примере она значительно упростит вам жизнь.

import math

# Функция для расчета среднего значения массива
def mean(arr):
    return sum(arr) / len(arr)

# Функция для расчета стандартного отклонения массива
def std_dev(arr):
    arr_mean = mean(arr)
    squared_diffs = [(x - arr_mean) ** 2 for x in arr]
    return math.sqrt(sum(squared_diffs) / len(arr))

# Функция для расчета корреляции Пирсона
def pearson_correlation(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
    x_std_dev = std_dev(x)
    y_std_dev = std_dev(y)
    n = len(x)

    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = x_std_dev * y_std_dev

    return numerator / (n * denominator)

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

correlation = pearson_correlation(x, y)
print(f"Корреляция Пирсона: {correlation}")