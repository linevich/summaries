from svgwrite import (
    shapes,
    container,
    text
)

SIZE = 600

circle_style = {
    'stroke': 'black',
    'fill': 'none',
    'stroke-width': '0.5mm',
}


class Person(object):
    def __init__(self, size, label, tx=0, ty=0):
        self.size = size
        self.label = label
        self.tx = SIZE / 2 - self.size / 2 + tx
        self.ty = SIZE / 2 - self.size / 2 + ty

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
        group.translate(tx=self.tx, ty=self.ty)
        return group
