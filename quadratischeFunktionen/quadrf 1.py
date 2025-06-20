def get_input(prompt):
    """A helper function to get float input and handle exceptions."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def format_term(coefficient, variable=None):
    """Manually formats terms to handle signs and zero coefficients without using formatted strings."""
    if coefficient == 0:
        return ""
    sign = "-" if coefficient < 0 else "+"
    abs_coefficient = abs(coefficient)
    if variable:
        if abs_coefficient == 1:
            return " " + sign + " " + variable
        else:
            return " " + sign + " " + str(abs_coefficient) + variable
    else:
        return " " + sign + " " + str(abs_coefficient)



choice = int(
    input(
        "1. Funktion in den drei Formen ausgeben\n2. Funktionsgleichung durch x-Achsen und y-Achse bestimmen\nWähle: "
    )
)

if choice == 1:
    a = get_input("Wie groß ist die Öffnung (a)? ")
    vertex_x = get_input("An welchem X Punkt ist der Scheitelpunkt (h)? ")
    vertex_y = get_input("An welchem Y Punkt ist der Scheitel (v)? ")
    x1 = get_input("An welchem Punkt ist x1? ")
    x2 = get_input("An welchem Punkt ist x2? ")

    # Grundform: a * x^2 + b * x + c
    b = -2 * a * vertex_x
    c = a * vertex_x**2 + vertex_y

    b_term = format_term(b, "x")
    c_term = format_term(c)
    print(
        "Grundform: y ="
        + (" " if a == 1 else (str(a) if a < 0 else " " + str(a)))
        + "x²"
        + b_term
        + c_term
    )

    # Scheitelpunktform: a * (x - h)² + v
    h_term = format_term(-vertex_x)
    fty = format_term(vertex_y)
    print(
        "Scheitelpunktform: y ="
        + (str(a) if a == 1 else ((str(a)) if a < 0 else " " + str(a)))
        + " * (x"
        + h_term
        + ")²"
        + fty
    )

    # Nullstellenform: a * (x - x1)(x - x2)
    x1_term = format_term(-x1)
    x2_term = format_term(-x2)
    print(
        "Nullstellenform: y ="
        + (str(a) if a == 1 else (str(a) if a < 0 else " " + str(a)))
        + " * (x"
        + x1_term
        + ") * (x"
        + x2_term
        + ")"
    )

elif choice == 2:
    k = int(input("1. Scheitelform\n2. Nullstellenform\n3. Grundform\nWähle: "))

    if k == 1:
        x1x = float(input("An welchem X Punkt ist x1?"))
        x1y = float(input("An welchem Y Punkt ist x1?"))
        x2x = float(input("An welchem X Punkt ist x2?"))
        x2y = float(input("An welchem Y Punkt ist x2?"))
        yx = float(input("An welchem X Punkt ist Punkt Y?"))
        yy = float(input("An welchem Y Punkt ist Punkt Y?"))

        u = (x1x + x2x) / 2

        # Now we need to find a and v

        a = ((x1x - u) ** 2) - ((x1y - u) ** 2)

        if a != 0:
            a = (yx - yy) / a
        else:
            a = 0

        v = yy - a * (yx - u) ** 2

        print(
            "Die Funktion lautet: y = ",
            a,
            " * (x ",
            "+ " if u < 0 else "- ",
            abs(u),
            ")² ",
            "- " if v < 0 else "+ ",
            abs(v),
        )
    elif k == 2:
        nx1x = float(input("An welchem X Punkt ist Px1?"))
        nx1y = float(input("An welchem y Punkt ist Px1?"))
        nx2x = float(input("An welchem x Punkt ist Px2?"))
        nx2y = float(input("An welchem y Punkt ist Px2?"))
        np2x = float(input("An welchem x Puntk ist Py?"))
        np2y = float(input("An welchem y Puntk ist Py?"))

        nx1 = np2x - nx1x
        nx2 = np2x - nx2x

        if np2y != 0:
            na = np2y / (nx1 * nx2)
        else:
            na = 0
        print(
            "Die Nullstellen Formel lautet: \n ",
            np2y,
            "=",
            na,
            " * (x",
            "+" if nx1x < 0 else "- ",
            abs(nx1x),
            ") * (x",
            "+" if nx2x < 0 else "-",
            abs(nx2x),
            ")",
        )
    elif k == 3:
        x1x = float(input("An welchem X Punkt ist x1?"))
        x1y = float(input("An welchem Y Punkt ist x1?"))
        x2x = float(input("An welchem X Punkt ist x2?"))
        x2y = float(input("An welchem Y Punkt ist x2?"))
        yx = float(input("An welchem X Punkt ist Punkt Y?"))
        yy = float(input("An welchem Y Punkt ist Punkt Y?"))

        a = (x1y - x2y) / ((x1x - x2x) ** 2)
        b = -2 * a * x1x
        c = a * x1x**2 + x1y

        print(
            "Die Grundformel lautet: y = ",
            a,
            "x²",
            "+" if b < 0 else "-",
            abs(b),
            "x",
            "+" if c < 0 else "-",
            abs(c),
        )
    else:
        print("Ungültige Eingabe")
else:
    print("Ungültige Eingabe")

