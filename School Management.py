# Dict_Data ={Gr no.:[Name(0),F.Name(1),M.Name(2),Class(3),Roll No.(4),DoB(5),M-Eng(6),M-Phy(7),M-Math(8),M-Chem(9),M-CS(10),Admission date(11)}
Dict_Data ={1: ['dummy_1', 'father 1', 'mother 1', '11 A', 1, '1/1/2005', 30, 29, 29, 28, 27, '1/4/2011'],
            2: ['dummy_2', 'father 2', 'mother 2', '11 A', 2, '2/2/2005', 22, 25, 28, 30, 30, '1/4/2011'],
            3: ['dummy_3', 'father 3', 'mother 3', '11 A', 3, '3/3/2004', 24, 26, 28, 22, 30, '1/4/2011'],
            4: ['dummy_4', 'father 4', 'mother 4', '11 B', 4, '4/4/2005', 30, 29, 29, 28, 27, '1/4/2011'],
            5: ['dummy_5', 'father 5', 'mother 5', '11 B', 5, '5/5/2004', 21, 27, 30, 20, 30, '1/4/2011'],
            6: ['dummy_6', 'father 6', 'mother 6', '10 A', 6, '6/6/2005', 29, 30, 30, 27, 28, '1/4/2012'],
            7: ['dummy_7', 'father 7', 'mother 7', '10 A', 7, '7/7/2006', 30, 29, 29, 28, 27, '1/4/2012'],
            8: ['dummy_8', 'father 8', 'mother 8', '10 B', 8, '8/8/2005', 22, 29, 26, 28, 27, '1/4/2012'],
            9: ['dummy_9', 'father 9', 'mother 9', '10 B', 9, '9/9/2006', 30, 29, 29, 28, 27, '1/4/2012'],
            10:['dummy_10', 'father 10', 'mother 10', '10 B', 10, '10/10/2005', 30, 29, 22, 26, 27, '1/4/2012'],
            11:['dummy_11', 'father 11', 'mother 11', '9 A', 11, '11/11/2007', 26, 29, 26, 28, 27, '1/4/2013'],
            12:['dummy_12', 'father 12', 'mother 12', '9 A', 12, '12/12/2007', 30, 29, 25, 22, 26, '1/4/2013'],
            13:['dummy_13', 'father 13', 'mother 13', '9 A', 13, '13/1/2006', 26, 25, 29, 28, 27, '1/4/2013'],
            14:['dummy_14', 'father 14', 'mother 14', '9 B', 14, '14/2/2007', 25, 29, 29, 28, 22, '1/4/2013'],
            15:['dummy_15', 'father 15', 'mother 15', '9 B', 15, '15/3/2006', 30, 26, 29, 28, 27, '1/4/2013']}
