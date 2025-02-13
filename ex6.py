# Enrollment Class: Ties a student to a course and includes a grade
class Enrollment:
    def __init__(self, student, course):
        # Initialize the enrollment with a student and a course
        self.student = student  # The student object
        self.course = course    # The course object
        self.grade = None       # Grade is initially unset (None)

    def set_grade(self, grade):
        # Method to set the grade for this enrollment (student in a course)
        self.grade = grade  # Update the grade for the course

# Course Class: Represents a course with a code and a title
class Course:
    def __init__(self, course_code, course_title):
        # Initialize a course with a unique code and a title
        self.course_code = course_code  # Course code (e.g., "CS101")
        self.course_title = course_title  # Course title (e.g., "Intro to Computer Science")
        self.enrollments = []  # List to store enrollments (students in this course)

    def add_enrollment(self, enrollment):
        # Add an enrollment to the course (a student enrolling in this course)
        self.enrollments.append(enrollment)  # Append the new enrollment to the list

# Student Class: Represents a student with a unique ID and a list of courses they are enrolled in
class Student:
    def __init__(self, student_id, name):
        # Initialize the student with an ID and a name
        self.student_id = student_id  # Unique ID for the student (e.g., "S001")
        self.name = name  # Name of the student (e.g., "Alice")
        self.enrollments = []  # List to store the student's enrollments (courses they are in)

    def enroll_in_course(self, course):
        # Enroll the student in a given course
        enrollment = Enrollment(self, course)  # Create an Enrollment object linking the student and the course
        self.enrollments.append(enrollment)  # Add this enrollment to the student's list of enrollments
        course.add_enrollment(enrollment)  # Also add the enrollment to the course's list of enrollments

    def record_grade(self, course_code, grade):
        # Record a grade for a student in a specific course identified by the course code
        for enrollment in self.enrollments:  # Loop through all the student's enrollments
            if enrollment.course.course_code == course_code:  # Find the course by its code
                enrollment.set_grade(grade)  # Set the grade for the course
                print(f"Grade {grade} recorded for {self.name} in course {enrollment.course.course_title}.")
                return  # Exit the method once the grade is recorded
        # If the course is not found in the student's enrollments
        print(f"{self.name} is not enrolled in course with code {course_code}.")

    def calculate_gpa(self):
        # Calculate the student's GPA based on the grades in their enrollments
        total_points = 0  # Initialize the total points (for GPA calculation)
        total_courses = 0  # Count the number of courses with recorded grades
        for enrollment in self.enrollments:  # Loop through the student's enrollments
            if enrollment.grade is not None:  # If the student has a grade for the course
                total_courses += 1  # Increment the course count
                total_points += self.grade_to_points(enrollment.grade)  # Add the grade points to the total
        if total_courses == 0:
            return 0  # Avoid division by zero if no grades are recorded
        return total_points / total_courses  # Return the GPA (average of grade points)

    def grade_to_points(self, grade):
        # Convert a letter grade to GPA points
        grade_points = {
            'A': 4.0,  # A corresponds to 4 points
            'B': 3.0,  # B corresponds to 3 points
            'C': 2.0,  # C corresponds to 2 points
            'D': 1.0,  # D corresponds to 1 point
            'F': 0.0   # F corresponds to 0 points
        }
        return grade_points.get(grade.upper(), 0.0)  # Convert grade to points; defaults to 0 if invalid grade

    def display_info(self):
        # Display the student's information, including enrollments and GPA
        print(f"Student ID: {self.student_id}")  # Display the student ID
        print(f"Student Name: {self.name}")  # Display the student's name
        print("Enrollments:")  # List all courses the student is enrolled in
        for enrollment in self.enrollments:
            grade = enrollment.grade if enrollment.grade else "Not graded"  # Display grade if available
            print(f"  - {enrollment.course.course_title} (Grade: {grade})")  # Display course title and grade
        print(f"GPA: {self.calculate_gpa():.2f}")  # Display the student's GPA, rounded to 2 decimal places


# Testing the system
if __name__ == "__main__":
    # Create some courses
    course1 = Course("CS101", "Intro to Computer Science")  # Course code "CS101" and title
    course2 = Course("MATH101", "Calculus I")  # Course code "MATH101" and title
    course3 = Course("HIST101", "World History")  # Course code "HIST101" and title

    # Create some students
    student1 = Student("S001", "Alice")  # Student with ID "S001" and name "Alice"
    student2 = Student("S002", "Bob")  # Student with ID "S002" and name "Bob"

    # Enroll students in courses
    student1.enroll_in_course(course1)  # Alice enrolls in "CS101"
    student1.enroll_in_course(course2)  # Alice enrolls in "MATH101"
    student2.enroll_in_course(course2)  # Bob enrolls in "MATH101"
    student2.enroll_in_course(course3)  # Bob enrolls in "HIST101"

    # Record grades for students
    student1.record_grade("CS101", "A")  # Alice receives grade "A" in "CS101"
    student1.record_grade("MATH101", "B")  # Alice receives grade "B" in "MATH101"
    student2.record_grade("MATH101", "A")  # Bob receives grade "A" in "MATH101"
    student2.record_grade("HIST101", "C")  # Bob receives grade "C" in "HIST101"

    # Display student information and GPA
    student1.display_info()  # Display Alice's info and GPA
    student2.display_info()  # Display Bob's info and GPA
