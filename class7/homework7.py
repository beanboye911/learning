import school
student_dict = {}
jason = school.Student(id = 1, name = 'Jason', age = 19, score = 10)
student_dict[1] = jason

amy = school.Student(id = 2, name = 'Amy', age = 15, score = 20)
student_dict[2] = amy
amy.print()

input()