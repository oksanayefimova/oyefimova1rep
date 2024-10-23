def get_student():
    students={}
    for i in range(10):
        name=input("Enter student's name")
        grades=input('Enter grades')
        final=input('Enter finals result')
        students[name]={'grades': grades, 'final': final}
    print(students)
def academ_integrity():
    pass
def start_program():