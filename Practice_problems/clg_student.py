class Student:

    count = 0;
    total_gpa = 0;

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return(f"{self.name} {self.gpa}")

    @classmethod
    def get_count(cls):
        return f"Total no. of students are: {cls.count}"

    @classmethod
    def avg_gpa(cls):
        if cls.count == 0:
            return 0;
        else:
            return f"The average GPA is {Student.total_gpa/Student.count}"


student1 = Student("Rahul", 9.5)
student2 = Student("Misaal", 9.6)
student3 = Student("Saksham", 9.0)

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

print(Student.get_count())
print(Student.avg_gpa())
