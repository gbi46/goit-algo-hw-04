import math

def koch_segments(p0, p1, depth, out):
    if depth == 0:
        out.append((p0, p1))
        return
    v = (p1[0]-p0[0], p1[1]-p0[1])
    one_third = (p0[0] + v[0]/3.0, p0[1] + v[1]/3.0)
    two_third = (p0[0] + 2*v[0]/3.0, p0[1] + 2*v[1]/3.0)

    # Punkt der Spitze (60°-Drehung um one_third)
    # Rot(v/3) um +60°:
    vx, vy = v[0]/3.0, v[1]/3.0
    cos60, sin60 = 0.5, math.sqrt(3)/2.0
    rx = vx*cos60 - vy*sin60
    ry = vx*sin60 + vy*cos60
    peak = (one_third[0] + rx, one_third[1] + ry)

    koch_segments(p0, one_third, depth-1, out)
    koch_segments(one_third, peak, depth-1, out)
    koch_segments(peak, two_third, depth-1, out)
    koch_segments(two_third, p1, depth-1, out)

def snowflake_segments(size, depth):
    # Gleichseitiges Dreieck zentriert um (0,0)
    h = math.sqrt(3) * size / 2.0
    p0 = (-size/2.0, -h/3.0)
    p1 = ( size/2.0, -h/3.0)
    p2 = (0.0, 2.0*h/3.0)

    segs = []
    koch_segments(p0, p1, depth, segs)
    koch_segments(p1, p2, depth, segs)
    koch_segments(p2, p0, depth, segs)
    return segs

def write_svg(segments, filename="koch_snowflake.svg", stroke_width=1.5, margin=10):
    xs = [x for (a,b) in segments for x in (a[0], b[0])]
    ys = [y for (a,b) in segments for y in (a[1], b[1])]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)

    width = (maxx - minx) + 2*margin
    height = (maxy - miny) + 2*margin

    def tx(x): return (x - minx) + margin
    # SVG hat y nach unten, daher invertieren:
    def ty(y): return (maxy - y) + margin

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.2f}" height="{height:.2f}" viewBox="0 0 {width:.2f} {height:.2f}">\n')
        f.write('<g fill="none" stroke="black" stroke-linecap="round" stroke-linejoin="round">\n')
        f.write(f'<g stroke-width="{stroke_width}">\n')
        for (a, b) in segments:
            f.write(f'<line x1="{tx(a[0]):.3f}" y1="{ty(a[1]):.3f}" x2="{tx(b[0]):.3f}" y2="{ty(b[1]):.3f}" />\n')
        f.write('</g>\n</g>\n</svg>\n')

def main():
    try:
        depth = int(input("Enter recursion depth (e.g. 0-6): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    size = 300
    segments = snowflake_segments(size, depth)
    write_svg(segments, filename="koch_snowflake.svg", stroke_width=1.2)
    print("Done. Wrote koch_snowflake.svg")

if __name__ == "__main__":
    main()
