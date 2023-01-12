# INHERITANCE - SHOULD BE USED IF ONE OBJECT IS SUBTYPE OF ANOTHER OBJECT
# AGGREGATION - SHOULD BE USED IF OBJECT IS NOT A SUBTYPE OF ANOTHER OBJECT, BUT DEPENDS ON SOME PROPERTIES
# COMPOSITION - WHEN AGGREGATED OBJECT CAN'T EXIST AS ALONE OBJECT WITHOUT AGGREGATION

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)


class Cube:

    def __init(self, square: Square):
        self.square = square
        self.height = square.height

    def count_surface_area(self):
        return self.square.count_surface_area() * 6

    def count_volume(self):
        return self.square.count_surface_area() * self.height


class Cuboid:

    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_volume(self):
        return self.base.count_surface_area() * self.height
