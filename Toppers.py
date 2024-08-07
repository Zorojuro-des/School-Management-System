Dict_Data = {1: ['vidit', 'chirayu', 'arpita', "11", 11, '27/11/2004', 30, 29, 29, 28, 27, '1/4/2011'],
             2: ['tapash', 'hiren', 'jigisha', "11", 20, '24/4/2005', 22, 29, 26, 23, 30, '1/4/2011'],
             3: ['devarsh', 'ashish', 'sonali', "11", 29, '20/12/2004', 24, 26, 30, 30, 30, '1/4/2011']}
Topper= int(input("Topper: \n1.Class Topper \n2.School Topper \n3.Subject Topper \nEnter the number:"))
Max_1=0
L1=[]
L_Eng=[]
L_Mat=[]
L_Chem=[]
L_Phy=[]
L_CS=[]
if Topper == 1:
    Task_5=int(input("Enter the class:"))
    for i in Dict_Data:
        if int(Dict_Data[i][3][0:2])==Task_5:
            Sum_1=Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
            if Sum_1>=Max_1:
                Max_1=Sum_1
    for i in Dict_Data:
        if int(Dict_Data[i][3][0:2])==Task_5:
            Sum_2=Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
            if Sum_2==Max_1:
                L1.append(i)
    for i in L1:
        print("The class Topper of class", Task_5,"is", Dict_Data[i][0] )

elif Topper == 2:
    for i in Dict_Data:
        Sum_3=Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
        if Sum_3>=Max_1:
            Max_1=Sum_3
    for i in Dict_Data:
        Sum_4=Dict_Data[i][6] + Dict_Data[i][7] + Dict_Data[i][8] + Dict_Data[i][9] + Dict_Data[i][10]
        if Sum_4==Max_1:
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
        Eng_top=max(L_Eng)
        CS_top=max(L_CS)
        Phy_top=max(L_Phy)
        Mat_top=max(L_Mat)
        Chem_top=max(L_Chem)

    for i in Dict_Data:
        if Dict_Data[i][6]==Eng_top:
            print("The English Topper is", Dict_Data[i][0])
    for i in Dict_Data:
        if Dict_Data[i][7]==Phy_top:
            print("The Physics Topper is", Dict_Data[i][0])
    for i in Dict_Data:
        if Dict_Data[i][8]==Mat_top:
            print("The Maths Topper is", Dict_Data[i][0])
    for i in Dict_Data:
        if Dict_Data[i][9]==Chem_top:
            print("The Chemistry Topper is", Dict_Data[i][0])
    for i in Dict_Data:
        if Dict_Data[i][10]==CS_top:
            print("The Computer Science Topper is", Dict_Data[i][0])
else:
    print("Give a valid input")