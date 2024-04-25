#7주차 과제
def display_multiplication_table(n):
    for n in range(1,10):
        for i in range(2,6):
            print(f'{i}x{n}={n*i:2} ',end= '')
        print()
    print()
    for n in range(1,10):
        for i in range(6,10):
            print(f'{i}x{n}={n*i:2} ',end= '')
        print()


display_multiplication_table(2)
