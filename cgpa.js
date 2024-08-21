function handleChoiceChange() {
    const choice = parseInt(document.getElementById('choice').value);
    document.getElementById('gpaInputSection').classList.add('hidden');
    document.getElementById('regulationInputSection').classList.add('hidden');

    if (choice === 1) {
        document.getElementById('gpaInputSection').classList.remove('hidden');
        generateGPAInputs();
    } else if (choice === 2) {
        document.getElementById('regulationInputSection').classList.remove('hidden');
    }
}

function generateGPAInputs() {
    const gpasContainer = document.getElementById('gpas');
    gpasContainer.innerHTML = ''; // Clear previous inputs

    for (let i = 1; i <= 8; i++) {
        const input = document.createElement('input');
        input.type = 'number';
        input.id = `gpa${i}`;
        input.placeholder = `Enter GPA For Semester ${i}`;
        input.step = '0.01';
        input.min = '0';
        input.max = '10';
        gpasContainer.appendChild(input);
    }
}

function calculateCGPA() {
    let gpas = [];
    for (let i = 1; i <= 8; i++) {
        let gpa = parseFloat(document.getElementById(`gpa${i}`).value);
        if (!isNaN(gpa) && gpa >= 0) {
            gpas.push(gpa);
        }
    }
    if (gpas.length === 8) {
        let cgpa = gpas.reduce((acc, curr) => acc + curr, 0) / 8;
        document.getElementById('output').innerText = `CGPA: ${cgpa.toFixed(2)}`;
    } else {
        document.getElementById('output').innerText = 'Please enter GPAs for all semesters.';
    }
}

function startRegulationProcess() {
    const regulation = parseInt(document.getElementById('regulation').value);
    if (regulation === 2023) {
        handleRegulation2023();
    } else if (regulation === 2019) {
        handleRegulation2019();
    }
}

function getGradePoints(grade) {
    switch (grade) {
        case "o":
            return 10;
        case "a+":
            return 9;
        case "a":
            return 8;
        case "b+":
            return 7;
        case "b":
            return 6;
        case "f":
            return 0;
        default:
            return 0;
    }
}

function calculateGPA(sem, grades) {
    let totalPoints = 0;
    let totalCredits = Object.values(sem).reduce((acc, curr) => acc + curr, 0);
    let credits = Object.values(sem);

    grades.forEach((grade, index) => {
        totalPoints += getGradePoints(grade) * credits[index];
    });

    let gpa = totalPoints / totalCredits;
    console.log(`GPA for the semester: ${gpa.toFixed(2)}`);
    gpas.push(gpa);
}

const semesters2023 = {
    1: {"Communicative English": 3, "Engineering Chemistry": 3, "Matrices and Calculus": 4, 
        "Engineering Physics": 3, "Problem Solving and Python Programming": 3, "Heritage of Tamils": 1, 
        "Physics and Chemistry Laboratory": 2, "Problem Solving and Programming Laboratory": 2, 
        "Communicative English Laboratory": 1},

    2: {"Technical English": 3, "Statistics and Numerical Methods": 4, "Physics for Computer Science Engineers": 3, 
        "Engineering Graphics": 4, "Programming in C": 3, "Tamils and Technology": 1, 
        "Environmental Sciences and Sustainability": 2, "Technical English Laboratory": 1, 
        "Programming in C Laboratory": 2, "Engineering Practices Laboratory": 2},

    3: {"Digital Principles and Computer Organization": 4, "Foundation of Data Science": 3, "Data Structures": 3, 
        "Object Oriented Programming": 3, "Operating Systems": 4, "Data Structures Laboratory": 2, 
        "Object Oriented Programming Laboratory": 2, "Data Science Laboratory": 2, 
        "Quantitative Aptitude & Verbal Reasoning": 1},

    4: {"Software Engineering": 3, "Design and Analysis of Algorithms": 4, "Discrete Mathematics": 4, 
        "Database Management Systems": 3, "Java Programming": 3, "NCC Credit Course Level 2*": 3, 
        "Database Management Systems Laboratory": 2, "Java Programming Laboratory": 2, 
        "Quantitative Aptitude & Behavioural Skills": 1},

    5: {"Compiler Design": 4, "Open Elective-I": 3, "Mandatory Course-I": 0, "Computer Networks": 4, 
        "Full Stack Programming": 4, "Professional Elective-I": 3, "Professional Elective-II": 3, 
        "Quantitative Aptitude & Communication": 1},

    6: {"Mobile Computing": 3, "Open Elective-II": 3, "Mandatory Course-II": 0, "NCC Credit Level 3*": 3, 
        "Cryptography and Cyber Security": 4, "Artificial Intelligence and Machine Learning": 4, 
        "Professional Elective-III": 3, "Professional Elective-IV": 3, "Mobile Application Development Lab": 2, 
        "Quantitative Aptitude & Soft Skills": 1, "Mini Project": 2},

    7: {"Human Values and Ethics": 2, "Elective-Management*": 3, "Open Elective-III": 3, 
        "Professional Elective-V": 3, "Professional Elective-VI": 3, "Internship": 1},

    8: {"Project Work": 10}
};

