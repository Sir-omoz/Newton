class Math:
    def addition(self, a, b):
        add = a + b
        return add

    def subtraction(self, a, b):
        subtract = a - b
        return subtract

    def multiplication(self, a, b):
        mult = a * b
        return mult

    def division(self, a, b):
        divide = a / b
        return divide

    def modulus(self, a, b):
        mod = a % b
        return mod


class Physics:
    def distance(self, v, t):
        distance = v * t
        return distance

    def velocity(self, d, t):
        velocity = d / t
        return velocity

    def acceleration(self, v, u, t):
        acceleration = (v - u) / t
        return acceleration

    def force(self, m, a):
        force = m * a
        return force

    def momentum(self, m, v):
        momentum = m * v
        return momentum


# Main program
print("Welcome to the Math/Physics calculator!")
while True:
    class_choice = input("Do you want to calculate Math or Physics? ").lower()
    if class_choice not in ["math", "physics"]:
        print("Invalid input! Please choose Math or Physics.")
    else:
        break

if class_choice == "math":
    math = Math()
    print("Choose an operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    while True:
        operation_choice = input("Enter your choice (1-5): ")
        if operation_choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid input! Please choose an operation (1-5).")
        else:
            break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation_choice == "1":
        print(num1, "+", num2, "=",math.addition(num1, num2))

    if operation_choice == "2":
        print(num1, "-", num2, "=", math.subtraction(num1, num2))

    if operation_choice == "3":
        print(num1, "*", num2, "=", math.multiplication(num1, num2))

    if operation_choice == "4":
        print(num1, "/", num2, "=", math.division(num1, num2))

    if operation_choice == "5":
        print(num1, "%", num2, "=", math.modulus(num1, num2))

if class_choice == "physics":
    physics = Physics()
    print("Choose an operation: ")
    print("1. Distance")
    print("2. Velocity")
    print("3. Acceleration")
    print("4. Force")
    print("5. Momentum")
    while True:
        operation_choice = input("Enter your choice (1-5): ")
        if operation_choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid input! Please choose an operation (1-5).")
        else:
            break

    if operation_choice == "1":
        v = float(input("Enter the velocity: "))
        t = float(input("Enter the time: "))
        print("Distance =", physics.distance(v, t))

    if operation_choice == "2":
        d = float(input("Enter the distance: "))
        t = float(input("Enter the time: "))
        print("veocity =", physics.velocity(d, t))

    if operation_choice == "3":
        v = float(input("Enter the final velocity: "))
        u = float(input("Enter the initial velocity: "))
        t = float(input("Enter the time: "))
        print("acceleration =", physics.acceleration(v, u, t))

    if operation_choice == "4":
        m = float(input("Enter the mass: "))
        a = float(input("Enter the acceleration: "))
        print("force =", physics.force(m, a))

    if operation_choice == "5":
        m = float(input("Enter the mass: "))
        v = float(input("Enter the velocity: "))
        print("momentum =", physics.momentum(m, v))