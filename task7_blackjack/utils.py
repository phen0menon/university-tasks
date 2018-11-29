import math
from enum import Enum


class TypeClassifyPoint(Enum):
    LEFT = 0  # СЛЕВА
    RIGHT = 1  # СПРАВА
    BEYOND = 2  # ВПЕРЕДИ
    BEHIND = 3  # ПОЗАДИ
    BETWEEN = 4  # МЕЖДУ
    ORIGIN = 5  # НАЧАЛО
    DESTINATION = 6  # КОНЕЦ


class TypeClassifyEdge(Enum):
    TOUCHING = 0  # КАСАТЕЛbНОЕ
    CROSSING = 1  # ПЕРЕСЕКАЮЩЕЕ
    INESSENTIAL = 2  # НЕСУЩЕСТВЕННОЕ


class TypeLocationPoint(Enum):
    INSIDE = 0  # ВНУТРИ
    OUTSIDE = 1  # ВНЕ
    BOUNDARY = 2  # НА ГРАНИЦЕ


def pts_equal(pt1, pt2):
    return (pt1[0] == pt2[0]) and (pt1[1] == pt2[1])

def sub_point(pt1, pt2):
    return [pt1[0]-pt2[0], pt1[1]-pt2[1]]

def distance_point(pt1, pt2):
    return math.sqrt(math.pow(pt1[0]-pt2[0], 2) + math.pow(pt1[1]-pt2[1], 2))

def classify(pt0, pt1, pt2):
    a = sub_point(pt1, pt0)
    b = sub_point(pt2, pt0)
    sa = a[0]*b[1]-b[0]*a[1]

    if sa > 0:
        return TypeClassifyPoint.LEFT
    elif sa < 0:
        return TypeClassifyPoint.RIGHT
    elif (a[0]*b[0] < 0) or (a[1]*b[1] < 0):
        return TypeClassifyPoint.BEHIND
    elif math.sqrt(a[0]*a[0]+a[1]*a[1]) < math.sqrt(b[0]*b[0]+b[1]*b[1]):
        return TypeClassifyPoint.BEYOND
    elif pts_equal(pt0, pt2):
        return TypeClassifyPoint.ORIGIN
    elif pts_equal(pt1, pt2):
        return TypeClassifyPoint.DESTINATION
    else:
        return TypeClassifyPoint.BETWEEN


def edge_type(pt_arg, pt_a, pt_b):
    pt_type = classify(pt_a, pt_b, pt_arg)

    if pt_type == TypeClassifyPoint.LEFT:
        return TypeClassifyEdge.CROSSING if (pt_a[1] < pt_arg[1]) and (pt_arg[1] <= pt_b[1]) else TypeClassifyEdge.INESSENTIAL
    elif pt_type == TypeClassifyPoint.RIGHT:
        return TypeClassifyEdge.CROSSING if (pt_b[1] < pt_arg[1]) and (pt_arg[1] <= pt_a[1]) else TypeClassifyEdge.INESSENTIAL
    elif (pt_type == TypeClassifyPoint.BETWEEN) or (pt_type == TypeClassifyPoint.ORIGIN) or (pt_type == TypeClassifyPoint.DESTINATION):
        return TypeClassifyEdge.TOUCHING
    else:
        return TypeClassifyEdge.INESSENTIAL


def is_polygon_contains_pt(pt_arg, list_pts):
    parity = 0
    for i in range(len(list_pts)):
        type_edge = 0
        if i == len(list_pts)-1:
            type_edge = edge_type(pt_arg, list_pts[i], list_pts[0])
        else:
            type_edge = edge_type(pt_arg, list_pts[i], list_pts[i+1])

        if type_edge == TypeClassifyEdge.TOUCHING:
            return TypeLocationPoint.BOUNDARY
        elif type_edge == TypeClassifyEdge.CROSSING:
            parity = 1-parity

    return TypeLocationPoint.INSIDE if parity else TypeLocationPoint.OUTSIDE


class Rect:
    def __init__(self, left, top, width, height):
        self._left = left
        self._right = left+width
        self._top = top
        self._bottom = top+height

    def contains(self, pt):
        return ((self._left <= pt[0]) and (self._right >= pt[0]) and
                (self._top <= pt[1]) and (self._bottom >= pt[1]))

    def intersect(self, rect):
        pass

    def top_left(self):
        return [self._left, self._top]

    def top_right(self):
        return [self._right, self._top]

    def bottom_left(self):
        return [self._left, self._bottom]

    def bottom_right(self):
        return [self._right, self._bottom]


class Polygon:
    def __init__(self, list_pts=[], src_pt=[0, 0]):
        self._src_pt = list(src_pt)
        self._pts = list(list_pts)

    def move_by(self, offset_pt):
        self._src_pt[0] += offset_pt[0]
        self._src_pt[1] += offset_pt[1]

        for pt in self._pts:
            pt[0] += offset_pt[0]
            pt[1] += offset_pt[1]

    def rotate(self, angle_degress):
        for pt in self._pts:
            prev_values = [pt[0] - self._src_pt[0], pt[1] - self._src_pt[1]]

            pt[0] = self._src_pt[0] + prev_values[0]*math.cos(math.radians(angle_degress)) - prev_values[1]*math.sin(math.radians(angle_degress))
            pt[1] = self._src_pt[1] + prev_values[0]*math.sin(math.radians(angle_degress)) + prev_values[1]*math.cos(math.radians(angle_degress))

    def contains(self, pt):
        return is_polygon_contains_pt(pt, self._pts) != TypeLocationPoint.OUTSIDE

    def intersect(self, primitive):
        if isinstance(primitive, Rect):
            if (is_polygon_contains_pt(primitive.top_left(), self._pts) or is_polygon_contains_pt(primitive.top_right(), self._pts) or
               is_polygon_contains_pt(primitive.bottom_left(), self._pts) or is_polygon_contains_pt(primitive.bottom_right(), self._pts)):
                return True
        elif isinstance(primitive, Polygon):
            for pt in primitive._pts:
                if self.contains(pt):
                    return True

        return False
