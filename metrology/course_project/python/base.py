import os


def print_to_file(func):
    path = os.path.join('py/', func.__name__ + '.tex')
    path = open(path, 'w')
    path.write(str(func()) + '\n')