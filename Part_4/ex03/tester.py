from new_student import Student

# Test case 1: Standard creation
student = Student(name="Edward", surname="agle")
print(student)

# Test case 2: Trying to pass an ID (should raise an error)
try:
    student = Student(name="Edward", surname="agle", id="toto")
except TypeError as e:
    print(e)
