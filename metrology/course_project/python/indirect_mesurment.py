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
RESULTS = [48.0, 48.0, 47.9, 47.9, 48.0, 48.1, 48.1, 48.0, 48.0, 48.0,
           47.9, 47.9, 47.9, 48.0, 48.0, 48.0, 48.0, 48.1, 48.1, 48.1,
           48.0, 48.0, 47.9, 47.9, 48.0, 48.0, 48.1, 48.1, 48.0, 48.0, ]

# Одиниці вимірювання
MEASUREMENT_UNIT = r'\%'

# Рахуємо середнє арифметичне 
ARITHMETIC_MEAN_OF_FI = sum(RESULTS) / len(RESULTS)


def delta_fi_i():
    result = []

    for delta_fi in RESULTS:
        result.append(delta_fi - ARITHMETIC_MEAN_OF_FI)

    return result


def delta_fi_square():
    result = []

    for delta_fi in delta_fi_i():
        result.append(pow(delta_fi, 2))

    return result


DELTA_FI_I = delta_fi_i()
DELTA_FI_SQUARE = delta_fi_square()


def format_data():
    result = []
    for i in range(len(RESULTS)):
        result.append([RESULTS[i], DELTA_FI_I[i], DELTA_FI_SQUARE[i]])

    return result


DELTA = math.sqrt(sum(delta_fi_square()) / (len(RESULTS) - 1))
DELTA_CA = DELTA / math.sqrt(len(RESULTS))

EQUATION_BREAK = '\\\ \n \\MoveEqLeft'
BEGIN_EQUATION = r'\begin{equation}\begin{split}' + '\n\\MoveEqLeft'
END_EQUATION = r'\end{split}\end{equation}' + '\n'

BEGIN_DMATH = r'\begin{dmath*}'
END_DMATH = r'\end{dmath*}'


def print_delta():
    """
    Виведення покоркових обрахунків середнього квадратичного в LaTex.
    """
    n = len(RESULTS)

    # Частина формули з сумою
    suma = r'\displaystyle\sum_{i=1}^{%s} ({\varphi_i} - %.2f)^2' % (n, ARITHMETIC_MEAN_OF_FI)

    # Підставлення значень в загальну формулу
    initial_formula = r'\delta = \sqrt{\frac{1}{%s-1} \cdot %s }' % (n, suma)

    first_step = []
    second_step = []

    for i in RESULTS:
        second_step_value = float(i) - float(ARITHMETIC_MEAN_OF_FI)

        if second_step_value != 0:
            first_step.append('(%s - %s)^2' % (i, ARITHMETIC_MEAN_OF_FI))
            if second_step_value < 0:
                second_step.append('(%.2f^2)' % (second_step_value))
            else:
                second_step.append('%.2f^2' % (second_step_value))
        else:
            first_step.append('\cancel{(%s - %s)}^2' % (i, ARITHMETIC_MEAN_OF_FI))

    # Параметри переносів
    indent = 2
    offset = 4

    # Ставимо перенос для 3-го елементу (нумерація з 0)
    first_step[indent] += ' + ' + EQUATION_BREAK

    # Розставляємо перенсоси для вирівнювання формули:
    for i in range(offset + indent, len(RESULTS), offset):
        first_step[i] += ' + ' + EQUATION_BREAK

    # Перший крок для обрахунків
    first_formula = r'%s = %s' % (suma, ' + '.join(first_step))

    for i in range(5, len(second_step), 7):
        second_step[i] += '+' + EQUATION_BREAK

    # Другий крок для обрахунків
    second_formula = ' = ' + EQUATION_BREAK + r'= %s = %.2f %s' % (
        ' + '.join(second_step),
        sum(DELTA_FI_SQUARE),
        MEASUREMENT_UNIT
    )

    final_formula = r'\delta = \sqrt{\frac{1}{%s-1} \cdot %.2f }' % (n, sum(DELTA_FI_SQUARE))
    final_formula += '= \sqrt{%.3f}' % (sum(DELTA_FI_SQUARE) / (n - 1))
    final_formula += r'\approx %.3f %s' % (math.sqrt(sum(DELTA_FI_SQUARE) / (n - 1)), MEASUREMENT_UNIT)

    return BEGIN_EQUATION + initial_formula + END_EQUATION + \
           BEGIN_EQUATION + first_formula + second_formula + END_EQUATION + \
           BEGIN_EQUATION + final_formula + END_EQUATION


def print_delta_ca():
    """
    Виводимо середнє квадратичне середнього арифметичного.
    """
    equation_string = r'\delta_{\text{са}} = \frac{\delta}{\sqrt{N}} = \frac{%.3f}{\sqrt{%d}} = %.3f'
    equation_string = equation_string % (DELTA, len(RESULTS), DELTA_CA)

    return BEGIN_EQUATION + equation_string + MEASUREMENT_UNIT + END_EQUATION


def print_table():
    rows = []
    for col in format_data():
        rows.append(r'\rownumber & $$%s$$ & $$%.2f$$ & $$%.2f$$ & \\ \hline' % (col[0], col[1], col[2]))

    rows = '\n'.join(rows)

    # Виводимо нижній рядок таблиці
    bottom_row = r' & $\bar{\varphi} = \frac{1}{%s} \cdot \displaystyle\sum_{i=1}^{%s} \Delta{\varphi_i}=%s$' % (
        len(RESULTS),
        len(RESULTS),
        ARITHMETIC_MEAN_OF_FI,
    )
    bottom_row += r' & %.2f' % sum(DELTA_FI_I)
    bottom_row += r' & $\delta = %.2f %s$' % (DELTA, MEASUREMENT_UNIT)
    bottom_row += r' & \\ \hline'

    return TABLE_BEING + rows + bottom_row + TABLE_END


def print_observations_confident_interval():
    equation_string = r'\Delta_i = %.2f \pm 2.0 \cdot %.3f = ( %.2f \pm %.3f )'
    equation_string = equation_string % (
        ARITHMETIC_MEAN_OF_FI,
        DELTA,
        ARITHMETIC_MEAN_OF_FI,
        2 * float(DELTA)
    )
    return BEGIN_EQUATION + equation_string + MEASUREMENT_UNIT + END_EQUATION


def print_calculations_confident_interval():
    equation_string = r'\Delta_{\text{са}} = %.2f \pm 2.04 \cdot %.3f = ( %.2f \pm %.3f )'
    equation_string = equation_string % (
        ARITHMETIC_MEAN_OF_FI,
        DELTA_CA,
        ARITHMETIC_MEAN_OF_FI,
        2.04 * float(DELTA_CA)
    )
    return BEGIN_EQUATION + equation_string + MEASUREMENT_UNIT + END_EQUATION
