students = []
courses = []
marks = {}
def add_students():
    n = int(input("enter the students number:"))
    for i in range(n):
        print("student", i + 1)
        student_id = input("ID: ")
        name = input("name: ")
        dob = input("date of birth: ")
        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }
        students.append(student)
def add_courses():
    n = int(input("number of courses: "))
    for i in range(n):
        print("courses", i + 1)
        course_id = input("ID course: ")
        name = input("name course: ")
        course = {
            "id": course_id,
            "name": name
        }
        courses.append(course)
def show_students():
    print("List of the student")
    for student in student:
        print(
            student["id"],
            "-",
            student["name"],
            "-",
            student["dob"],
        )
def show_courses():
    print("List of courses")
    for course in course:
        print(
            course["id"],
            "-",
            course["name"]
        )
def add_marks():
    course_id = input("Enter id of course: ")
    marks[course_id] = {}
    for student in student:
        score = float(
            input("enter the mark" + student["name"] + ": ")
        )
        marks[course_id][student["id"]] = score
def show_marks():
    course_id = input("Enter ID of course: ")
    if course_id not in marks:
        print("not the mark")
        return
    print("Score")
    for student_id in marks[course_id]:
        score = marks[course_id][student_id]
        print(student_id, "-", score)
def main():
    while True:
        print("\n     Title     ")
        print("1. Enter students")
        print("2. Enter the courses")
        print("3. Enter the mark")
        print("4. Show student")
        print("5. Show courses")
        print("6. Show mark")
        print("7. Exit")
        choice = input("chosse: ")
        if choice == "1":
            add_students()
        elif choice == "2":
            add_courses()
        elif choice == "3":
            add_marks()
        elif choice == "4":
            show_courses()
        elif choice == "5":
            show_students()
        elif choice == "6":
            show_marks()
        elif choice == "7":
            print("Exit")
            break
        else:
            print("Page not found")
main()