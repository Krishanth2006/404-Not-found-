print("1.Calculate Total CGPA With GPAs ..\n2.Caluate per Each Sem With Regulations...")
a = int(input("Enter Your Choice::"))

if a == 1:
    def semester():
        s1 = float(input("Enter GPA For First Semester::"))
        s2 = float(input("Enter GPA For Second Semester::"))
        s3 = float(input("Enter GPA For Third Semester::"))
        s4 = float(input("Enter GPA For Fourth Semester::"))
        s5 = float(input("Enter GPA For Fifth Semester::"))
        s6 = float(input("Enter GPA For Sixth Semester::"))
        s7 = float(input("Enter GPA For Seventh Semester::"))
        s8 = float(input("Enter GPA For Eighth Semester::"))
        cgpa = (s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8) / 8
        print("CGPA::", cgpa)
    semester()
else:
    b = int(input("Enter Your Regulation(2019/2023)"))
    if b == 2023:
        def grade(grade):
            if grade == "o":
                return 10
            elif grade == "a+":
                return 9
            elif grade == "a":
                return 8
            elif grade == "b+":
                return 7
            elif grade == "b":
                return 6
            elif grade == "f":
                return 0
            else:
                return 0

        li = []  # List to store GPA for each semester

        def cal(sem, l):
            t = 0
            t_c = sum(sem.values())
            l_c = list(sem.values())

            for i, j in zip(l, l_c):
                t += grade(i) * j

            gpa = t / t_c
            print(f"GPA for the semester: {gpa:.2f}")
            li.append(gpa)

        # Dictionaries for each semester
        sem1 = {"Communicative English": 3, "Engineering Chemistry": 3, "Matrices and Calculus": 4, 
                "Engineering Physics": 3, "Problem Solving and Python Programming": 3, "Heritage of Tamils": 1, 
                "Physics and Chemistry Laboratory": 2, "Problem Solving and Programming Laboratory": 2, 
                "Communicative English Laboratory": 1}

        sem2 = {"Technical English": 3, "Statistics and Numerical Methods": 4, "Physics for Computer Science Engineers": 3, 
                "Engineering Graphics": 4, "Programming in C": 3, "Tamils and Technology": 1, 
                "Environmental Sciences and Sustainability": 2, "Technical English Laboratory": 1, 
                "Programming in C Laboratory": 2, "Engineering Practices Laboratory": 2}

        sem3 = {"Digital Principles and Computer Organization": 4, "Foundation of Data Science": 3, "Data Structures": 3, 
                "Object Oriented Programming": 3, "Operating Systems": 4, "Data Structures Laboratory": 2, 
                "Object Oriented Programming Laboratory": 2, "Data Science Laboratory": 2, 
                "Quantitative Aptitude & Verbal Reasoning": 1}

        sem4 = {"Software Engineering": 3, "Design and Analysis of Algorithms": 4, "Discrete Mathematics": 4, 
                "Database Management Systems": 3, "Java Programming": 3, "NCC Credit Course Level 2*": 3, 
                "Database Management Systems Laboratory": 2, "Java Programming Laboratory": 2, 
                "Quantitative Aptitude & Behavioural Skills": 1}

        sem5 = {"Compiler Design": 4, "Open Elective-I": 3, "Mandatory Course-I": 0, "Computer Networks": 4, 
                "Full Stack Programming": 4, "Professional Elective-I": 3, "Professional Elective-II": 3, 
                "Quantitative Aptitude & Communication": 1}

        sem6 = {"Mobile Computing": 3, "Open Elective-II": 3, "Mandatory Course-II": 0, "NCC Credit Level 3*": 3, 
                "Cryptography and Cyber Security": 4, "Artificial Intelligence and Machine Learning": 4, 
                "Professional Elective-III": 3, "Professional Elective-IV": 3, "Mobile Application Development Lab": 2, 
                "Quantitative Aptitude & Soft Skills": 1, "Mini Project": 2}

        sem7 = {"Human Values and Ethics": 2, "Elective-Management*": 3, "Open Elective-III": 3, 
                "Professional Elective-V": 3, "Professional Elective-VI": 3, "Internship": 1}

        sem8 = {"Project Work": 10}

        def semester():
            global li
            l = []  # List to store grades
            n = int(input("Enter Total Number of Semesters To Be Calculated: "))

            for i in range(n):
                num = int(input("Enter semester: "))
                if num == 1:
                    for j in sem1.keys():
                        m1 = input(f"{j}: ").lower()
                        l.append(m1)
                    cal(sem1, l)
                elif num == 2:
                    for k in sem2.keys():
                        m2 = input(f"{k}: ").lower()
                        l.append(m2)
                    nc = int(input("If you have NCC credits: 1: YES 2: NO "))
                    if nc == 1:
                        l.append("o")
                    cal(sem2, l)
                elif num == 3:
                    for v in sem3.keys():
                        m3 = input(f"{v}: ").lower()
                        l.append(m3)
                    cal(sem3, l)
                elif num == 4:
                    for m in sem4.keys():
                        m4 = input(f"{m}: ").lower()
                        l.append(m4)
                    nc = int(input("If you have NCC credits: 1: YES 2: NO "))
                    if nc == 1:
                        l.append("o")
                    cal(sem4, l)
                elif num == 5:
                    for n in sem5.keys():
                        m5 = input(f"{n}: ").lower()
                        l.append(m5)
                    cal(sem5, l)
                elif num == 6:
                    for p in sem6.keys():
                        m6 = input(f"{p}: ").lower()
                        l.append(m6)
                    nc = int(input("If you have NCC credits: 1: YES 2: NO "))
                    if nc == 1:
                        l.append("o")
                    cal(sem6, l)
                elif num == 7:
                    for q in sem7.keys():
                        m7 = input(f"{q}: ").lower()
                        l.append(m7)
                    cal(sem7, l)
                elif num == 8:
                    for r in sem8.keys():
                        m8 = input(f"{r}: ").lower()
                        l.append(m8)
                    cal(sem8, l)
                else:
                    print("Invalid semester number")
                l = []  # Clear the list for the next semester

        # Call the function to process semesters and calculate CGPA
        semester()

        # Calculate CGPA
        total_gpa = sum(li)
        num_semesters = len(li)
        cgpa = total_gpa / num_semesters 
        print(f"Total CGPA: {cgpa:.2f}")

    else:
        def grade(grade):
            if grade == "o":
                return 10
            elif grade == "a+":
                return 9
            elif grade == "a":
                return 8
            elif grade == "b+":
                return 7
            elif grade == "b":
                return 6
            elif grade == "f":
                return 0
            else:
                return 0

        li = []  # List to store GPA for each semester

        def cal(sem, l):
            t = 0
            t_c = sum(sem.values())
            l_c = list(sem.values())
            for i, j in zip(l, l_c):
                if i == "ncc":
                    t += grade("o") * j
                else:
                    t += grade(i) * j

            gpa = t / t_c
            print(f"GPA for the semester: {gpa:.2f}")
            li.append(gpa)

        # Dictionaries for each semester
        sem1 = {"Communicative English": 2, "Engineering Chemistry": 3, "Matrices, Differential and Integral Calculus": 4,
                "Programming for Problem Solving in C": 3, "Engineering Graphics": 4, "Chemistry Laboratory": 1,
                "C Programming Laboratory": 2, "Communicative English Laboratory": 1}

        sem2 = {"Vector Calculus and Complex Functions": 4, "Engineering Physics": 3, "Programming for Problem Solving using Python": 4,
                "Basic Electrical, Electronics and Communication Engineering": 3, "Introduction to Information and Computing Technology": 3,
                "Constitution of India": 0, "Physics Laboratory": 1, "Workshop Practice": 2, 
                "Basic Electrical, Electronics & Communication Engineering Laboratory": 1, "Quantitative Aptitude and Verbal Reasoning": 1}

        sem3 = {"Data Structures": 3, "Digital Logic Circuits": 4, "Object Oriented Programming": 3, "Computer Architecture": 3,
                "Discrete Mathematics": 4, "Fundamentals of Nano Science": 0, "Data Structures Laboratory": 1,
                "Object Oriented Programming Laboratory": 1, "Personality & Character Development": 0, "Quantitative Aptitude & Behavioral Skills": 1}

        sem4 = {"Operating System": 3, "Design and Analysis of Algorithms": 4, "Object Oriented Software Engineering": 3,
                "Database Management Systems": 3, "Java Programming": 3, "Probability and Queueing Theory": 4,
                "Environmental Science and Engineering": 0, "Operating System Laboratory": 1, "Programming in JAVA Laboratory": 1,
                "Database Management Systems Laboratory": 1, "Quantitative Aptitude & Communication Skills": 1}

        sem5 = {"Internet Programming": 3, "Theory of Computation": 4, "Computer Networks": 3, "Professional Ethics and Human Values": 3,
                "Professional Elective-I": 3, "Open Elective-I": 3, "Internet Programming Laboratory": 1, "Computer Networks Laboratory": 1,
                "Quantitative Aptitude & Soft Skills": 1}

        sem6 = {"Mobile Computing": 3, "Compiler Design": 3, "Artificial Intelligence": 4, "Resource Management Techniques": 3,
                "Professional Elective-II": 3, "Open Elective-II": 3, "Mobile Application Development Laboratory": 1,
                "Compiler Design Laboratory": 1, "Internship": 1, "Mini Project": 1}

        sem7 = {"Cryptography and Network Security": 3, "Data Science using Python": 3, "Cloud Computing and Virtualization": 3,
                "Professional Elective-III": 3, "Professional Elective-IV": 3, "Open Elective-III": 3, "Cloud and Security Laboratory": 2,
                "Data Science using Python Laboratory": 2}

        sem8 = {"Professional Elective-V": 3, "Professional Elective-VI": 3, "Project Work": 6}

        def semester():
            global li
            l = []  # List to store grades
            n = int(input("Enter Total Number of Semesters To Be Calculated: "))
            for i in range(n):
                num = int(input("Enter semester: "))
                if num == 1:
                    for j in sem1.keys():
                        m1 = input(f"{j}: ").lower()
                        l.append(m1)
                    cal(sem1, l)
                elif num == 2:
                    for k in sem2.keys():
                        m2 = input(f"{k}: ").lower()
                        l.append(m2)
                    nc = int(input("If you have NCC credits: 1: YES 2: NO "))
                    if nc == 1:
                        l.append("ncc")
                    cal(sem2, l)
                elif num == 3:
                    for v in sem3.keys():
                        m3 = input(f"{v}: ").lower()
                        l.append(m3)
                    cal(sem3, l)
                elif num == 4:
                    for m in sem4.keys():
                        m4 = input(f"{m}: ").lower()
                        l.append(m4)
                    nc = int(input("If you have NCC credits: 1: YES 2: NO "))
                    if nc == 1:
                        l.append("ncc")
                    cal(sem4, l)
                elif num == 5:
                    for n in sem5.keys():
                        m5 = input(f"{n}: ").lower()
                        l.append(m5)
                    cal(sem5, l)
                elif num == 6:
                    for p in sem6.keys():
                        m6 = input(f"{p}: ").lower()
                        l.append(m6)
                    nc = int(input("If you have NCC credits: 1: YES 2: NO "))
                    if nc == 1:
                        l.append("ncc")
                    cal(sem6, l)
                elif num == 7:
                    for q in sem7.keys():
                        m7 = input(f"{q}: ").lower()
                        l.append(m7)
                    cal(sem7, l)
                elif num == 8:
                    for r in sem8.keys():
                        m8 = input(f"{r}: ").lower()
                        l.append(m8)
                    cal(sem8, l)
                else:
                    print("Invalid semester number")
                l = []  # Clear the list for the next semester

        # Call the function to process semesters and calculate CGPA
        semester()

        # Calculate CGPA
        total_gpa = sum(li)
        num_semesters = len(li)
        cgpa = total_gpa / num_semesters
        print(f"Total CGPA: {cgpa:.2f}")
