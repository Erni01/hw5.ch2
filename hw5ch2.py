# 5. A school decided to replace the desks in three classrooms.
# Each desk sits two students. Given the number of students in each class,
# print the smallest possible number of desks that can be purchased.
# The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
# In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
# The second group has 21 students, so they can get by with no fewer than 11 desks.
# 11 desks is also enough for the third group of 22 students.
# So we need 32 desks in total.


classA = int(input("Enter the number of students in class A: "))
classB = int(input("Enter the number of students in class B: "))
classC = int(input("Enter the number of students in class C: "))

classA += 1
classB += 1
classC += 1

print("Total number of needed desk is: ", classA // 2 + classB // 2 + classC // 2, ".")