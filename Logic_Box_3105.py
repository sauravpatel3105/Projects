print("")
print("Welcome to the Pattern Generator and Number Analyzer!")

def pattern_enter():
    print("")

    pattern = int (input("Enter your pattern numbeer :"))
    
    def positive(): 
        i = 1
        print("Pattern :")
        print("")
        while i <= pattern :
            j = 1
            while j <=i:
            
    
                print("*",end="")

                j += 1
            print()
            i += 1
    if 0 < pattern:
        
        print(positive())
    else:
        print("Please Enter your Positive Number and which is greater then zero(0)")


def enter():
    first_number = int (input ("enter your first number :"))
    second_number = int (input ("enter your second number :"))

    def odd_even():
        range_number = range(first_number , second_number+1)
        i = 0
        for i in list (range_number):
            if i %2 == 0:
                print(f"{i} is Even Number.")
            else:
                print(f"{i} is ODD Number.")
 
        print(f"Sum of all number frome {first_number ,second_number} = {sum(list(range_number))}")

    if first_number<= second_number:
        print(odd_even())
    else:
        print("Please check the range .the range is greater then the strat")

print("")
print("Select an option :")
print("")

print("1. Generate pattern.")
print("2. Analyze a rangen of number.")
print("3. Exit.")

print("")
number = int (input("Enter your choice option :"))

Exit = ("Exiting the program. Goodbye !" )

print("")

if number == 1 :
    print(pattern_enter())
elif number == 2:
    print(enter())
elif number == 3 :
    print(Exit)
else:
    print("not number")
