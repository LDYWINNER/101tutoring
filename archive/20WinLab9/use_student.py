import student


def main():
    # Start adding things here.
    s1 = student.Student('Amy', 1, 'CS', 3.21)
    print('s1:', s1)

    s2 = student.Student('Ken', 2, 'TSM', 3.42)
    print('s2:', s2)

    print('s1 == s1:', s1 == s1)
    print('s1 == s2:', s1 == s2)

    print('s1 < s1:', s1 < s1)
    print('s1 < s2:', s1 < s2)

    s1.change_major('TSM')
    print('s1:', s1)

    s1.change_gpa(s1.gpa + 0.3)
    print('s1.gpa:', s1.gpa)

    tsm_majors = [s1, s2]
    gpa_sum = 0.0
    for s in tsm_majors:
        gpa_sum += s.gpa
    print('Average GPA = ' + str(gpa_sum / len(tsm_majors)))

main()
