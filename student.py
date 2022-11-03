class student:

    def __init__(self, name, degree, grade, is_on_probation):
        self.name = name
        self.degree = degree
        self.grade = grade
        self.is_on_probation = is_on_probation
    
    def first_class(self):
        if self.grade >= 70:
            return True
        else:
            return False
