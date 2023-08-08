class student:

    def __init__(self, id, lastName, firstName, courses = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        if courses == None:
            courses = {}
        else:
            courses = courses
        self.courses = courses
        
    def gpa(self):
        sum = 0
        numcour = len(self.courses)
        for value in self.courses.values():
            sum += value
        avg = sum/numcour
        self.avg = avg
        return self.avg

    def addCourse(self, course, score):
        assert score is score>=0 and score<=4
        self.course = course
        self.score = score
        self.courses[course] = score

    def addCourses(self, courses):
        self.courses.update(courses)

    def __str__(self):
        k = list(self.courses.keys())
        return f"{self.id:<10} {self.lastName:<12} {self.firstName:<12} {self.gpa():<5,.3f} {', '.join(k):<40}"
        
    def __repr__(self):
        return f"{self.id} {self.lastName} {self.firstName} {self.courses}"
    
    def header():
        return f"{'ID':<10} {'Last Name':<12} {'First Name':<12} {'GPA':<5} {'Courses':<40} \n {'='*85}"
    
s1 = student(123456,"Smith","Johnnie")
s2 = student(234567,"Strauss", "Jamie")
s3 = student(345678,"O'Neill","Jack")
s1c = {'CSE-101':3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00}
s2c = {'CSE-101': 3.00, 'CSE-103': 3.50, 'CSE-202': 3.25, 'CSE-220': 4.00, 'CSE-401': 4.00}
s3c = {'CSE-101': 2.50, 'CSE-102': 3.50, 'CSE-103': 3.00, 'CSE-104': 4.00}
for (k,v) in s1c.items():
    s1.addCourse(k,v)
for (k,v) in s2c.items():
    s2.addCourse(k,v)
for (k,v) in s3c.items():
    s3.addCourse(k,v)
s4 = student(456789,"Marks","Susie")
s5 = student(567890,"Marks", "Frank")
s6 = student(654321,"Marks", "Annie")
s4c = {'CSE-101': 4.00, 'CSE-103': 2.50, 'CSE-301': 3.50, 'CSE-302': 3.00, 'CSE-310': 4.00}
s5c = {'CSE-102': 4.00, 'CSE-104': 3.50, 'CSE-201': 2.50, 'CSE-202': 3.50, 'CSE-203': 3.00}
s6c = {'CSE-101': 4.00, 'CSE-102': 4.00, 'CSE-103': 3.50, 'CSE-201': 4.00, 'CSE-203': 4.00}
s4.addCourses(s4c)
s5.addCourses(s5c)
s6.addCourses(s6c)
s7 = student(456987,"Smith","John",{'CSE-101': 2.50, 'CSE-103': 3.00, 'CSE-210': 3.50, 'CSE-260': 4.00})
s8 = student(987456,"Smith","Judy", {'CSE-102': 4.00, 'CSE-103': 4.00, 'CSE-201': 3.00, 'CSE-210': 3.50, 'CSE-310': 4.00})
s9 = student(111354,"Williams","Kelly", {'CSE-101': 3.50, 'CSE-102': 3.50, 'CSE-201': 3.00, 'CSE-202': 3.50, 'CSE-203': 3.50})
s10 = student(995511,"Williams","Brad", {'CSE-102': 3.00, 'CSE-110': 3.50, 'CSE-125': 3.50, 'CSE-201': 4.00, 'CSE-203': 3.00})

students = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
def printStudents(students):
    print(student.header())
    for x in students:
        print(x)
printStudents(students)
#Query 1: Sorting by Name
namelist = sorted(students, key=lambda x: (x.lastName, x.firstName))
printStudents(namelist)
#Query 2: Sorting by GPA
gpalist = sorted(students, key=lambda x: x.gpa())
printStudents(gpalist)
#Query 3: Getting Unique set of Classes
classes = {(y) for x in students for y in x.courses.keys()}
print(classes)
#Query 4: List of Students who have taken CSE-201
students1 = [ x for x in students for y in x.courses.keys() if y == 'CSE-201']
printStudents(students1)
#Query 5: List of Honor students
students2 = [ x for x in students if x.gpa()>= 3.500]
printStudents(students2)