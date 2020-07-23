students = {
    "Ivanov": [7,8,12],
    "Petrov": [6,4,10],
    "Kalashnikov": [7,11,8]
}

best = {"name":" ", "mark":0 }
loser = {"name":" ", "mark":0 }

def avg_stud(marks):
    return float("{:.2f}".format(sum(marks)/len(marks)))


for student in students.keys():
    avg = avg_stud(students.get(student))
    if (avg > best.get("mark")):
        best["mark"] = avg
        best["name"] = student
    if ((loser.get("mark") == 0) or (avg < loser.get("mark"))):
        loser["mark"] = avg
        loser["name"] = student

print(best,loser)