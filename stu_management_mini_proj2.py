Students = []
while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")

    choice = input("Enter choice:")

    if choice == "1":
        name = input("Enter student Name:")
        Students.append(name)
        print(Students)

    elif choice == "2":
        print("Students:")
        for student in Students:
            print(student)

    elif choice == "3":
        break

    else:
        print("Invalid Number!!!")
