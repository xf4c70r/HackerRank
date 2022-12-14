if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total = 0.00
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key,val in student_marks.items():
        if(key == query_name):
            avg = sum(val)/len(val)
    print('%.2f'%avg)
