# Dict_Data ={Gr no.:[Name(0),F.Name(1),M.Name(2),Class(3),Roll No.(4),DoB(5),M-Eng(6),M-Phy(7),M-Math(8),M-Chem(9),M-CS(10), Admission Date(11)}
# 1.Details of student(Name, Admission date, Roll No, DOB, Marks   2. Topper list(Class wise, Subject wise , School wise))
Task_3 = int(input("Tasks: \n 1.Details of student \n 2.Topper's list \n Enter the number:"))
if Task_3 == 1:
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

#elif Task_3 == 2: