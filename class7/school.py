class Student:
    def __init__(self, id, name, age, score):
        self.id = id
        self.name = name
        self.age = age
        self.score = score
    def print(self):
        print(f'Student id {self.id} name {self.name} age {self.age} score {self.score}')
        