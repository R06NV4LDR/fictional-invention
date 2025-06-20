import math


def to_hex(val):
    hex_digits = "0123456789ABCDEF"
    hex_high = val // 16
    hex_low = val % 16
    print(f"to_hex({val}) -> High: {hex_high} ({hex_digits[hex_high]}), Low: {hex_low} ({hex_digits[hex_low]})")
    return hex_digits[hex_high] + hex_digits[hex_low]


while True:
    what = int(input("Hex zu RGB und CMYK: 1\nCMYK zu RGB und HEX: 2\nRGB zu HEX und CMYK: 3\n"))

    if what == 1:
        hex_val = input("HEX (z.B. FF00FF): ")
        r, g, b = int(hex_val[0:2], 16), int(hex_val[2:4], 16), int(hex_val[4:6], 16)

        print(f"HEX {hex_val} → R: {hex_val[0:2]} = {r}, G: {hex_val[2:4]} = {g}, B: {hex_val[4:6]} = {b}")
        print(f"RGB: R={r}, G={g}, B={b}")

        c = 1 - (r / 255)
        m = 1 - (g / 255)
        y = 1 - (b / 255)

        print(f"CMY vor K-Berechnung: C={c}, M={m}, Y={y}")

        k = min(c, m, y)
        print(f"K = min(C, M, Y) = {k}")

        if k < 1:
            c_calc = ((c - k) / (1 - k)) * 100
            m_calc = ((m - k) / (1 - k)) * 100
            y_calc = ((y - k) / (1 - k)) * 100
            print(f"C = (({c} - {k}) / (1 - {k})) * 100 = {c_calc}")
            print(f"M = (({m} - {k}) / (1 - {k})) * 100 = {m_calc}")
            print(f"Y = (({y} - {k}) / (1 - {k})) * 100 = {y_calc}")
            print(f"K = {k} * 100 = {round(k * 100, 2)}")

            print(f"C={round(c_calc, 2)}%, M={round(m_calc, 2)}%, Y={round(y_calc, 2)}%, K={round(k * 100, 2)}%")
        else:
            print("C=0, M=0, Y=0, K=100%")

    elif what == 2:
        c = float(input("C (0–1): "))
        m = float(input("M (0–1): "))
        y = float(input("Y (0–1): "))
        k = float(input("K (0–1): "))

        print(f"Berechnung RGB aus CMYK:")
        r = int(255 * (1 - c) * (1 - k))
        g = int(255 * (1 - m) * (1 - k))
        b = int(255 * (1 - y) * (1 - k))

        print(f"R = 255 * (1 - {c}) * (1 - {k}) = {r}")
        print(f"G = 255 * (1 - {m}) * (1 - {k}) = {g}")
        print(f"B = 255 * (1 - {y}) * (1 - {k}) = {b}")

        print(f"RGB: R={r}, G={g}, B={b}")

        hex_color = "#" + to_hex(r) + to_hex(g) + to_hex(b)
        print(f"HEX: {hex_color}")

    elif what == 3:
        r = int(input("R (0–255): "))
        g = int(input("G (0–255): "))
        b = int(input("B (0–255): "))

        print(f"Umwandlung RGB → HEX")
        hex_color = "#" + to_hex(r) + to_hex(g) + to_hex(b)
        print(f"HEX: {hex_color}")

        c = 1 - (r / 255)
        m = 1 - (g / 255)
        y = 1 - (b / 255)

        print(f"CMY vor K-Berechnung: C={c}, M={m}, Y={y}")

        k = min(c, m, y)
        print(f"K = min(C, M, Y) = {k}")

        if k < 1:
            c_calc = ((c - k) / (1 - k)) * 100
            m_calc = ((m - k) / (1 - k)) * 100
            y_calc = ((y - k) / (1 - k)) * 100
            print(f"C = (({c} - {k}) / (1 - {k})) * 100 = {c_calc}")
            print(f"M = (({m} - {k}) / (1 - {k})) * 100 = {m_calc}")
            print(f"Y = (({y} - {k}) / (1 - {k})) * 100 = {y_calc}")
            print(f"K = {k} * 100 = {round(k * 100, 2)}")

            print(f"C={round(c_calc, 2)}%, M={round(m_calc, 2)}%, Y={round(y_calc, 2)}%, K={round(k * 100, 2)}%")
        else:
            print("C=0, M=0, Y=0, K=100%")
