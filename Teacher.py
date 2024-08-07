elif Login_1 == 2:
while i <= 3:
    Pass_2 = input("Enter the password")
    if Pass_2 == "ssc2019":
        print("Logged in as Teacher.")  # Teacher Loop start here
        while True:
            Task_2 = int(input(
                "Tasks:\n 1.Add data \n 2.Extract data \n 3.View data \n 4.Calculate data \n 5.Modify Data \n 6.Print Report Card \n 7.Log out"))  # 1.Add 2. Extract 3.View 4.Calculate 5.Modify 6. Print report card 7.Exit
            if Task_2 == 1:  # Add Data
                while True:
                    while True:
                        Gr_no = int(input("Enter Gr.no."))
                        if len(str(Gr_no)) == 4:
                            break
                        else:
                            print("Error: Enter a 4-Digit Gr. No.")
                            continue
                    name = (input("Enter the name")).capitalize()
                    F_name = (input("Enter Father's name")).capitalize()
                    M_name = (input("Enter Mother's name")).capitalize()
                    while True:
                        Class = input("Enter Class with section(Format=00-X)")
                        if int(Class[:1]) <= 12 and len(Class[3:]) == 1 and Class[2] == '-':
                            break
                        else:
                            print("Error: Enter a Class Between 1 to 12")
                            continue
                    while True:
                        Roll_No = int(input("Enter Roll No. "))
                        if Roll_No <= 40:
                            break
                        else:
                            print("Error: Enter a valid Roll No. ")
                            continue
                    while True:
                        DoB = input("Enter Date of Birth(dd/mm/yy)")
                        if 1 <= int(DoB[:2]) <= 31 and 1 <= int(DoB[3:5]) <= 12 and 00 <= int(DoB[6:]) <= 22:
                            break
                        else:
                            print("Error: Enter a valid Date of Birth")
                            continue
                    while True:
                        M_Eng = int(input("Enter Marks in English "))
                        if 0 <= M_Eng <= 30:
                            break
                        else:
                            print("Error: Enter Marks Out of 30")
                            continue
                    while True:
                        M_Phy = int(input("Enter Marks in Physics "))
                        if 0 <= M_Phy <= 30:
                            break
                        else:
                            print("Error: Enter Marks Out of 30")
                            continue
                    while True:
                        M_Math = int(input("Enter Marks in Maths "))
                        if 0 <= M_Math <= 30:
                            break
                        else:
                            print("Error: Enter Marks Out of 30")
                            continue
                    while True:
                        M_Chem = int(input("Enter Marks in Chemistry "))
                        if 0 <= M_Chem <= 30:
                            break
                        else:
                            print("Error: Enter Marks Out of 30")
                            continue
                    while True:
                        M_CS = int(input("Enter Marks in Computer Science "))
                        if 0 <= M_CS <= 30:
                            break
                        else:
                            print("Error: Enter Marks Out of 30")
                            continue
                    while True:
                        Adm_Date = input("Enter Admission date(dd/mm/yy)")
                        if 1 <= int(Adm_Date[:2]) <= 31 and 1 <= int(Adm_Date[3:5]) <= 12 and 00 <= int(
                                Adm_Date[6:]) <= 22 and int(
                            Adm_Date[6:]) >= int(DoB[6:]):
                            break
                        else:
                            print("Error: Enter a valid Admission date")
                            continue
                    Dict_list = [name, F_name, M_name, Class, Roll_No, DoB, M_Eng, M_Phy, M_Math, M_Chem, M_CS,
                                 Adm_Date]
                    Dict_Data[Gr_no] = Dict_list
                    a = 0
                    while True:
                        End = input("Do you want to keep adding?(y/n)")
                        if End == 'N' or End == 'n':
                            a += 1
                            break
                        elif End == 'Y' or End == 'y':
                            break
                        else:
                            print("Print valid input")
                    if a == 1:
                        break
            elif Task_2 == 2:  # Extract Data
                print()
            elif Task_2 == 3:  # View Data
                print()
            elif Task_2 == 4:  # Calculate Data
                print()
            elif Task_2 == 5:  # Modify Data
                print()
            elif Task_2 == 6:  # Print Report Data
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
            elif Task_2 == 7:  # Logged out
                print("You are successfully logged out")
                break
            else:
                print("Give a valid input")
    # break for correct password has to be typed
    else:
        print("Password Incorrect")
        i += 1