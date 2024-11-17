from os import lstat

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a=sum(grades[0]) / len(grades[0])
b=sum(grades[1]) / len(grades[1])
c=sum(grades[2]) / len(grades[2])
d=sum(grades[3]) / len(grades[3])
e=sum(grades[4]) / len(grades[4])
students_list = (list(students))
students_list = { students_list[0] : a ,students_list[1]: b ,students_list[2] : c , students_list[3] : d , students_list[4] : e }
print(students_list)


