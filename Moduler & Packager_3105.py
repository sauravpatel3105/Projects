# Moduler & Packager 

from datetime import datetime, timedelta
import time

def datetime_menu():
    print("\n--- Datetime and Time Operations ---")
    print("1. Show Current Date and Time")
    print("2. Calculate Difference Between Two Dates")
    print("3. Format Date using strftime")
    print("4. Stopwatch")
    print("5. Countdown Timer")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Current Date and Time:", datetime.now())
    elif choice == '2':
        d1 = input("Enter first date (YYYY-MM-DD): ")
        d2 = input("Enter second date (YYYY-MM-DD): ")
        date1 = datetime.strptime(d1, '%Y-%m-%d')
        date2 = datetime.strptime(d2, '%Y-%m-%d')
        print("Difference:", abs(date2 - date1))
    elif choice == '3':
        now = datetime.now()
        print("Formatted Date:", now.strftime("%A, %d %B %Y %I:%M:%S %p"))
    elif choice == '4':
        input("Press Enter to start stopwatch...")
        start = time.time()
        input("Press Enter to stop...")
        end = time.time()
        print(f"Elapsed time: {end - start:.2f} seconds")
    elif choice == '5':
        sec = int(input("Enter countdown time in seconds: "))
        while sec:
            print(f"Time left: {sec} seconds", end='\r')
            time.sleep(1)
            sec -= 1
        print("Time's up!")
    else:
        print("Invalid option.")
import math

def math_menu():
    print("\n--- Mathematical Operations ---")
    print("1. Basic Arithmetic")
    print("2. Trigonometry (sin, cos, tan)")
    print("3. Factorial")
    print("4. Logarithm")
    print("5. Compound Interest Calculator")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Add: {a + b}, Sub: {a - b}, Mul: {a * b}, Div: {a / b}")
    elif choice == '2':
        angle = float(input("Enter angle in degrees: "))
        rad = math.radians(angle)
        print(f"sin: {math.sin(rad)}, cos: {math.cos(rad)}, tan: {math.tan(rad)}")
    elif choice == '3':
        num = int(input("Enter a number: "))
        print(f"Factorial: {math.factorial(num)}")
    elif choice == '4':
        num = float(input("Enter a number: "))
        base = float(input("Enter base (default is e): ") or math.e)
        print(f"Log: {math.log(num, base)}")
    elif choice == '5':
        p = float(input("Principal: "))
        r = float(input("Rate (%): "))
        t = float(input("Time (years): "))
        n = float(input("Compounded per year: "))
        amount = p * (1 + r / (100 * n))**(n * t)
        print(f"Compound Interest Amount: {amount:.2f}")
    else:
        print("Invalid option.")


import random
import string

def random_menu():
    print("\n--- Random Data Generation ---")
    print("1. Generate Random Number")
    print("2. Random Password")
    print("3. Random Sample from List")
    print("4. Generate OTP")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Random number (1-100):", random.randint(1, 100))
    elif choice == '2':
        length = int(input("Enter password length: "))
        chars = string.ascii_letters + string.digits + string.punctuation
        print("Password:", ''.join(random.choices(chars, k=length)))
    elif choice == '3':
        data = input("Enter comma-separated values: ").split(',')
        sample = random.sample(data, k=min(3, len(data)))
        print("Sample:", sample)
    elif choice == '4':
        print("OTP:", ''.join(random.choices(string.digits, k=6)))
    else:
        print("Invalid option.")


import uuid

def uuid_menu():
    print("\n--- UUID Generation ---")
    print("1. Generate UUID4")
    print("2. Generate Multiple UUIDs")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("UUID4:", uuid.uuid4())
    elif choice == '2':
        count = int(input("How many UUIDs? "))
        for _ in range(count):
            print(uuid.uuid4())
    else:
        print("Invalid option.")


def file_menu():
    print("\n--- File Operations ---")
    print("1. Write to File")
    print("2. Read from File")
    print("3. Append to File")
    
    choice = input("Enter your choice: ")
    filename = input("Enter filename (with extension): ")

    if choice == '1':
        content = input("Enter content to write: ")
        with open(filename, 'w') as f:
            f.write(content)
        print("Written successfully.")
    elif choice == '2':
        with open(filename, 'r') as f:
            print("File Content:\n", f.read())
    elif choice == '3':
        content = input("Enter content to append: ")
        with open(filename, 'a') as f:
            f.write(content + "\n")
        print("Appended successfully.")
    else:
        print("Invalid option.")


def explore_modules():
    print("\n--- Module Explorer ---")
    mod_name = input("Enter module name to explore (e.g., math, datetime): ")
    try:
        mod = __import__(mod_name)
        print(f"Attributes in {mod_name}:\n", dir(mod))
    except ModuleNotFoundError:
        print("Module not found.")



def main():
    while True:
        print("\n--- Multi-Utility Toolkit ---")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            datetime_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            uuid_menu()
        elif choice == '5':
            file_menu()
        elif choice == '6':
            explore_modules()
        elif choice == '7':
            print("Exit the project.")
            print("Thank you for Visiting My project. GOODBYE!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
