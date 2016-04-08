class School():

    def __init__(self, name):
        self.name = name
        self._db = dict()

    @property
    def db(self):
        return self._db

    def add(self, student, grade):
        if grade not in self._db:
            self._db[grade] = set()

        self._db[grade].add(student)

    def grade(self, grade):
        if grade not in self._db:
            return set()

        return self._db[grade]

    def sort(self):
        return [(grade, tuple(self._db[grade])) for grade in sorted(self._db)]
