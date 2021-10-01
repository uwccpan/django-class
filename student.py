class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def set_scores(self, scores):
        self.scores = scores
    
    def get_avg(self):
        return sum(self.scores)/len(self.scores)

student1 = Student('jerry')
student1.set_scores([100, 99, 88])

student2 = Student('Mary')
student2.set_scores([120, 199, 288])

student3 = Student('KK')
student3.set_scores([18, 129, 218])

students = [student1, student2, student3, Student('kevin')]

for student in students:
    print(f'{student.name}\t 平均分數為:{round(student.get_avg(),2)}')

# print(student1)
# print(student1.name)
# print(student1.scores)
# print(student1.get_avg())