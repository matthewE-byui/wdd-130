import math

def kinematics():
    print("\nKinematics Equations:")
    print("1. v = u + at")
    print("2. s = ut + 0.5at^2")
    print("3. v^2 = u^2 + 2as")
    try:
        choice = input("Choose an equation (1/2/3): ")
        
        if choice == "1":
            u = float(input("Initial velocity (u) m/s: "))
            a = float(input("Acceleration (a) m/s²: "))
            t = float(input("Time (t) s: "))
            v = u + a * t
            print(f"Final velocity (v) = {v} m/s")
        elif choice == "2":
            u = float(input("Initial velocity (u) m/s: "))
            a = float(input("Acceleration (a) m/s²: "))
            t = float(input("Time (t) s: "))
            s = u * t + 0.5 * a * t ** 2
            print(f"Displacement (s) = {s} m")
        elif choice == "3":
            u = float(input("Initial velocity (u) m/s: "))
            a = float(input("Acceleration (a) m/s²: "))
            s = float(input("Displacement (s) m: "))
            v = math.sqrt(u ** 2 + 2 * a * s)
            print(f"Final velocity (v) = {v} m/s")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def force():
    print("\nNewton's Second Law: F = ma")
    try:
        m = float(input("Mass (m) kg: "))
        a = float(input("Acceleration (a) m/s²: "))
        F = m * a
        print(f"Force (F) = {F} N")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def energy():
    print("\nEnergy Equations:")
    print("1. Kinetic Energy: KE = 0.5mv^2")
    print("2. Potential Energy: PE = mgh")
    try:
        choice = input("Choose an equation (1/2): ")
        
        if choice == "1":
            m = float(input("Mass (m) kg: "))
            v = float(input("Velocity (v) m/s: "))
            KE = 0.5 * m * v ** 2
            print(f"Kinetic Energy (KE) = {KE} J")
        elif choice == "2":
            m = float(input("Mass (m) kg: "))
            g = 9.81  # Gravity on Earth
            h = float(input("Height (h) m: "))
            PE = m * g * h
            print(f"Potential Energy (PE) = {PE} J")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def circuits():
    print("\nOhm's Law: V = IR")
    try:
        V = float(input("Voltage (V) V: "))
        R = float(input("Resistance (R) Ω: "))
        I = V / R
        print(f"Current (I) = {I} A")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("Resistance cannot be zero.")

def main():
    while True:
        print("\nPhysics Calculator")
        print("1. Kinematics")
        print("2. Force (Newton's Second Law)")
        print("3. Energy (Kinetic & Potential)")
        print("4. Circuits (Ohm's Law)")
        print("5. Exit")
        
        try:
            choice = input("Select a category (1-5): ")
            if choice == "1":
                kinematics()
            elif choice == "2":
                force()
            elif choice == "3":
                energy()
            elif choice == "4":
                circuits()
            elif choice == "5":
                print("Exiting calculator. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")
        except OSError:
            print("I/O error encountered. Please try again.")
        except KeyboardInterrupt:
            print("\nProcess interrupted. Exiting...")
            break

if __name__ == "__main__":
    main()
