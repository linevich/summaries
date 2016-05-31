#!/env/bin/python3
# -*- coding: utf-8 -*-

import math

TABLE_BEING = r"""\begin{table}[ht!]
  \caption{Результати спостереження}
\label{t:results_indirect}
\begin{tabular}{| c | c | c | c | c | c |}
  \hline
  \multicolumn{1}{|C{1cm}|}{№} &
  \multicolumn{1}{c|}{$\varphi_i$,~\%} &
  \multicolumn{1}{C{3.0cm}|}{{$\Delta\varphi_i = \varphi_i - \bar{\varphi}$}} &
  \multicolumn{1}{C{2.5cm}|}{$\Delta{\varphi_i}^2$} &
  \multicolumn{1}{C{2.5cm}|}{Примітка} \\ \hline"""
TABLE_END = r"""\end{tabular}
\end{table}
"""

# Вихідні дані
RESULTS = [ 48.0, 48.0, 47.9, 47.9, 48.0, 48.1, 48.1, 48.0, 48.0, 48.0,
            47.9, 47.9, 47.9, 48.0, 48.0, 48.0, 48.0, 48.1, 48.1, 48.1,
            48.0, 48.0, 47.8, 47.9, 48.0, 48.0, 48.1, 48.2, 48.0, 48.0,]

# Рахуємо середнє арифметичне 
ARITHMETIC_MEAN_OF_FI = sum(RESULTS)/len(RESULTS)

def delta_fi_i():
    result = []
    
    for delta_fi in RESULTS:
        result.append(delta_fi - ARITHMETIC_MEAN_OF_FI)

    return result

def delta_fi_square():
    result = []
    
    for delta_fi in RESULTS:
        result.append(math.sqrt(delta_fi))

    return result

DELTA_FI_I = delta_fi_i()
DELTA_FI_SQUARE = delta_fi_square()

def format_data():
    result = []
    for i in range(len(RESULTS)):
        result.append([RESULTS[i], DELTA_FI_SQUARE[i], DELTA_FI_I[i]])

    return result

DELTA = math.sqrt(sum(RESULTS)/(len(RESULTS) - 1))

def print_table():

    print(TABLE_BEING)
    #Виводимо таблицю результатів
    for col in format_data():
        print(r'\rownumber & %s & %.2f & %.2f & \\ \hline' % (col[0], col[1], col[2]))

    # Виводимо нижній рядок таблиці
    bottom_row = r' & $\bar{\varphi} = \frac{1}{%s} \cdot \displaystyle\sum_{i=1}^{%s} \Delta{\varphi_i}=%s$ & %s & $\delta = %.2f$ & \\ \hline'
    print(bottom_row % (len(RESULTS), len(RESULTS), ARITHMETIC_MEAN_OF_FI, sum(DELTA_FI_I), DELTA))
    print(TABLE_END)

print_table()
