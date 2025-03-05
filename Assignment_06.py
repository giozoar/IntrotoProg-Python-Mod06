# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Giovanna Torres, 3/4/2025, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

class IO:
    """ This class groups the inputs and output functions called in this script.

    ChangeLog: (Who, When, What)
    Giovanna Torres, 3/4/2025, Created class

    :return: None
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        Giovanna Torres, 3/4/2025, Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Giovanna Torres, 3/4/2025, Created Function

        :return:
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """This function captures the user menu choice input.
            ChangeLog: (Who, When, What)
            Giovanna Torres, 3/4/2025, Created function

            :return: None
        """
        try:
            menu_choice = input("Enter your menu choice number: ")  # note this for the next lab
            print()  # Adding extra space to make it look nicer.
            if menu_choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the registered students by course.

        ChangeLog: (Who, When, What)
        Giovanna Torres, 3/4/2025, Created function

        :return: None
        """

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-" * 50)
    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        Giovanna Torres, 3/4/2025,Created function

        :return: student_data
        """

        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Enter the course name. ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

class FileProcessor:
    """ This class groups the file and data processing functions called in this script.

    ChangeLog: (Who, When, What)
    Giovanna Torres, 3/4/2025, Created class

    :return: student_data
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """This function reads the data from an existing JSON file into a variable.
            ChangeLog: (Who, When, What)
            Giovanna Torres, 3/4/2025, Created function

            :return: student_data
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This function writes the data captured from the user into a JSON file
            ChangeLog: (Who, When, What)
            Giovanna Torres, 3/4/2025, Created function

            :return: None
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print('The following students have been registered: ')
            IO.output_student_courses(student_data)
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice=IO.input_menu_choice()
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students=IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
