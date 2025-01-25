student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

#print(max(student_scores))

max_val = 0

for max in student_scores:
    if max > max_val:
        max_val = max
    else:
        max_val = max_val

print(max(student_scores))
