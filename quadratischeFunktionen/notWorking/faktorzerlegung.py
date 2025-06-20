# Lösen con quadratischen Gleichungen
# Faktorzerlegung
# Nimm eine Formel wir x²+8x=0 und gib zurück x1 und x2
inputsa = int(input("Faktorzerlegung (1) \nQuadratische Gleichung lösen (2) \n"))

if inputsa == 1:
    a = float(input("Gib den Wert von a ein: "))
    b = float(input("Gib den Wert von b ein: "))
    c = float(input("Gib den Wert von c ein: "))

    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        # Two real and distinct solutions
        sqrt_discriminant = discriminant**0.5
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        print("x1 =", x1, "x2 =", x2)
    elif discriminant == 0:
        # One real solution
        x1 = x2 = -b / (2 * a)
        print("x1 = x2 =", x1)
    else:
        # No real solutions
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * a)
        print("x1 =", real_part, "+", imaginary_part, "i")
        print("x2 =", real_part, "-", imaginary_part, "i")
        print("\nnothing found")
elif inputsa == 2:
    equation = input("Enter the quadratic equation in the form 'ax^2 + bx + c = 0': ")
    # Calculate the discriminant
    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        # Two real and distinct solutions
        sqrt_discriminant = discriminant**0.5
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        # One real solution
        x1 = x2 = -b / (2 * a)
        return x1, x2
    else:
        # No real solutions
        return None, None
