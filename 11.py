import students


def input_student():
    student= []
    n = int(input("Enter number of student:"))
    for i in range(n):
        name =input(f"\nEnter name of students {i+1}:")
        mark = []
        subject = int(input(f"How many subject for {name}?"))
        for j in range(subject):
            mark = float(input(f" Enter mark of subject {j+1}:"))
            mark.append(mark)
        student.append({"name":name,"marks":mark})
    return students

def display_summary(student):
    print("\n---Student Grade Summary---")
    topper = None
    highest_avg = -1
    total_avg_sum = 0

    for student in students:
        avg = sum(student["marks"])/len(student["mark"])
        total_ang_sum += avg
        print(f"{student['name']}-> Marks:{student['mark']},Average:{avg:2f}")
        
        if avg>highest_avg:
            highest_avg=avg
            topper = student["name"]

    overall_class_avg=total_avg_sum/len(student)
    print("\nClassAverage:",round(overall_class_avg,2))

    # Main program
    students = input_student()
    display_summary(students)



