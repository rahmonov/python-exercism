all_students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

all_plants = {'V': 'Violets', 'R': 'Radishes', 'C': 'Clover', 'G': 'Grass'}


class Garden():
    def __init__(self, rows, students=all_students):
        self.rows = rows.split()
        self.students = sorted(students)

    def plants(self, student):
        """
        Returns student's plants as a list
        """
        student_plants = []
        for row in self.rows:
            student_plants.extend(self.get_plants_of(student, row))

        return student_plants

    def get_plants_of(self, student, row):
        """
        Returns student's plants in a row as a list
        """
        return [all_plants[row[self.students.index(student) * 2]],
                all_plants[row[self.students.index(student) * 2 + 1]]]