const semesters2019 = {
    1: {"Communicative English": 2, "Engineering Chemistry": 3, "Matrices, Differential and Integral Calculus": 4,
        "Programming for Problem Solving in C": 3, "Engineering Graphics": 4, "Chemistry Laboratory": 1,
        "C Programming Laboratory": 2, "Communicative English Laboratory": 1},

    2: {"Vector Calculus and Complex Functions": 4, "Engineering Physics": 3, "Programming for Problem Solving using Python": 4,
        "Basic Electrical, Electronics and Communication Engineering": 3, "Introduction to Information and Computing Technology": 3,
        "Constitution of India": 0, "Physics Laboratory": 1, "Workshop Practice": 2, 
        "Basic Electrical, Electronics & Communication Engineering Laboratory": 1, "Quantitative Aptitude and Verbal Reasoning": 1},

    3: {"Data Structures": 3, "Digital Logic Circuits": 4, "Object Oriented Programming": 3, "Computer Architecture": 3,
        "Discrete Mathematics": 4, "Fundamentals of Nano Science": 0, "Data Structures Laboratory": 1,
        "Object Oriented Programming Laboratory": 1, "Personality & Character Development": 0, "Quantitative Aptitude & Behavioral Skills": 1},

    4: {"Operating System": 3, "Design and Analysis of Algorithms": 4, "Object Oriented Software Engineering": 3,
        "Database Management Systems": 3, "Java Programming": 3, "Probability and Queueing Theory": 4,
        "Environmental Science and Engineering": 0, "Operating System Laboratory": 1, "Programming in JAVA Laboratory": 1,
        "Database Management Systems Laboratory": 1, "Quantitative Aptitude & Communication Skills": 1},

    5: {"Internet Programming": 3, "Theory of Computation": 4, "Computer Networks": 3, "Professional Ethics and Human Values": 3,
        "Professional Elective-I": 3, "Open Elective-I": 3, "Internet Programming Laboratory": 1, "Computer Networks Laboratory": 1,
        "Quantitative Aptitude & Soft Skills": 1},

    6: {"Mobile Computing": 3, "Compiler Design": 3, "Artificial Intelligence": 4, "Resource Management Techniques": 3,
        "Professional Elective-II": 3, "Open Elective-II": 3, "Mobile Application Development Laboratory": 1,
        "Compiler Design Laboratory": 1, "Internship": 1, "Mini Project": 1},

    7: {"Cryptography and Network Security": 3, "Data Science using Python": 3, "Cloud Computing and Virtualization": 3,
        "Professional Elective-III": 3, "Professional Elective-IV": 3, "Open Elective-III": 3, "Cloud and Security Laboratory": 2,
        "Data Science using Python Laboratory": 2},

    8: {"Professional Elective-V": 3, "Professional Elective-VI": 3, "Project Work": 6}
};

function handleRegulation2023() {
    let gpas = [];

    function calculateGPA(sem, grades) {
        let totalPoints = 0;
        let totalCredits = Object.values(sem).reduce((acc, curr) => acc + curr, 0);
        let credits = Object.values(sem);

        grades.forEach((grade, index) => {
            totalPoints += getGradePoints(grade) * credits[index];
        });

        let gpa = totalPoints / totalCredits;
        console.log(`GPA for the semester: ${gpa.toFixed(2)}`);
        gpas.push(gpa);
    }

    function processSemesters() {
        let numSemesters = parseInt(prompt("Enter Total Number of Semesters To Be Calculated:"));
        for (let i = 0; i < numSemesters; i++) {
            let semesterNumber = parseInt(prompt("Enter semester:"));
            let grades = [];

            if (semesterNumber >= 1 && semesterNumber <= 8) {
                let semester = semesters2023[semesterNumber];
                for (let subject in semester) {
                    let grade = prompt(`${subject}:`).toLowerCase();
                    grades.push(grade);
                }
                calculateGPA(semester, grades);
            } else {
                console.log("Invalid semester number");
            }
        }

        let totalGPA = gpas.reduce((acc, curr) => acc + curr, 0);
        let cgpa = totalGPA / gpas.length;
        document.getElementById('output').innerText = `Total CGPA: ${cgpa.toFixed(2)}`;
    }

    processSemesters();
}

function handleRegulation2019() {
    let gpas = [];

    function calculateGPA(sem, grades) {
        let totalPoints = 0;
        let totalCredits = Object.values(sem).reduce((acc, curr) => acc + curr, 0);
        let credits = Object.values(sem);

        grades.forEach((grade, index) => {
            totalPoints += getGradePoints(grade) * credits[index];
        });

        let gpa = totalPoints / totalCredits;
        console.log(`GPA for the semester: ${gpa.toFixed(2)}`);
        gpas.push(gpa);
    }

    function processSemesters() {
        let numSemesters = parseInt(prompt("Enter Total Number of Semesters To Be Calculated:"));
        for (let i = 0; i < numSemesters; i++) {
            let semesterNumber = parseInt(prompt("Enter semester:"));
            let grades = [];

            if (semesterNumber >= 1 && semesterNumber <= 8) {
                let semester = semesters2019[semesterNumber];
                for (let subject in semester) {
                    let grade = prompt(`${subject}:`).toLowerCase();
                    grades.push(grade);
                }
                calculateGPA(semester, grades);
            } else {
                console.log("Invalid semester number");
            }
        }

        let totalGPA = gpas.reduce((acc, curr) => acc + curr, 0);
        let cgpa = totalGPA / gpas.length;
        document.getElementById('output').innerText = `Total CGPA: ${cgpa.toFixed(2)}`;
    }

    processSemesters();
}
