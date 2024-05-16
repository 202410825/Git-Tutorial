def buy(shopping_bag):
    while True:
        item = input('상품명? ')
        if not item:  # 만약 상품명이 입력되지 않으면 종료
            return False
        num = int(input('수량은? '))
        if item in shopping_bag:
            shopping_bag[item] += num
        else:
            shopping_bag[item] = num
        print(f'{item} {num}개가 담았습니다.')
    return True

def show(shopping_bag):
    print('장바구니 보기:')
    for item, num in shopping_bag.items():
        print(f'{item}: {num}개')

def find(shopping_bag):
    item = input('장바구니에서 확인하고자 하는 상품은? ')
    if item in shopping_bag:
        print(f'{item}의 수량은 {shopping_bag[item]}개 입니다.')
    else:
        print(f'장바구니에 {item}은(는) 없습니다.')

def main():
    shopping_bag = {}
    while True:
        if not buy(shopping_bag):
            show(shopping_bag)
            find(shopping_bag)
            break

if __name__ == "__main__":
    main()