print("Welcome to the School Management Program. \nYou have to enter the task number for the task you want to execute(This rule applies in the whole program).")# Q_1:Login Question
print("Hope you enjoy using the program")
while True:
    Login_1 = int(input("1. To login as Teacher \n2. To login as Student\n3. Exit \nEnter Number:"))
    i=1
    if Login_1==1:
        while i <= 3:
            Pass_2 = input("Enter the password")
            if Pass_2 == "ssc2019":
                print("Logged in as Teacher.")  # Teacher Loop start here
                while True:
                    Task_2 = int(input("Tasks:\n 1.Add data \n 2.Extract data \n 3.View data \n 4.Calculate data \n 5.Modify Data \n 6.Print Report Card \n 7.Log out\nEnter the number:"))  # 1.Add 2. Extract 3.View 4.Calculate 5.Modify 6. Print report card 7.Exit
                    if Task_2 == 1:  # Add Data
                        while True:
                            Gr_no = int(input("Enter Gr.no."))
                            name = (input("Enter the name")).capitalize()
                            F_name = (input("Enter Father's name")).capitalize()
                            M_name = (input("Enter Mother's name")).capitalize()
                            while True:
                                Class= input("Enter Class with section(Format=00-X)")
                                if int(Class[:1]) <= 12 and len(Class[3:]) == 1 and Class[2] == '-':
                                    break
                                else:
                                    print("Enter a Class Between 1 to 12")
                                    continue
                            Roll_No = int(input("Enter Roll No. "))
                            while True:
                                DoB = input("Enter Date of Birth(dd/mm/yy)")
                                if 1 <= int(DoB[:2]) <= 31 and 1 <= int(DoB[3:5]) <= 12 and 00 <= int(DoB[6:]) <= 22:
                                    break
                                else:
                                    print("Enter a valid Date of Birth")
                                    continue
                            while True:
                                M_Eng = int(input("Enter Marks in English "))
                                if 0 <= M_Eng <= 30:
                                    break
                                else:
                                    print("Enter Marks Out of 30")
                                    continue
                            while True:
                                M_Phy = int(input("Enter Marks in Physics "))
                                if 0 <= M_Phy <= 30:
                                    break
                                else:
                                    print("Enter Marks Out of 30")
                                    continue
                            while True:
                                M_Math = int(input("Enter Marks in Maths "))
                                if 0 <= M_Math <= 30:
                                    break
                                else:
                                    print("Enter Marks Out of 30")
                                    continue
                            while True:
                                M_Chem = int(input("Enter Marks in Chemistry "))
                                if 0 <= M_Chem <= 30:
                                    break
                                else:
                                    print("Enter Marks Out of 30")
                                    continue
                            while True:
                                M_CS = int(input("Enter Marks in Computer Science "))
                                if 0 <= M_CS <= 30:
                                    break
                                else:
                                    print("Enter Marks Out of 30")
                                    continue
                            while True:
                                Adm_Date = input("Enter Admission date(dd/mm/yy)")
                                if 1 <= int(Adm_Date[:2]) <= 31 and 1 <= int(Adm_Date[3:5]) <= 12 and 00 <= int(
                                        Adm_Date[6:]) <= 22 and int(
                                    Adm_Date[6:]) >= int(DoB[6:]):
                                    break
                                else:
                                    print("Enter a valid Admission date")
                                    continue
                            Dict_list = [name, F_name, M_name, Class, Roll_No, DoB, M_Eng, M_Phy, M_Math, M_Chem, M_CS,Adm_Date]
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
                            Gr_no = int(input("1.Enter Gr.no."))
                            print("Name of student:", Dict_Data[Gr_no][0])
                            print("Date of Birth:", Dict_Data[Gr_no][5])
                            print("Admission Date:", Dict_Data[Gr_no][11])
                            print("Roll No.:", Dict_Data[Gr_no][4])
                            print("Marks of English", Dict_Data[Gr_no][6])
                            print("Marks of Physics", Dict_Data[Gr_no][7])
                            print("Marks of Mathematics", Dict_Data[Gr_no][8])
                            print("Marks of Chemistry", Dict_Data[Gr_no][9])
                            print("Marks of Computer Science", Dict_Data[Gr_no][10])
                    elif Task_2 == 3:  # View Data
                        Task_4 = int(input("Tasks: \n 1.Details of student \n 2.Topper's list \n Enter the number:"))
                        if Task_4 == 1:
                            Gr_no = int(input("1.Enter Gr.no."))
                            print("Name of student:", Dict_Data[Gr_no][0])
                            print("Date of Birth:", Dict_Data[Gr_no][5])
                            print("Admission Date:", Dict_Data[Gr_no][11])
                            print("Roll No.:", Dict_Data[Gr_no][4])
                            print("Marks of English", Dict_Data[Gr_no][6])
                            print("Marks of Physics", Dict_Data[Gr_no][7])
                            print("Marks of Mathematics", Dict_Data[Gr_no][8])
                            print("Marks of Chemistry", Dict_Data[Gr_no][9])
                            print("Marks of Computer Science", Dict_Data[Gr_no][10])
                        elif Task_4 == 2:
                            Topper = int(input("Topper: \n1.Class Topper \n2.School Topper \n3.Subject Topper \nEnter the number:"))
                            Max_1 = 0
                            L1 = []
                            L_Eng = []
                            L_Mat = []
                            L_Chem = []
                            L_Phy = []
                            L_CS = []
                            if Topper == 1:
                                Task_5 = int(input("Enter the class:"))
                                for i in Dict_Data:
                                    if int(Dict_Data[i][3][0:2]) == Task_5:
                                        Sum_1 = Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
                                        if Sum_1 >= Max_1:
                                            Max_1 = Sum_1
                                for i in Dict_Data:
                                    if int(Dict_Data[i][3][0:2]) == Task_5:
                                        Sum_2 = Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
                                        if Sum_2 == Max_1:
                                            L1.append(i)
                                for i in L1:
                                    print("The class Topper of class", Task_5, "is", Dict_Data[i][0])

                            elif Topper == 2:
                                for i in Dict_Data:
                                    Sum_3 = Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
                                    if Sum_3 >= Max_1:
                                        Max_1 = Sum_3
                                for i in Dict_Data:
                                    Sum_4 = Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
                                    if Sum_4 == Max_1:
                                        L1.append(i)
                                for i in L1:
                                    print("The class Topper of school is ", Dict_Data[i][0])

                            elif Topper == 3:
                                for i in Dict_Data:
                                    L_Eng.append(Dict_Data[i][6])
                                    L_CS.append(Dict_Data[i][10])
                                    L_Phy.append(Dict_Data[i][7])
                                    L_Chem.append(Dict_Data[i][9])
                                    L_Mat.append(Dict_Data[i][8])
                                    Eng_top = max(L_Eng)
                                    CS_top = max(L_CS)
                                    Phy_top = max(L_Phy)
                                    Mat_top = max(L_Mat)
                                    Chem_top = max(L_Chem)

                                for i in Dict_Data:
                                    if Dict_Data[i][6] == Eng_top:
                                        print("The English Topper is", Dict_Data[i][0])
                                for i in Dict_Data:
                                    if Dict_Data[i][7] == Phy_top:
                                        print("The Physics Topper is", Dict_Data[i][0])
                                for i in Dict_Data:
                                    if Dict_Data[i][8] == Mat_top:
                                        print("The Maths Topper is", Dict_Data[i][0])
                                for i in Dict_Data:
                                    if Dict_Data[i][9] == Chem_top:
                                        print("The Chemistry Topper is", Dict_Data[i][0])
                                for i in Dict_Data:
                                    if Dict_Data[i][10] == CS_top:
                                        print("The Computer Science Topper is", Dict_Data[i][0])
                            else:
                                print("Give a valid input")
                        else:
                            print("Give a valid input")
                    elif Task_2 == 4:  # Calculate Data
                        Gr_no = int(input("1.Enter Gr.no."))
                        Average = (Dict_Data[Gr_no][6] + Dict_Data[Gr_no][7] + Dict_Data[Gr_no][8] + Dict_Data[Gr_no][9] +Dict_Data[Gr_no][10]) / 5
                        Percent_Eng = (Dict_Data[Gr_no][6] / 30) * 100
                        Percent_Phy = (Dict_Data[Gr_no][7] / 30) * 100
                        Percent_Math = (Dict_Data[Gr_no][8] / 30) * 100
                        Percent_Chem = (Dict_Data[Gr_no][9] / 30) * 100
                        Percent_CS = (Dict_Data[Gr_no][10] / 30) * 100
                        C_1 = int(input("Calculate\n1.Average Marks \n2.Overall Percentage \n3.1"
                                        "Individual Subject Percentage\nEnter the task you want to perform:"))
                        if C_1 == 1:
                            print("English:", Dict_Data[Gr_no][6])
                            print("Physics:", Dict_Data[Gr_no][7])
                            print("Maths:", Dict_Data[Gr_no][8])
                            print("Chemistry:", Dict_Data[Gr_no][9])
                            print("Computer Science:", Dict_Data[Gr_no][10])
                            print()
                            print("Average Mark is:", Average)
                        elif C_1 == 2:
                            print("English:", Dict_Data[Gr_no][6])
                            print("Physics:", Dict_Data[Gr_no][7])
                            print("Maths:", Dict_Data[Gr_no][8])
                            print("Chemistry:", Dict_Data[Gr_no][9])
                            print("Computer Science:", Dict_Data[Gr_no][10])
                            print()
                            print("Overall Percentage:", (Average / 30) * 100)
                        elif C_1 == 3:
                            print("Percentage in English:", Percent_Eng)
                            print("Percentage in Phy:", Percent_Phy)
                            print("Percentage in Math:", Percent_Math)
                            print("Percentage in Chem:", Percent_Chem)
                            print("Percentage in CS:", Percent_CS)

                    elif Task_2 == 5:  # Modify Data
                        while True:
                            E_Gr_no = int(input("Enter the Gr no of the students whose data is to be modified"))
                            print("Which Category will you like to modify:")
                            print("1.Name \n2.Fathers Name \n3.Mothers Name \n4.Class \n5.Roll No. \n6.Date of Birth\n7.English Marks \n8.Physics Marks \n9.Maths Marks \n10.Chemistry marks \n11.Computer science marks \n12.Admission date ")
                            modify_input = int(input("Enter a digit to modify corresponding entry:"))
                            if modify_input == 1:
                                name = input("Enter the new name").capitalize()
                                Dict_Data[E_Gr_no][0] = name
                            elif modify_input == 2:
                                F_name = input("Enter the new father's name").capitalize()
                                Dict_Data[E_Gr_no][1] = F_name
                            elif modify_input == 3:
                                M_name = input("Enter the new mother's name").capitalize()
                                Dict_Data[E_Gr_no][2] = M_name
                            elif modify_input == 4:
                                while True:
                                    Class = input("Enter new Class with section(Format=00-X)")
                                    if int(Class[:1]) <= 12 and len(Class[3:]) == 1 and Class[2] == '-':
                                        Dict_Data[E_Gr_no][3] = Class
                                        break
                                    else:
                                        print("Enter a Class Between 1 to 12")
                                        continue
                            elif modify_input == 5:
                                Roll_No = int(input("Enter the new Roll No. "))
                            elif modify_input == 6:
                                while True:
                                    DoB = input("Enter corrected Date of Birth(dd/mm/yy)")
                                    if 1 <= int(DoB[:2]) <= 31 and 1 <= int(DoB[3:5]) <= 12 and 00 <= int(
                                            DoB[6:]) <= 22:
                                        Dict_Data[E_Gr_no][5] = DoB
                                        break
                                    else:
                                        print("Enter a valid Date of Birth")
                                        continue
                            elif modify_input == 7:
                                while True:
                                    M_Eng = int(input("Enter correct Marks in English "))
                                    if 0 <= M_Eng <= 30:
                                        Dict_Data[E_Gr_no][6] = M_Eng
                                        break
                                    else:
                                        print("Enter Marks Out of 30")
                                        continue
                            elif modify_input == 8:
                                while True:
                                    M_Phy = int(input("Enter correct Marks in Physics "))
                                    if 0 <= M_Phy <= 30:
                                        Dict_Data[E_Gr_no][7] = M_Phy
                                        break
                                    else:
                                        print("Enter Marks Out of 30")
                                        continue
                            elif modify_input == 9:
                                while True:
                                    M_Math = int(input("Enter correct Marks in Maths "))
                                    if 0 <= M_Math <= 30:
                                        Dict_Data[E_Gr_no][8] = M_Math
                                        break
                                    else:
                                        print("Enter Marks Out of 30")
                                        continue
                            elif modify_input == 10:
                                while True:
                                    M_Chem = int(input("Enter correct Marks in Chemistry "))
                                    if 0 <= M_Chem <= 30:
                                        Dict_Data[E_Gr_no][9] = M_Chem
                                        break
                                    else:
                                        print("Enter Marks Out of 30")
                                        continue
                            elif modify_input == 11:
                                while True:
                                    M_CS = int(input("Enter correct Marks in Computer Science "))
                                    if 0 <= M_CS <= 30:
                                        Dict_Data[E_Gr_no][10] = M_CS
                                        break
                                    else:
                                        print("Enter Marks Out of 30")
                                        continue
                            elif modify_input == 12:
                                while True:
                                    Adm_Date = input("Enter correct Admission date(dd/mm/yy)")
                                    if 1 <= int(Adm_Date[:2]) <= 31 and 1 <= int(Adm_Date[3:5]) <= 12 and 00 <= int(
                                            Adm_Date[6:]) <= 22:
                                        Dict_Data[E_Gr_no][11] = Adm_Date
                                        break
                                    else:
                                        print("Enter a valid Admission date")
                                        continue
                            while True:
                                a = 0
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
                    elif Task_2 == 6:  # Print Report Data
                        Gr_no = int(input("1.Enter Gr.no."))
                        # section = input("Enter section:")

                        space0 = " " * (51 - len(Dict_Data[Gr_no][11]) - len(Dict_Data[Gr_no][3][3:]))
                        space1 = " " * (40 - len(Dict_Data[Gr_no][0]))
                        space2 = " " * (41 - len(Dict_Data[Gr_no][1]))
                        space3 = " " * (41 - len(Dict_Data[Gr_no][2]))

                        print(" " * 25, "Anand Vidya Vihar School")
                        print(" " * 28, "Harinagar, Vadodara")
                        print(" " * 31, "Report Card")

                        print("Class:", Dict_Data[Gr_no][3], Dict_Data[Gr_no][3][4:], space0, "Admission Date", Dict_Data[Gr_no][11])
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
                        print("Average marks:", (Dict_Data[Gr_no][6] + Dict_Data[Gr_no][7] + Dict_Data[Gr_no][8] + Dict_Data[Gr_no][9] +Dict_Data[Gr_no][10]) / 5)
                    elif Task_2 == 7:  # Logged out
                        print("You are successfully logged out")
                        break
                    else:
                        print("Give a valid input")
                break
            else:
                print("Password Incorrect")
                i += 1
    elif Login_1 == 2:
        while i <= 3:
            Pass_1 = input("Enter the password:")  # Student password
            if Pass_1 == "Avv123":
                print("Logged in as Student.")  # student Loop start here
                while True:
                    Task_1 = int(input("Tasks:\n 1.View Data \n 2.Extract Data \n 3.Print Report Card \n 4.Log out \n Enter the Number:"))  # 1.View own (or) topper 2.Extract 3.Report Card 4.Exit
                    if Task_1 == 1:  # View Data
                        Task_4 = int(input("Tasks: \n 1.Details of student \n 2.Topper's list \n Enter the number:"))
                        if Task_4 == 1:
                            Gr_no = int(input("1.Enter Gr.no."))
                            print("Name of student:", Dict_Data[Gr_no][0])
                            print("Date of Birth:", Dict_Data[Gr_no][5])
                            print("Admission Date:", Dict_Data[Gr_no][11])
                            print("Roll No.:", Dict_Data[Gr_no][4])
                            print("Marks of English", Dict_Data[Gr_no][6])
                            print("Marks of Physics", Dict_Data[Gr_no][7])
                            print("Marks of Mathematics", Dict_Data[Gr_no][8])
                            print("Marks of Chemistry", Dict_Data[Gr_no][9])
                            print("Marks of Computer Science", Dict_Data[Gr_no][10])

                        elif Task_4 == 2:
                            Topper = int(input("Topper: \n1.Class Topper \n2.School Topper \n3.Subject Topper \nEnter the number:"))
                            Max_1 = 0
                            L1 = []
                            L_Eng = []
                            L_Mat = []
                            L_Chem = []
                            L_Phy = []
                            L_CS = []
                            if Topper == 1:
                                Task_5 = int(input("Enter the class:"))
                                for i in Dict_Data:
                                    if int(Dict_Data[i][3][0:2]) == Task_5:
                                        Sum_1 = Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
                                        if Sum_1 >= Max_1:
                                            Max_1 = Sum_1
                                for i in Dict_Data:
                                    if int(Dict_Data[i][3][0:2]) == Task_5:
                                        Sum_2 = Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
                                        if Sum_2 == Max_1:
                                            L1.append(i)
                                for i in L1:
                                    print("The class Topper of class", Task_5, "is", Dict_Data[i][0])

                            elif Topper == 2:
                                for i in Dict_Data:
                                    Sum_3 = Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
                                    if Sum_3 >= Max_1:
                                        Max_1 = Sum_3
                                for i in Dict_Data:
                                    Sum_4 = Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
                                    if Sum_4 == Max_1:
                                        L1.append(i)
                                for i in L1:
                                    print("The class Topper of school is ", Dict_Data[i][0])

                            elif Topper == 3:
                                for i in Dict_Data:
                                    L_Eng.append(Dict_Data[i][6])
                                    L_CS.append(Dict_Data[i][10])
                                    L_Phy.append(Dict_Data[i][7])
                                    L_Chem.append(Dict_Data[i][9])
                                    L_Mat.append(Dict_Data[i][8])
                                    Eng_top = max(L_Eng)
                                    CS_top = max(L_CS)
                                    Phy_top = max(L_Phy)
                                    Mat_top = max(L_Mat)
                                    Chem_top = max(L_Chem)

                                for i in Dict_Data:
                                    if Dict_Data[i][6] == Eng_top:
                                        print("The English Topper is", Dict_Data[i][0])
                                for i in Dict_Data:
                                    if Dict_Data[i][7] == Phy_top:
                                        print("The Physics Topper is", Dict_Data[i][0])
                                for i in Dict_Data:
                                    if Dict_Data[i][8] == Mat_top:
                                        print("The Maths Topper is", Dict_Data[i][0])
                                for i in Dict_Data:
                                    if Dict_Data[i][9] == Chem_top:
                                        print("The Chemistry Topper is", Dict_Data[i][0])
                                for i in Dict_Data:
                                    if Dict_Data[i][10] == CS_top:
                                        print("The Computer Science Topper is", Dict_Data[i][0])
                            else:
                                print("Give a valid input")
                        else:
                            print("Give a valid input")
                    elif Task_1 == 2:  # Extract Data
                            Gr_no = int(input("1.Enter Gr.no."))
                            print("Name of student:", Dict_Data[Gr_no][0])
                            print("Date of Birth:", Dict_Data[Gr_no][5])
                            print("Admission Date:", Dict_Data[Gr_no][11])
                            print("Roll No.:", Dict_Data[Gr_no][4])
                            print("Marks of English", Dict_Data[Gr_no][6])
                            print("Marks of Physics", Dict_Data[Gr_no][7])
                            print("Marks of Mathematics", Dict_Data[Gr_no][8])
                            print("Marks of Chemistry", Dict_Data[Gr_no][9])
                            print("Marks of Computer Science", Dict_Data[Gr_no][10])
                    elif Task_1 == 3:  # Print Report Card
                        Gr_no = int(input("1.Enter Gr.no."))
                        # section = input("Enter section:")

                        space0 = " " * (51 - len(Dict_Data[Gr_no][11]) - len(Dict_Data[Gr_no][3][3:]))
                        space1 = " " * (40 - len(Dict_Data[Gr_no][0]))
                        space2 = " " * (41 - len(Dict_Data[Gr_no][1]))
                        space3 = " " * (41 - len(Dict_Data[Gr_no][2]))

                        print(" " * 25, "Anand Vidya Vihar School")
                        print(" " * 28, "Harinagar, Vadodara")
                        print(" " * 31, "Report Card")

                        print("Class:", Dict_Data[Gr_no][3], Dict_Data[Gr_no][3][4:], space0, "Admission Date", Dict_Data[Gr_no][11])
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
                        print("Average marks:", (Dict_Data[Gr_no][6] + Dict_Data[Gr_no][7] + Dict_Data[Gr_no][8] + Dict_Data[Gr_no][9] +Dict_Data[Gr_no][10]) / 5)
                    elif Task_1 == 4:  # Log out
                        print("You are successfully logged out")
                        break
                    else:
                        print("Give a valid input")
            else:
                print("Password Incorrect")
                i += 1
            break
    elif Login_1 == 3:
        print("Thanks for using the school management system ")
        print("Hope you had a great day")
        break
    else:
        print("Please enter a Valid Input")
