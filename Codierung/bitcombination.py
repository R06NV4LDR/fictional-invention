import math
n = int(input("Wie viele Kombinationen? "))
bits = math.ceil(math.log(n, 2))
print("Mindestens nötig:", bits, "Bit")
