# unfinished
import math
from sys import stdin

PI = math.pi

raw = stdin.readlines()
n, r, s, w, f, l1, l2 = map(float, raw[0].split())
race_len = float(raw[1])

curve_len = PI * (r + l1)
track_len = s * 2 + curve_len * 2

dist_needed = race_len - (0.5 * s + f)
pct_needed = dist_needed / curve_len
inner_angle = 180 - (pct_needed * 180)
sin_theta = math.sin(math.radians(inner_angle))
cos_theta = math.cos(math.radians(inner_angle))
print(sin_theta * r, cos_theta * r)