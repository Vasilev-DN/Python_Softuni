class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        Class.__students_count -= 1
        if Class.__students_count >= 0:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        number = f"{(sum(self.grades) / len(self.grades)):.2f}"
        return float(number)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. " \
               f"Average grade: {Class.get_average_grade(self)}"