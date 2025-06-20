import math


def to_hex(val):
    hex_digits = "0123456789ABCDEF"
    hex_high = val // 16
    hex_low = val % 16

    return hex_digits[hex_high] + hex_digits[hex_low]


while True:
    what = int(input("Hex zu RGB und CMYK: 1\n CMYK zu RGB und HEX: 2\n RGB zu HEX und CMYK: 3\n"))

    match what:
        case 1:
            hex = input("HEX: ")
            r, g, b = int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)
            print("RGB: R=" + str(r) + ", G=" + str(g) + " ,B=" + str(b))

            c, m, y = 1 - (r / 255), 1 - (g / 255), 1 - (b / 255)
            k = min(c, m, y)

            if k < 1:
                c = round(((c - k) / (1 - k)) * 100, 2)
                m = round(((m - k) / (1 - k)) * 100, 2)
                y = round(((y - k) / (1 - k)) * 100, 2)
                print("C=" + str(c) + "%, M=" + str(m) + "% ,Y=" + str(y) + "% ,K=" + str(round(k, 2) * 100) + "%")


            elif k == 1:
                print("C=0, M=0, Y=0, K=100%")
        case 2:
            c, m, y, k = float(input("C: ")), float(input("M: ")), float(input("Y: ")), float(input("K: "))
            # c, m, y, k in range [0,1]
            r = int(255 * (1 - c) * (1 - k))
            g = int(255 * (1 - m) * (1 - k))
            b = int(255 * (1 - y) * (1 - k))
            print("R: " + str(r) + " ,B: " + str(b) + " ,G: " + str(g))

            hex_color = "#" + to_hex(r) + to_hex(g) + to_hex(b)
            print(hex_color)

        case 3:
            r, g, b = int(input("R: ")), int(input("G: ")), int(input("B: "))
            hex_color = "#" + to_hex(r) + to_hex(g) + to_hex(b)
            print(hex_color)

            c, m, y = 1 - (r / 255), 1 - (g / 255), 1 - (b / 255)
            k = min(c, m, y)

            if k < 1:
                c = round(((c - k) / (1 - k)) * 100, 2)
                m = round(((m - k) / (1 - k)) * 100, 2)
                y = round(((y - k) / (1 - k)) * 100, 2)
                print("C=" + str(c) + "%, M=" + str(m) + "% ,Y=" + str(y) + "% ,K=" + str(round(k, 2)) + "%")

            elif k == 1:
                print("C=0, M=0, Y=0, K=100%")
