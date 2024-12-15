import sys
sys.path.append('..')
from shapely import box, MultiPolygon
from collections import defaultdict
from utils import read_input

'''
    This solution is not mine. Found from some dude on reddit.
    Thank you very much @whyrememberpassword

    Shapely looks hot though
'''

shapes = defaultdict(MultiPolygon)

inp = read_input('input.txt')
for r, line in enumerate(inp):
    for c, color in enumerate(line):
        shapes[color] = shapes[color].union( box(r, c, r + 1, c + 1) )

total = 0
for color, polys in shapes.items():
    for poly in polys.geoms if hasattr(polys, "geoms") else [polys]:
        poly = poly.simplify(tolerance=1e-1)
        sides = len(poly.exterior.coords) - 1
        for interior in poly.interiors:
            sides += len(interior.coords) - 1
        total += poly.area * sides

print(f'Total price of the fence: {int(total)}')