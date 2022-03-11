from math import sin, cos, radians, sqrt, isclose

outs = []


def get_dist(x1, y1, x2, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def get_line_dist(x1, y1, d, x2, y2):
    if d % 90 != 0 and is_intersecting(x2, y2, x1, y1):
        return abs((cos(d) * (0 - y1)) - (sin(d) * (0 - x1)))
    elif (d == 180 or d == 0) and (0 <= x1 <= x2 or 0 >= x1 >= x2):
        return abs(y1)
    elif (d == 90 or d == 270) and (0 <= y1 <= y2 or 0 >= y1 >= y2):
        return abs(x1)
    return -1


def is_intersecting(x1, y1, x2, y2):
    x_inter = (y1 * x1 * y2 + ((x1 ** 2) * x2)) / ((x1 ** 2) + (y1 ** 2))
    y_inter = (y1 / x1) * x_inter
    return isclose(get_dist(0, 0, x_inter, y_inter) + get_dist(x_inter, y_inter, x1, y1), get_dist(0, 0, x1, y1))


def main():
    import sys
    input = sys.stdin.readline

    d, l, n = map(int, input().split())
    d = radians(d)
    pp = [l * (cos(d)), l * (sin(d))]

    airports = [list(map(int, input().split())) for _ in range(n)]

    count = 1

    for radar in airports:
        dist_start = get_dist(0, 0, radar[0], radar[1])
        dist_end = get_dist(radar[0], radar[1], pp[0], pp[1])
        dist_path = get_line_dist(radar[0], radar[1], d, pp[0], pp[1])
        if min(dist_start, dist_end) <= radar[2]:
            count += 1
        elif dist_path != -1 and dist_path <= radar[2]:
            count += 1
    print(f"The jet will appear on {count} radar screens.")

[main() for _ in range(5)]
