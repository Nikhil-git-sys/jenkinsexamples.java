import sys

def main():
    if len(sys.argv) < 3:
        print("Please provide two integer arguments.")
        return
    
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])

        r1 = n1 + n2
        r2 = n1 - n2
        r3 = n1 * n2

        print("Addition:", r1)
        print("Subtraction:", r2)
        print("Multiplication:", r3)

        if n2 != 0:
            r4 = n1 / n2
            print("Division:", r4)
        else:
            print("Division by zero is not allowed.")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()

