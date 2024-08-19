# Define the Student class
class Student:
    def __init__(self, name, student_id):
        # Initialize the student with name, student ID, and an empty list of grades
        self._name = name               # Protected attribute for the student's name
        self._student_id = student_id   # Protected attribute for the student's ID
        self._grades = []               # Protected attribute for the student's grades

    def add_grade(self, grade):
        # Add a grade to the student's record
        self._grades.append(grade)

    def calculate_average(self):
        # Calculate and return the average of the student's grades
        if self._grades:
            return sum(self._grades) / len(self._grades)
        return 0  # Return 0 if the student has no grades

    def get_info(self):
        # Return a formatted string with the student's information
        average_grade = self.calculate_average()
        return f"Student ID: {self._student_id}, Name: {self._name}, Average Grade: {average_grade:.2f}"

# Define the Classroom class
class Classroom:
    def __init__(self):
        # Initialize the classroom with an empty list of students
        self._students = []  # Protected attribute for storing the list of students

    def add_student(self, student):
        # Add a student to the classroom
        self._students.append(student)

    def remove_student(self, student_id):
        # Remove a student from the classroom by their ID
        self._students = [student for student in self._students if student._student_id != student_id]

    def find_student(self, student_id):
        # Find a student by their ID and return their information
        for student in self._students:
            if student._student_id == student_id:
                return student.get_info()
        return "Student not found."

    def list_students(self):
        # Return a list of information about all students in the classroom
        return [student.get_info() for student in self._students]

# Example usage
if __name__ == "__main__":
    # Create instances of Student
    student1 = Student("Alice", 101)
    student2 = Student("Bob", 102)
    student3 = Student("Charlie", 103)
    
    # Add grades to students
    student1.add_grade(85)
    student1.add_grade(90)
    student2.add_grade(78)
    student2.add_grade(82)
    student3.add_grade(95)
    student3.add_grade(88)
    
    # Create a Classroom instance and add students to it
    my_classroom = Classroom()
    my_classroom.add_student(student1)
    my_classroom.add_student(student2)
    my_classroom.add_student(student3)
    
    # Find and list students
    print(my_classroom.find_student(101))  # Find the student with ID 101 and print their information
    print(my_classroom.list_students())    # Print the information of all students in the classroom
    
    # Remove a student and list students again
    my_classroom.remove_student(102)       # Remove the student with ID 102 from the classroom
    print(my_classroom.list_students())    # Print the updated list of students in the classroom
