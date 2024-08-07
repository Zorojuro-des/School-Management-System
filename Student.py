if Login_1 == 1:
    while i <= 3:
        Pass_1 = input("Enter the password:")  # Student password
        if Pass_1 == "Avv123":
            print("Logged in as Student.")  # student Loop start here
            while True:
                Task_1 = int(input(
                    "Tasks:\n 1.View Data \n 2.Extract Data \n 3.Print Report Card \n 4.Log out \n Enter the Number:"))  # 1.View own (or) topper 2.Extract 3.Report Card 4.Exit
                if Task_1 == 1:  # View Data
                    print()
                elif Task_1 == 2:  # Extract Data
                    print()
                elif Task_1 == 3:  # Print Report Card
                    Gr_no = int(input("1.Enter Gr.no."))
                    # section = input("Enter section:")

                    space0 = " " * (42 - len(Dict_Data[Gr_no][11]) - len(Class[3:]))
                    space1 = " " * (30 - len(Dict_Data[Gr_no][0]))
                    space2 = " " * (31 - len(Dict_Data[Gr_no][1]))
                    space3 = " " * (31 - len(Dict_Data[Gr_no][2]))

                    print(" " * 20, "Anand Vidya Vihar School")
                    print(" " * 23, "Harinagar, Vadodara")
                    print(" " * 26, "Report Card")

                    print("Class:", Dict_Data[Gr_no][3], Class[3:], space0, "Admission Date")
                    print("Student Name:", Dict_Data[Gr_no][0], space1, "Date of Birth:", Dict_Data[Gr_no][5])
                    print("Father Name:", Dict_Data[Gr_no][1], space2, "Roll No:", Dict_Data[Gr_no][4])
                    print("Mother Name:", Dict_Data[Gr_no][2], space3, "Gr No:", Gr_no)
                    print()

                    print("Subject Marks(out of 30):")
                    print("English:", Dict_Data[Gr_no][6])
                    print("Physics:", Dict_Data[Gr_no][7])
                    print("Maths:", Dict_Data[Gr_no][8])
                    print("Chemistry:", Dict_Data[Gr_no][9])
                    print("Computer Science:", Dict_Data[Gr_no][10])
                    print()
                    print("Average marks:", (
                                Dict_Data[Gr_no][6] + Dict_Data[Gr_no][7] + Dict_Data[Gr_no][8] + Dict_Data[Gr_no][9] +
                                Dict_Data[Gr_no][10]) / 5)
                elif Task_1 == 4:  # Log out
                    print("You are successfully logged out")
                    break
                else:
                    print("Give a valid input")
        # break for correct password has to be typed
        else:
            print("Password Incorrect")
            i += 1