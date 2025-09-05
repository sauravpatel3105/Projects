import os
from datetime import datetime

class Journal:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self, content):

        try:

            with open(self.filename, "a", encoding="utf-8") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}]\n{content}\n\n")
            print("Entry added successfully.")
        
        except PermissionError:
            print("Permission denied: Unable to write to the file.")

    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                entries = file.read()
                if entries.strip():
                    print("Journal Entries:")
                    print("-" * 30)
                    print(entries)
                else:
                    print("Journal is currently empty.")
        except FileNotFoundError:
            print("No journal file found. Add an entry first.")

    def search_entries(self, keyword):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                entries = file.readlines()
                found = False
                print(f" Searching for the Keyword :'{keyword}'...")
                print("-" * 30)
                for line in entries:

                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True
                        
                        print("Thank you for searching Keyword.")
                
                if not found:
                    print("No entries found with that keyword.")
                    
        except FileNotFoundError:
            print("No journal file found. Add an entry first.")

    def delete_entries(self):

        if not os.path.exists(self.filename):
            print("Journal file does not exist.")
            return
        
        confirm = input("Are you sure you want to delete all entries? (yes/no): ").lower()
        
        if confirm == "yes":

            try:
                os.remove(self.filename)
                print("All entries deleted successfully.")
            
            except PermissionError:
                print("Permission denied: Unable to delete the file.")
        
        else:
            print("Deletion cancelled.")



def main():
    journal = Journal()
    while True:
        print("")
        print("Welcome to Personl Journal Manager! ")
        print("")
        print("Please Select an Option: ")
        print("")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            content = input("Write your journal entry Text :\n")
            journal.add_entry(content)

        elif choice == "2":
            journal.view_entries()

        elif choice == "3":
            keyword = input("Enter a keyword or date to search: ")
            journal.search_entries(keyword)

        elif choice == "4":
            journal.delete_entries()

        elif choice == "5":
            print("Exiting Journal. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()
