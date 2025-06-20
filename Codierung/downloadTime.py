res_w = float(input("Width: "))
res_h = float(input("Height: "))
fps = float(input("FPS: "))
byte_per_pic = float(input("Byte per Bild: "))
length = float(input("Movie length min: "))
full = res_h * res_w

size = full * byte_per_pic


def print_size(nr: float):
    print("Byte: ", nr)
    print("KB: ", nr / 1000)
    print("MB: ", nr / 1000000)
    print("GB: ", nr / 1000000000)
    print("TB: ", nr / 1000000000000)


print("Speicher für ein Bild ist: " + str(size) + " Byte")

size_full = size * fps * (60 * length)
print("Speicher für den Film ist " + str(size_full / 1000000000) + "GB")

rate = full * byte_per_pic * fps
r = rate / 1000000
print(str(r) + "MB/s oder " + str(round((r * 8) / 1000, 3)) + "Gb/s")

download_time = (size_full * 8) / 1000000000
print(str(round(download_time, 0)) + " Sekunden oder " + str(download_time / 60 / 60))
