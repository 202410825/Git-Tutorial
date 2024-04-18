#과제

def read_single_digit(num):
    if num == 0:
        return '영'
    elif num == 1:
        return '일'
    elif num == 2:
        return '이'
    elif num == 3:
        return '삼'
    elif num == 4:
        return '사'
    elif num == 5:
        return '오'
    elif num == 6:
        return '육'
    elif num == 7:
        return '칠'
    elif num == 8:
        return '팔'
    elif num == 9:
        return '구'
    else :
        return '정수가 아닙니다.'
    
def read_number():
    num = int(input('세자리 정수 입력:'))

    firstnum = num // 100
    fnum = read_single_digit(firstnum)

    n = num % 100
    secondnumm = n // 10
    snum = read_single_digit(secondnumm)

    n = num % 100
    thirdnum = n % 10
    tnum = read_single_digit(thirdnum)

    print(f'{fnum}{snum}{tnum}')

read_number()