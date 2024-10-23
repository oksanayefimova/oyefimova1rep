def get_student():
    pass
def academ_integrity(students):
    is_cheater = {}
    for name, grades in students.items():
        if -2 <grades['final'] - sum(grades['grades'])/len(grades['grades'])<2:
            is_cheater[name]=False
        else:
            is_cheater[name] = False
    return is_cheater
def start_program():