import math

def get_float_input(prompt):
    while True:
        try:
            response = input(prompt)
            return float(response)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_values():
    a = get_float_input("Enter coefficient a: ")
    b = get_float_input("Enter coefficient b: ")
    c = get_float_input("Enter coefficient c: ")
    start = int(get_float_input("Enter the start of x values: "))
    end = int(get_float_input("Enter the end of x values: "))
    x_values = range(start, end + 1)
    print("x y")
    for x in x_values:
        y = a * x ** 2 + b * x + c
        print(x, y)

def solve_quadratic():
    a = get_float_input("Enter coefficient a: ")
    b = get_float_input("Enter coefficient b: ")
    c = get_float_input("Enter coefficient c: ")
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("No real roots")
    elif discriminant == 0:
        root = -b / (2 * a)
        print("One real root: x =", root)
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        print("Two real roots: x1 =", root1, ", x2 =", root2)

def solve_quadratic2(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("No real roots")
    elif discriminant == 0:
        root = -b / (2 * a)
        print("One real root: x =", root)
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        print("Two real roots: x1 =", root1, ", x2 =", root2)
        return root1, root2

def vertex_form():
    a = get_float_input("Enter the known coefficient a: ")
    h = get_float_input("Enter the x-coordinate of the vertex (h): ")
    k = get_float_input("Enter the y-coordinate of the vertex (k): ")
    x = get_float_input("Enter the x-coordinate of another point: ")
    y = get_float_input("Enter the y-coordinate of the same point: ")
    a_calculated = (y - k) / ((x - h) ** 2)
    print("Vertex form: y =", a_calculated, "*(x -", h, ")^2 +", k)

def intersections_with_axes():
    a = get_float_input("Enter coefficient a: ")
    b = get_float_input("Enter coefficient b: ")
    c = get_float_input("Enter coefficient c: ")
    # Solving for x intercepts
    roots = solve_quadratic2(a, b, c)
    y_intercept = a * 0 ** 2 + b * 0 + c
    print("Y-intercept at y =", y_intercept)

print("Select the function you want to use:")
print("1. Calculate values for a range of x")
print("2. Solve a quadratic equation")
print("3. Find vertex form given a vertex and a point")
print("4. Find intersections with the axes")
choice = input("Enter your choice (1-4): ")
if choice == '1':
    calculate_values()
elif choice == '2':
    solve_quadratic()
elif choice == '3':
    vertex_form()
elif choice == '4':
    intersections_with_axes()
else:
    print("Invalid choice")

