classmates = ["arav", "priya", "rahul", "senha", "dev"]
print("class list", classmates)
print("total students", len(classmates))
print("first student", classmates[0])
print("last student", classmates[-1])
print("first three", classmates[:3])
classmates.append("meera")
print("after adding meera", classmates)
classmates.remove("dev")
print("after removing dev", classmates)
classmates.sort()
print("sorted alpabetically", classmates)
classmates.reverse()
print("reversed", classmates)
teacher = {"name": "mr sharma", "subject": "pythone", "experience": 5}
print("teacher profile", teacher)
print("subject", teacher["subject"])
print("subject", teacher.get("experience", "not found"))
teacher["experience"] = 6
print("teacher", teacher)
teacher["email"] = "shrma@school.com"
teacher.pop("experience")
print("updated teacher profile", teacher)
roll_numbers = [1,2,3,4,5]
names = ["arav", "priya", "rahul", "sneha", "meera"]
student_directory = dict(zip(roll_numbers, names))
print("student directory", student_directory)
print("student at roll 3:", student_directory[3])