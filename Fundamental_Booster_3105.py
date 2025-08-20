
print("")
print("Welcome to the Interactive Personal Data Collector !")
print("")

first_name  = input("Please Enter your First Name : " )
last_name = input("Please Enter your last Name :")
age= int(input("Please Enter your Age :"))
city_name = input("Please Enter your City Name :")
collge_name = input("Please Enter your Collge Name :")
height = float(input("Please Enter your Height in Centimeter :"))
mobile_number = int(input("Please Enter your Mobile Number :"))
hobby = input("Please Enter your hobby : ")
print("")

print("Thank You! Here is the Information we Collected :")
print("")
full_name = first_name+" "+last_name
print("Full Name :",full_name,type(full_name))
print("Memory Address :",id(full_name))
 
print("")

print("Age :",age,type(age))
print("Memory Address :",id(age))
current_year = 2025
birth_year = current_year - (age)
print(f"You were born in {birth_year}.") 
print("")

print("City Name : ",city_name,type(city_name))
print("Memory Address :",id(city_name))

print("")

print("Collge Name : ",collge_name,(type(collge_name)))
print("Memory Address :",id(collge_name))

print("")

print("Height :",height,type(height))
print("Memory Address :",id(height))

print("")

print("Mobile Number :",mobile_number,type(mobile_number))
print("Memory Address :",id(mobile_number))

print("")

print("Hobby : ",hobby,type(hobby))
print("Memory Address :",id(hobby))

print("")

print("Thank You For Using the Personal Data Collector. Goodbye!")
