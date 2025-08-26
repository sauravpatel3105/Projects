# Global dataset and summary
data = []
data_type = "1D"  # Can be "1D" or "2D"
dataset_summary = {}

# --- User-defined Functions ---

def display_doc():
    """Displays the documentation of all functions."""
    print("\nFunction Documentation:")
    for func in [input_data, display_summary, factorial, filter_data, sort_data, get_statistics, display_data, fibonacci]:
        print(f"{func.__name__} - {func.__doc__}")

def input_data():
    """Allows the user to input 1D or 2D data manually."""
    global data, data_type
    print("\nStep 1: Input Data")
    choice = input("Choose:\n1. 1D Array\n2. 2D Array\nEnter your choice: ")
    if choice == "1":
        data_type = "1D"
        raw = input("Enter values separated by spaces: ")
        data = list(map(int, raw.split()))
    elif choice == "2":
        data_type = "2D"
        rows = int(input("Enter number of rows: "))
        data = []
        for i in range(rows):
            row = list(map(int, input(f"Enter row {i+1} values separated by spaces: ").split()))
            data.append(row)
    else:
        print("Invalid choice.")
    print("Data has been stored successfully!")

def display_data():
    """Displays the current dataset."""
    global data, data_type
    print("\nCurrent Data:")
    if data_type == "1D":
        print(data)
    else:
        for row in data:
            print("\t".join(map(str, row)))

def display_summary():
    """Uses built-in functions to display statistics."""
    global data, dataset_summary
    print("\nData Summary (Built-in Functions):")
    if not data:
        print("No data found.")
        return

    flat_data = data if data_type == "1D" else [item for sublist in data for item in sublist]

    total = len(flat_data)
    minimum = min(flat_data)
    maximum = max(flat_data)
    total_sum = sum(flat_data)
    avg = total_sum / total if total else 0

    dataset_summary = {
        "Total elements": total,
        "Minimum value": minimum,
        "Maximum value": maximum,
        "Sum": total_sum,
        "Average": round(avg, 2)
    }

    for key, value in dataset_summary.items():
        print(f"- {key}: {value}")

def factorial(n):
    """Recursively calculates factorial of a number."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Recursively calculates Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibs = fibonacci(n - 1)
        fibs.append(fibs[-1] + fibs[-2])
        return fibs

def filter_data():
    """Filters data based on user-defined threshold using lambda and filter."""
    if not data:
        print("No data available.")
        return
    flat_data = data if data_type == "1D" else [item for sublist in data for item in sublist]

    threshold = int(input("Enter a threshold value: "))
    filtered = list(filter(lambda x: x >= threshold, flat_data))
    print(f"Filtered Data (values >= {threshold}):")
    print(filtered)

def sort_data():
    """Sorts data using sort() for 1D and sorted() for 2D."""
    global data
    if not data:
        print("No data available.")
        return
    print("\nChoose sorting option:\n1. Ascending\n2. Descending")
    order = input("Enter your choice: ")
    reverse = True if order == "2" else False

    if data_type == "1D":
        data.sort(reverse=reverse)
        print(f"Sorted Data ({'Descending' if reverse else 'Ascending'}):\n{data}")
    else:
        sorted_rows = sorted(data, key=lambda row: sum(row), reverse=reverse)
        print(f"2D Data Sorted by Row Sum ({'Descending' if reverse else 'Ascending'}):")
        for row in sorted_rows:
            print("\t".join(map(str, row)))

def get_statistics():
    """Returns multiple values: min, max, sum, and average."""
    if not data:
        print("No data to analyze.")
        return
    flat_data = data if data_type == "1D" else [item for sublist in data for item in sublist]
    minimum = min(flat_data)
    maximum = max(flat_data)
    total_sum = sum(flat_data)
    avg = total_sum / len(flat_data)
    return minimum, maximum, total_sum, round(avg, 2)

def args_demo(*args):
    """Demonstrates usage of *args by printing values."""
    print("Values passed using *args:")
    for value in args:
        print(value)

def kwargs_demo(**kwargs):
    """Demonstrates usage of **kwargs to print key-value dataset summary."""
    print("Dataset Summary using **kwargs:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# --- Main Menu Interface ---

def main():
    while True:
        print("\n" + "="*50)
        print("Welcome to the Data Analyzer and Transformer Program")
        print("="*50)
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Fibonacci Series (Recursion)")
        print("8. *args Demo")
        print("9. **kwargs Demo")
        print("10. View All Function Docs")
        print("11. Display Current Data")
        print("12. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == "1":
            input_data()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            num = int(input("Enter a number to calculate its factorial: "))
            print(f"Factorial of {num} is: {factorial(num)}")
        elif choice == "4":
            filter_data()
        elif choice == "5":
            sort_data()
        elif choice == "6":
            stats = get_statistics()
            if stats:
                print("Dataset Statistics:")
                print(f"- Minimum: {stats[0]}")
                print(f"- Maximum: {stats[1]}")
                print(f"- Sum: {stats[2]}")
                print(f"- Average: {stats[3]}")
        elif choice == "7":
            n = int(input("Enter number of Fibonacci terms: "))
            print(f"Fibonacci Sequence ({n} terms): {fibonacci(n)}")
        elif choice == "8":
            args_demo(10, 20, 30, "text", [1, 2, 3])
        elif choice == "9":
            if dataset_summary:
                kwargs_demo(**dataset_summary)
            else:
                print("No dataset summary available. Please run option 2 first.")
        elif choice == "10":
            display_doc()
        elif choice == "11":
            display_data()
        elif choice == "12":
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
