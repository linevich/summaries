import os
from svgwrite import (
    Drawing,
)
from python.base import *

OUTPUT = os.path.join(os.getcwd(), 'py', 'chart.svg')
CENTER = SIZE / 2

CIRCLE_1 = CENTER - 200
CIRCLE_2 = CENTER - 100

# Базове зображення
plot = Drawing(OUTPUT, size=(SIZE, SIZE), profile='full')

group_1 = plot.add(container.Group())

main_circle_1 = group_1.add(shapes.Circle(center=[CENTER, CENTER], r=CIRCLE_1))
main_circle_1.update(circle_style)

main_circle_2 = plot.add(shapes.Circle(center=[CENTER, CENTER], r=CIRCLE_2))
main_circle_2.update(circle_style)

main_circle_3 = plot.add(shapes.Circle(center=[CENTER, CENTER], r=CENTER))
main_circle_3.update(circle_style)

man = Male(
    size=50,
    label='A',
    tx=50
)
women = Female(
    size=50,
    label='B',
)

plot.add(man.create_element())
plot.add(women.create_element())


# BEGIN
plot.save()
