import datetime
Attendance_st=[]
def Attendance_Marking():
    print("<============================Mark Attendance==========================>")
    date=input("Enter date (YYYY-MM-DD) or press Enter for today:")
    if not date:
         date = str(datetime.date.today())

    student=int(input("Enter Number Of Student to Mark Attendance:"))
    for i in range (student):
        Name=input("Enter The Student Name:")
        Rollnumber=input("Enter The Rollnumber Of Student:")
        Course=input("Enter The Course Name:")
        Attendance=input("Present (P) and Absent (A):").strip().upper()
        if Attendance not in ('P','A'):
            print("Invalid status. Marking as Absent by default.")
            Attendance = 'A'
        Attendance_st.append({
                'Name':Name,
                'Rollnumber':Rollnumber,
                'Course':Course,
                'date':date,
                'Attendance':Attendance
            })
    print(f"Attendance Marked For {student} Students on {date}")      

def Attendance_Report():
    print("<===========================Attendance Report=======================>")
    option=input(""" Enter your option:-
                    1.Individual Student Report:-
                    2.Full class Report:-
                 """)
    
    if option=='1':
        Rollnumber=input("Enter The Rollnumber Of Student:")
        student_records = [i for i in Attendance_st if i['Rollnumber'] == Rollnumber]

        if not student_records:
            print("No Attendance records found for this student.")
            return

        total=len(student_records)
        present=sum(1 for i in student_records if i['Attendance']=='P')
        absent=total-present
        percantage=(present/total)*100

        print(f"Attendance Report for Roll No:{Rollnumber}")
        print(f"Name:{Name}")
        print(f"Total Days:{total}")
        print(f"Present Days:{present}")
        print(f"Absent Days:{absent}")
        print(f"Percantage:{percantage}")
        if percantage<75:
            print("Defaulter: Yes (Below 75%)")
        else:
            print("Good Attendance:-")
    elif option=='2':
        Course=input("Enter The Course Name:")
        Course_records=[i for i in Attendance_st if i['Course']==Course]
        if not Course_records:
            print("No Record found for this course")
            return
        Records={}
        for i in Course_records:
            Rollnumber=i['Rollnumber']
            Name=i['Name']
            key=(Rollnumber,Name)
            if key not in Records:
                Records[key]={'P':0,'A':0}
            if i['Attendance']=='P':
                Records[key]['P']+=1
            else:
                Records[key]['A']+=1
        print(f"Class Attendance Records for {Course}")
        print("Rollnumber\tName\t\tPresent\tAbsent\tDefaulter")   
        for (roll, name), counts in Records.items():
            total = counts['P'] + counts['A']
            percent = (counts['P'] / total) * 100
            defaulter = "Yes" if percent < 75 else "No"
            print(f"{roll}\t\t\t\t\t{name}\t\t{counts['P']}\t\t{counts['A']}\t{percent}%\t{defaulter}")
    else:
        print("Invalid Optional Selected!")

def Welcome_screen():
    while True:
        print("*****************************EduTrack Attendance Management Systeam**********************")
        print("1. Mark Attendance")
        print("2. Generate Report")
        print("3. Exit")
        choice=input("Enter your choice:-")
        if choice=='1':
            Attendance_Marking()
        elif choice=='2':
            Attendance_Report()
        elif choice=='3':
            print("Exit EduTrack!")
            break
        else:
            print("Invalid Choice!")

Welcome_screen()