class Employee:
    def __init__(self, employee_id=None, name=None, age=None, salary=None):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary!")

    def display(self):
        print(f"Employee ID: {self.__employee_id}, Name: {self.name}, Age: {self.age}, Salary: {self.__salary}")

    def __del__(self):
        print(f"Employee {self.name} (ID: {self.__employee_id}) has been deleted.")

    def __str__(self):
        return f"Employee[{self.__employee_id}] - {self.name}, Salary: {self.__salary}"

    def __eq__(self, other):
        return self.__salary == other.__salary

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __gt__(self, other):
        return self.__salary > other.__salary


class Manager(Employee):

    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):

    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language
        
    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


def menu():
    employees = []

    while True:
        print("\n--- Employee Management System ---")
        print("1. Create Employee")
        print("2. Create Manager")
        print("3. Create Developer")
        print("4. Show Details of All Employees")
        print("5. Compare Salaries")
        print("6. Check Subclass")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            eid = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            emp = Employee(eid, name, age, salary)
            employees.append(emp)

        elif choice == "2":
            eid = int(input("Enter Manager ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            mgr = Manager(eid, name, age, salary, dept)
            employees.append(mgr)

        elif choice == "3":
            eid = int(input("Enter Developer ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            dev = Developer(eid, name, age, salary, lang)
            employees.append(dev)

        elif choice == "4":
            for emp in employees:
                print("Display the Data : ")
                
                print("1.Employee : ")
                print("2.Manager : ")
                print("3.Developer : ")
                num = int(input ("Enter your choice :"))

                if num == 1:
                    
                    emp.display()
                    
                elif num == 2:
                    mgr.display()
                    
                    
                elif num == 3:
                    dev.display()
                else :
                    print("no number")
                print("-" * 40)

        elif choice == "5":
            if len(employees) < 2:
                print("Need at least 2 employees to compare.")
            else:
                print("Comparing first two employees...")
                if employees[0] > employees[1]:
                    print(f"{employees[0].name} has a higher salary than {employees[1].name}")
                elif employees[0] < employees[1]:
                    print(f"{employees[1].name} has a higher salary than {employees[0].name}")
                else:
                    print("Both have equal salary.")

        elif choice == "6":
            print("Is Manager a subclass of Employee?", issubclass(Manager, Employee))
            print("Is Developer a subclass of Employee?", issubclass(Developer, Employee))

        elif choice == "7":
            print("Exiting Employee Management System...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()