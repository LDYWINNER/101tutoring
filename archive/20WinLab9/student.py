class Student:
    """ Instance variables:
    name
    id
    major
    gpa
    """

    # Start adding things here
    def __init__(self, name, id, major, gpa):
        self.name = name
        self.id = id
        self.major = major
        self.gpa = gpa

    def __repr__(self):
        return '(' + self.name + ', ' + self.major + ')'

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def change_major(self, new_major):
        self.major = new_major

    def change_gpa(self, new_gpa):
        self.gpa = new_gpa

