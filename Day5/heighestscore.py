student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highestscore=0
for score in student_scores:
  if score > highestscore:
    highestscore=score
print(f"The highest score is {highestscore}")