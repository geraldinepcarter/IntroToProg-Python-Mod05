# -------------------------------------------------------------------------- #
# Title: Assignment05
# Desc: Using dictionaries, files, and exception handling.
# Change Log: (Who, When, What)
# GCarter, 11/11/2026, Created Script
# -------------------------------------------------------------------------- #

import json

# Define the Data Constants
MENU: str = '''
----- Course Registration Program -----
Select from the following menu:
1. Register a student for a course.
2. Show current data.
3. Save data to a file.
4. Exit the program.
---------------------------------------
'''
FILE_NAME: str = 'Enrollments.json'

#Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict = {}
students: list = []
file = None
menu_choice: str = ''

# When the program starts, read the file data into a list of dictionary rows
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script.\n")
    print("---Technical Error Message---")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("---Technical Error Message---")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    # Check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()

# Present menu and process the data
while True:
    print(MENU)
    menu_choice = input("What would you like to do? ")
    print()

    # input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {'FirstName': student_first_name,
                        'LastName': student_last_name,
                        'CourseName': course_name}
            # Load it into our collection (list of lists)
            students.append(student_data)
            print(f"You have registered for {student_first_name} "
                  f"{student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)
            print("---Technical Error Message---")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("---Technical Error Message---")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # show current data
    elif menu_choice == "2":
        print("-"*50)
        for student_data in students:
            print(f"Student {student_data['FirstName']} {student_data['LastName']} is "
                  f"enrolled in {student_data['CourseName']}.")
        print("-"*50)
        continue

    # save the data to the file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            file.close()
            print("The data has been saved in", FILE_NAME)
        except TypeError as e:
            print("Please check that the data is a valid JSON format.\n")
            print("---Technical Error Message---")
            print(e.__doc__, type(e), e.__str__(), sep='\n')
        except Exception as e:
            print("---Technical Error Message---")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and file.closed == False:
                file.close()
        continue

    # stop the loop
    elif menu_choice == "4":
        break

    else:
        print("Please only choose option 1, 2, 3 or 4")

print("Program ended. Have a nice day!")


