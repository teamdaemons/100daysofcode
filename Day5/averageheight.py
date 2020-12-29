student_heights = [180, 124, 165, 173, 189, 169, 146]
total=0
count=0
for student in student_heights:
  total += student
  count+=1
print(round(total/count))  