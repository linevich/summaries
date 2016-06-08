import os


def newline_join(lst):
    return '\n'.join(lst)


def amp_join(lst):
    return '&'.join(lst)


def amp_newline_join(lst):
    return '&\n'.join(lst)


def print_to_file(func):
    path = os.path.join('py/', func.__name__ + '.tex')
    path = open(path, 'w')
    path.write(str(func()) + '\n')
