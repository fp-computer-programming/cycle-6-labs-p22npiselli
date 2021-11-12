# Author: Nolan (AMDG) 11/12/2021

subjects = ["math", "science", "history"]
subjects.append("latin")
print(subjects)

print(subjects.index("history"))

subjects.sort()
print(subjects)

c_subjects = subjects.copy()
c_subjects.reverse()
print(c_subjects)