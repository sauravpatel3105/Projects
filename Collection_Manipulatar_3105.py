# project :- collection Manipulatar 


# Student Data organizer 
students = []

def add_student():
    print("\n Please Enter your student details :")
    student_id = int (input("student ID : "))
    name = input("student Name : ")
    age = int (input("Age : "))
    grade = input("Grade : ")
    dob = input("Date of Birth (DD-MM-YYYY)) : ")
    subjects = input("Subjects (comm-separated):")
    mobile_number = int(input("Mobile Number : "))
    address = input("Address : ")

    # create student record
    student = {
        'id': student_id,
        'name': name,
        'age': age,
        'grade': grade,
        'dob': dob,
        'subjects': [subjects],
        'mobile number': mobile_number,
        'address' : address,

    }
    students.append(student)
    print ("\n Student added Successfully! ")

def display_students():
    print ("\n    DISPLAY ALL STUDENTS    ")
    for student in students:
        print(" " .join(f"{key}:{value}" for key,value in student . items()) )


def update_students():
    student_id = int (input ( "Enter Student ID to update : "))
    for student in students:
        if student['id'] == student_id:
            print ("\n Current information : ")
            print(f"1. Name: {student['name']}")
            print(f"2. Age: {student['age']} ")
            print(f"3. Grade : {student ['grade']}")
            print (f"4. Subjects : {student['subjects']}")

            choice = input("\n What would you like to update ? (1 to 4 ) : ")
            if choice == '1':
                student['name'] = input("Enter your new Name : ")
            elif choice == '2':
                student['age'] = int(input("Enter your new age : "))
            elif choice == '3':
                student['grade'] = input("Enter your new grade : ")
            elif choice == '4':
                student['subjects'] = input ("Enter new subjects (comma-separated):").split(',')
            else:
                print("Invalid choice!")
                return
            
            print ("\n Student information update succrssfully! ")
            return
    print("\n student not found!")


def delete_student():
    student_id = int (input("Enter student ID to Delete : "))
    for i , student in enumerate(students):
        if student ['id'] == student_id:
            del students[i] # using del keyword
            print("\n deleted successfully!")
            return
    print ("\n student not found. ")


def display_subjects():
    subjects = set()
    for student in students:
        for subjects in student['subjects']:
            print ("\n    Subjects offered   ")
    print(subjects)

def main ():
    print (" Welcome to the student Data organizer! \n ")

    while True:
        print ("\n Select an Option :- ")
        print ("1. Add Student ")
        print ("2. Display All students ")
        print ("3. Update student Information ")
        print ("4. Delete student ")
        print ("5. Display subjects offered ")
        print ("6. Exit ")

        choice = input("\n Enter your choice :- ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            update_students()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_subjects()
        elif choice == '6':
            print("\n Thank you for using the Student Data Organizer ")
            break
        else:
            print("\n Invalid choice Please try again. ")

main()