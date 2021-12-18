import re


def get_box(text):
    return [int(n) for n in re.findall("-?\d+", text)]


def step(px, py, vx, vy):
    px += vx
    py += vy

    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1

    vy -= 1

    return (px, py, vx, vy)


def check(px, py, has_hit):

    if px > X_MAX or py < Y_MIN:
        return py, has_hit, False

    if X_MIN <= px <= X_MAX and Y_MIN <= py <= Y_MAX:
        has_hit = True
        return py, has_hit, True

    return py, has_hit, True


# TARGET = "target area: x=20..30, y=-10..-5"
TARGET = "target area: x=56..76, y=-162..-134"

X_MIN, X_MAX, Y_MIN, Y_MAX = get_box(TARGET)


def shoot(vx, vy):
    max_py = 0
    has_hit = False
    v = (0, 0, vx, vy)

    while True:
        v = step(*v)
        new_py, has_hit, keep_going = check(v[0], v[1], has_hit)
        if not keep_going:
            if has_hit:
                return max_py
            else:
                return None
        if new_py > max_py:
            max_py = new_py


def search():
    for vx in range(-200, 200, 1):
        for vy in range(-200, 200, 1):
            hit = shoot(vx, vy)
            if hit is not None:
                yield (vx, vy)
