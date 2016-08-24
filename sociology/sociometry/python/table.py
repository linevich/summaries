from python.data import *


def search_by_val(lst, key, value):
    for dictionary in lst:
        for _, val in dictionary.items():
            if dictionary[key] == value:
                return dictionary


def get_by_code(code):
    return search_by_val(PUPILS, 'code', code)


def is_mutual(person, answer):
    choice = get_by_code(answer)
    if person['code'] in choice['answers']:
        return True
    else:
        return False


def get_choices():
    for pupil in PUPILS:
        mutual = []
        i = 0
        for answer in pupil['answers']:
            if is_mutual(pupil, answer):
                if get_by_code(answer) not in mutual:
                    if i == 0 or i == 2:
                        print('+ %s - %s' % (pupil['name'], get_by_code(answer)['name']))
                    if i == 1 or i == 3:
                        print('- %s - %s' % (pupil['name'], get_by_code(answer)['name']))
                    mutual.append(get_by_code(answer))
                    i += 1


get_choices()


def print_table():
    # BEGIN
    begin = [r'\begin{table}', ]
    cols = []
    for _ in PUPILS:
        cols.append('c')
    begin.append(r'\begin{tabular}{|' + '|'.join(cols) + '|}')
    begin = '\n'.join(begin)

    # MIDDLE

    # END
    end = [
        r'\end{tabular}',
        r'\end{table}',
    ]
    end = '\n'.join(end)

    return begin + end
