import datetime
import threading
import time
import grade


# Q1. Create Student class with constructor
class Student:

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = 0

    # Q3. Getter and Setter

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Invalid Marks! Enter between 0 and 100")

        self.__marks = marks

    def get_marks(self):
        return self.__marks

    # Q4. Calculate Grade using method

    def calculate_grade(self):
        return grade.calculate_grade(self.__marks)

    # Q2. Display student details

    def display(self):
        print("\n--- Student Details ---")
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.get_marks())
        print("Grade:", self.calculate_grade())


# Q8. Thread for report generation

def generate_report():
    print("\nGenerating Student Report...")
    time.sleep(2)
    print("Report Generated Successfully!")


# Main Program

try:

    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")

    # Create object
    s1 = Student(roll_no, name)

    marks = float(input("Enter Marks: "))

    # Set marks
    s1.set_marks(marks)

    # Q6. Store admission date
    admission_date = datetime.datetime.now()

    print("Admission Date:", admission_date.strftime("%d-%m-%Y"))

    # Display details
    s1.display()

    # Q8. Create and run thread
    t1 = threading.Thread(target=generate_report)

    t1.start()
    t1.join()

except ValueError as e:
    print("Error:", e)