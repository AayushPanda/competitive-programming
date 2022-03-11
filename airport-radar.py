from math import sin, cos, tan, radians, degrees, sqrt

outs = []

def get_dist(x1, y1, x2, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


def get_line_dist(x, y, d):
    if d%90!=0:
        return abs((cos(d) * (0 - y)) - (sin(d) * (0 - x)))


def main():
    import sys
    input = sys.stdin.readline

    d, l, n = map(int, input().split())
    d = radians(d)
    pp = [l * (cos(d)), l * (sin(d))]

    airports = [list(map(int, input().split())) for _ in range(n)]

    count = 0

    for radar in airports:
        print(get_dist(radar[0], radar[1], pp[0], pp[1]), get_line_dist(radar[0], radar[1], d))
        if get_dist(0, 0, radar[0], radar[1]) <= get_line_dist(radar[0], radar[1], d) <= get_dist(radar[0], radar[1], pp[0], pp[1]):
            count += 1

    outs.append(f"The jet will appear on {count} radar screens.")


[main() for _ in range(2)]

for out in outs:
    print(out)
