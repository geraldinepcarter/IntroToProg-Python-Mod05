# -------------------------------------------------------------------------- #
# Title: Working with JSON files
# Desc: Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
#   GCarter, 11/6/2026, Created File
# -------------------------------------------------------------------------- #
import json

# Define the data constants
FILE_NAME: str = 'MyLabData.json'

# Define the program's data
MENU: str = '''
------ Student GPAs ---------------------
Select from the following menu:
1. Show current student data.
2. Enter new student data.
3. Save data to a file.
4. Exit the program.
-----------------------------------------
'''

FILE_NAME = "MyLabData.json"
student_first_name: str = ''
student_last_name: str = ''
student_gpa: float = 0.0
message: str = ''
menu_choice: str = ''
student_data: dict = {}
students: list = []
file_data: str = ''
file = None

# When the program starts, read the file data into a list of dictionary rows
# Extract the data from the file
#file = open(FILE_NAME, 'r')
#for row in file.readlines():

    # Transform the data from the file
#   parts = row.strip().split(',')
#   student_first_name = parts[0]
#    student_last_name = parts[1]
#    student_gpa = float(parts[2])
#    student_data = {'FirstName': student_first_name,
#                    'LastName': student_last_name,
#                    'GPA': student_gpa}

    # Load it into our collection (list of lists)
#    students.append(student_data)
#file.close()
try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("--Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("--Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file is not None and file.closed == False:
        file.close()

#file.close()
#print(students)

# Repeat the following tasks
while True:
    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()

    if menu_choice == "1":
        print("-" * 50)
        for student_data in students:
            if student_data["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student_data["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student_data["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student_data["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student_data["FirstName"],
                             student_data["LastName"],
                             student_data["GPA"]))
        print("-" * 50)
        continue

    try:
        #elif menu_choice == "2":
            # Input the data
        student_first_name = input("What is the student's first name? ")
        if not student_first_name.isalpha():
            raise ValueError("The first name should not contain numbers.")

        student_last_name = input("What is the student's last name? ")
        if not student_last_name.isalpha():
            raise ValueError("The last name should not contain numbers.")

        try:
            student_gpa = float(input("What is the student's GPA? "))
        except ValueError:
            raise ValueError("The GPA should be a number.")

        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "GPA": student_gpa}
        students.append(student_data)
    except ValueError as e:
        print(e)
        print("--Technical Error Message--")
        print(e.__doc__)
        print(e.__str__())
    except Exception as e:
        print("There was a non-specific error!\n")
        print("--Technical Error Message--")
        print(e, e.__doc__, type(e), sep='\n')

    #elif menu_choice == "3":
#        file = open(FILE_NAME, 'w')
#        file.write('FirstName,LastName,GPA\n')
#        for student_data in students:
#            student_first_name = student_data['FirstName']
#            student_last_name = student_data['LastName']
#            student_gpa = float(student_data['GPA'])
#            file.write(f'{student_first_name},{student_last_name},{student_gpa}\n')
#        file.close()
#        print("Data Saved!")

    #Save the data to the file
    try:
        file = open(FILE_NAME, 'w')
        json.dump(students, file)
    except TypeError as e:
        print("Please check that the data is a valid JSON format\n")
        print("--Technical Error Message--")
        print(e, e.__doc__, type(e), sep='\n')
    except Exception as e:
        print("--Technical Error Message--")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
    finally:
        if file is not None and file.closed == False:
            file.close()
        #continue

    #elif menu_choice == "4":
        #break

#else:
#    print("Please choose a valid menu choice.")
#print("Program ended. Have a nice day!")
