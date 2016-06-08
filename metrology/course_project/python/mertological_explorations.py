"""
Обрахунки до 3-го розділу.
-------------------------

Дослідження метрологічних характеристик гігрометру ВИТ1.

Результати вимірювання подані в форматі [ [Вологість, Ємність], ..., ]
"""
from python.base import newline_join, amp_join, amp_newline_join
from python.indirect_mesurment import BEGIN_EQUATION, END_EQUATION, EQUATION_BREAK

RESULTS = [
    [24.1, 11.0],
    [32.3, 25.6],
    [42.0, 34.3],
    [53.1, 45.2],
    [67.0, 60.0],
    [82.3, 72.2],
    [65.9, 59.4],
    [51.6, 45.0],
    [42.4, 34.7],
    [33.2, 25.5],
    [24.0, 10.6],
]

RESULTS_COUNT = len(RESULTS)

MEASUREMENT_UNITS = r'\text{ пкФ}/\%'


def find_sensitivity():
    """
    Розрахуємо чутливість для кожного з результатів.

    :return: Список значень чутливості для кожного вимірювання.
    """
    sensitivity = []

    for humidity, capacitance in RESULTS:
        sensitivity.append(round(capacitance / humidity, 2))

    return sensitivity


SENSITIVITY = find_sensitivity()


def print_sensitivity():
    """
    Виведення обрахунків чутливості в LaTeX.
    """

    formula_string = r'S_{%s} &= \frac{%s}{%s} &= %.2f %s; %s'
    output_formula = []

    counter = 0
    before = ''

    first_column = int(round(RESULTS_COUNT / 2))

    for i in range(RESULTS_COUNT):
        counter += 1

        if counter == 1:
            before = r'\begin{aligned}[t]'
            after = r'\\[1em]'

        elif counter == first_column:
            after = r'\end{aligned} \qquad \qquad  \begin{aligned}[t]'

        elif counter == RESULTS_COUNT:
            after = r'\end{aligned}'
        else:
            before = ''
            after = r'\\[1em] '

        output_formula.append(
            before +
            formula_string % (
                i + 1,
                RESULTS[i][1],
                RESULTS[i][0],
                SENSITIVITY[i],
                MEASUREMENT_UNITS,
                after,
            ))

    output_formula = r'\begin{equation}' + '\n' + '\n'.join(output_formula) + '\n' + r'\end{equation}'
    return output_formula


# Обраховуємо середню чутливість.
SENSITIVITY_AM = sum(SENSITIVITY) / RESULTS_COUNT


def print_sensitivity_am():
    """
    Виводимо середню чутливість в LaTeX
    """
    suma = r'\sum S_{\text{cp}} = %s = %s'

    sensivity = []
    sensivity += SENSITIVITY
    sensivity.insert(8, EQUATION_BREAK)
    sensivity = (str(item) for item in sensivity)

    suma %= ('+'.join(sensivity), str(sum(SENSITIVITY)) + MEASUREMENT_UNITS)

    formula = r' S_{\text{cp}} = \frac{%.2f}{%s} = %.2f %s'
    formula %= (
        sum(SENSITIVITY),
        RESULTS_COUNT,
        SENSITIVITY_AM,
        MEASUREMENT_UNITS
    )
    return BEGIN_EQUATION + suma + END_EQUATION + \
           BEGIN_EQUATION + formula + END_EQUATION


def print_sensitivity_table():
    """
    Генерування таблиці результатів.

    :return: вивід таблиці в LaTeX
    """
    begin = [
        r'\begin{table}[ht!]',
        r'\caption{Результати обрахунків та вимірювань}',
        r'\label{t:metrological_exp}',
    ]

    begin = newline_join(begin) + '\n'

    end = [
        r'\end{tabular}',
        r'\end{table}',
    ]
    end = newline_join(end)

    newline = r' \\ \hline' + '\n'

    tabular = []
    tabular_string = r'\begin{tabular}{|%s|}'

    for col in range(RESULTS_COUNT + 1):
        tabular.append('c')

    tabular = tabular_string % '|'.join(tabular) + '\n\\hline\n'

    first_row = [r'\multicolumn{1}{|c|}{$\varphi$,~\%}', ]
    first_row_string = r'\multicolumn{1}{c|}{%s}'

    second_row = [r'$C$,~\text{пФ}', ]
    second_row_string = ' $%s$ '

    for humidity, capacitance in RESULTS:
        first_row.append(first_row_string % humidity)
        second_row.append(second_row_string % capacitance)

    third_six_rows = [
        r'$\Delta C_1$, ~\text{пФ} & \multicolumn{11}{|c|}{$1$}  \\ \hline',
        r'$\Delta C_2$, ~\text{пФ} & \multicolumn{11}{|c|}{$1$}  \\ \hline',
        r'$\Delta C_{\sum}$, ~пФ  & \multicolumn{11}{|c|}{$1$}  \\ \hline',
        r'$y_{\sum}$, ~\%  & \multicolumn{11}{|c|}{$1$}  \\ \hline',
    ]

    # for row in third_six_rows:
    #     row = row.format(1)

    bottom_row = [r'$\delta_n$, ~\%', ]
    bottom_row_string = ' $%s$ '

    for humidity, capacitance in RESULTS:
        bottom_row.append(bottom_row_string % humidity)

    first_row = amp_newline_join(first_row) + newline
    second_row = amp_join(second_row) + newline
    third_six_rows = newline_join(third_six_rows) + '\n'  # % (1, 2, 3, 4)
    bottom_row = amp_join(bottom_row) + newline

    return begin + tabular + first_row + second_row + third_six_rows + bottom_row + end
