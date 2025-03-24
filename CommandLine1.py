import sys

def main():
    if len(sys.argv) < 4:
        print("Please provide Name, Roll Number, and Department as arguments.")
        return
    
    name = sys.argv[1]
    roll_no = sys.argv[2]
    dept = sys.argv[3]

    print("Name:", name)
    print("Roll No:", roll_no)
    print("Department:", dept)

if __name__ == "__main__":
    main()

