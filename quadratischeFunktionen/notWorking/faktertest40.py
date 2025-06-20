import math


def solve_quadratic(a, b, c):
    """Solve quadratic equation given a, b, c coefficients for ax^2 + bx + c = 0"""
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b - sqrt_discriminant) / (2 * a)
        x2 = (-b + sqrt_discriminant) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x1 = -b / (2 * a)
        return x1, x1
    else:
        return None, None


def parse_and_convert_equation(equation):
    equation = equation.replace(" ", "").replace("=0", "")

    # Initialize coefficients
    a = 0
    b = 0
    c = 0

    # Handle the case with parentheses like (x-5)*(x-1)
    if "(" in equation and ")" in equation:
        if equation.startswith("(") and equation.count(")") == 2:
            parts = equation.split(")*(")
            part1 = parts[0].strip("()")
            part2 = parts[1].strip("()")

            if "x" in part1 and "x" in part2:
                if "-" in part1:
                    root1 = float(part1.split("-")[1])
                elif "+" in part1:
                    root1 = -float(part1.split("+")[1])
                else:
                    root1 = 0

                if "-" in part2:
                    root2 = float(part2.split("-")[1])
                elif "+" in part2:
                    root2 = -float(part2.split("+")[1])
                else:
                    root2 = 0

                a = 1
                b = -(root1 + root2)
                c = root1 * root2
                return a, b, c

    # Handle forms like k*(x²+mx+n)
    if "*" in equation and "(" in equation:
        outer_part, inner_part = equation.split("*", 1)
        a = float(outer_part)
        inner_part = inner_part.strip("()")
        if "x²" in inner_part:
            inner_parts = inner_part.split("x²")
            b_part = inner_parts[1]
            if "x" in b_part:
                bx_part, c_part = b_part.split("x")
                b = float(bx_part + "1") if bx_part in ["+", "-"] else float(bx_part)
                c = float(c_part) if c_part else 0
            else:
                b = 0
                c = float(b_part) if b_part else 0
            return a, a * b, a * c

    # Handle standard forms like ax²+bx+c
    if "x²" in equation:
        parts = equation.split("x²")
        if parts[0] == "" or parts[0] == "+":
            a = 1.0
        elif parts[0] == "-":
            a = -1.0
        else:
            a = float(parts[0])
        remainder = parts[1]
        if "x" in remainder:
            bx_part, c_part = remainder.split("x", 1)
            b = float(bx_part + "1") if bx_part in ["+", "-"] else float(bx_part)
            c = float(c_part) if c_part else 0
        else:
            b = 0
            c = float(remainder) if remainder else 0
        return a, b, c

    return None, None, None


def main():
    equation = input("Enter the quadratic equation: ")
    try:
        a, b, c = parse_and_convert_equation(equation)
        if a is not None and b is not None and c is not None:
            result = solve_quadratic(a, b, c)
            if result:
                x1, x2 = result

                print("The solutions are:\n x1=", x1, "\n x2=", x2)
            else:
                print("The equation has no real solutions.")
        else:
            print("Unable to parse the equation.")
    except Exception as e:
        print("An error occurred: "+ e)


if __name__ == "__main__":
    main()
