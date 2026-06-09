students = []

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        reg_no = input("Enter Register Number: ")
        DOB = input("Enter DOB: ")
        city = input("Enter City: ")
        course = input("Enter Course: ")

        student = {
            "name": name,
            "reg_no": reg_no,
            "DOB": DOB,
            "city": city,
            "course": course
        }

        students.append(student)

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found!")

        else:
            print("\n===== Students List =====")

            for student in students:

                print("\n--------------------")
                print("Name:", student["name"])
                print("Reg No:", student["reg_no"])
                print("DOB:", student["DOB"])
                print("City:", student["city"])
                print("Course:", student["course"])

    elif choice == "3":

        search_name = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["name"].lower() == search_name.lower():

                print("\nStudent Found")
                print("Name:", student["name"])
                print("Reg No:", student["reg_no"])
                print("DOB:", student["dob"])
                print("City:", student["city"])
                print("Course:", student["course"])

                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "4":

        delete_name = input("Enter Student Name to Delete: ")

        found = False

        for student in students:

            if student["name"].lower() == delete_name.lower():

                students.remove(student)
                print("Student Deleted Successfully!")

                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "5":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")
