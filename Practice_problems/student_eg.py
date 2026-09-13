from student import Student

stud1 = Student("Misaal",18)
stud2 = Student("Rahul",19)
stud3 = Student("Rajdeep",18)
stud4 = Student("Rhoswen",17)

print(stud1.name)
print(stud1.age)
print(Student.class_year)
print(Student.num_students)

print(f"This is the batch of {Student.class_year} and it contains {Student.num_students} passouts.")