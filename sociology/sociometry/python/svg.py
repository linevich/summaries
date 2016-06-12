import os
from svgwrite import (
    shapes,
    Drawing,
    mm,
    container,
    text
)

OUTPUT = os.path.join(os.getcwd(), 'py', 'chart.svg')
CENTER = 84 * mm

circle_style = {
    'stroke': 'black',
    'fill': 'none',
    'stroke-width': '0.5mm',
}

# Базове зображення
plot = Drawing(OUTPUT, size=(170 * mm, 170 * mm), profile='full')

group_1 = plot.add(container.SVG())

main_circle_1 = group_1.add(shapes.Circle(center=[CENTER, CENTER], r=34 * mm))
main_circle_1.update(circle_style)

main_circle_2 = plot.add(shapes.Circle(center=[CENTER, CENTER], r=64 * mm))
main_circle_2.update(circle_style)

main_circle_3 = plot.add(shapes.Circle(center=[CENTER, CENTER], r=84 * mm))
main_circle_3.update(circle_style)


def male_unit(size, label):
    polygon = shapes.Polygon(
        points=[
            [size / 2, 0, ],
            [size, size],
            [0, size]
        ])
    polygon.update(circle_style)

    title = text.Text(
        label,
        x=[size / 2],
        y=[size / 1.5]
    )
    title.update({
        'text-anchor': 'middle',
    })
    group = container.Group()
    group.add(polygon)
    group.add(title)
    return group


def female_unit(size, label):
    size = size / 2
    polygon = shapes.Circle(
        center=[size, size],
        r=size
    )
    polygon.update(circle_style)
    title = text.Text(
        label,
        x=[size],
        y=[size]
    )
    title.update({
        'text-anchor': 'middle',
    })
    group = container.Group()
    group.add(polygon)
    group.add(title)
    return group


man = male_unit(50, 'A')
# man.translate(tx=320, ty=100)
group_1.add(man)

women = female_unit(50, 'B')
women.translate(tx=200, ty=100)

# BEGIN
plot.add(women)

plot.save()
