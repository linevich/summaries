from svgwrite import (
    shapes,
    container,
    text
)
import os
from copy import copy

SIZE = 600

circle_style = {
    'stroke': 'black',
    'fill': 'none',
    'stroke-width': '0.5mm',
}

person_style = copy(circle_style)
person_style['fill'] = '#ffffff'

person_label_style = {
    'text-anchor': 'middle',
    'font-family': 'GOST Type B',
    'font-style': 'italic',
}


class Person(object):
    def __init__(self, size, label, tx=0, ty=0):
        self.size = size
        self.label = label
        self.tx = SIZE / 2 - self.size / 2 + tx
        self.ty = SIZE / 2 - self.size / 2 + ty
        print('%s %s' % (self.tx, self.ty))

    def create_element(self):
        pass


class Male(Person):
    def create_element(self):
        size = self.size
        label = self.label
        polygon = shapes.Polygon(
            points=[
                [size / 2, 0, ],
                [size, size],
                [0, size]
            ])
        polygon.update(person_style)

        title = text.Text(
            label,
            x=[size / 2],
            y=[size / 1.5]
        )
        title.update(person_label_style)
        group = container.Group()
        group.add(polygon)
        group.add(title)
        group.translate(tx=self.tx, ty=self.ty)
        return group


class Female(Person):
    def create_element(self):
        size = self.size / 2
        label = self.label

        polygon = shapes.Circle(
            center=[size, size],
            r=size
        )
        polygon.update(person_style)
        title = text.Text(
            label,
            x=[size],
            y=[size]
        )
        title.update(person_label_style)
        group = container.Group()
        group.add(polygon)
        group.add(title)
        group.translate(tx=self.tx, ty=self.ty)
        return group


def print_to_file(func):
    path = os.path.join('py/', func.__name__ + '.tex')
    path = open(path, 'w')
    path.write(str(func()) + '\n')
