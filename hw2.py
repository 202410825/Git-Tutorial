def get_integer(prompt) :
    res = int(input(prompt))
    return res
def exchange(coin) :
    
    obaekwon = coin // 500
    coin = coin % 500
    baekwon = coin //100
    coin = coin % 100
    oushipwon = coin // 50
    coin = coin % 50
    shipwon = coin // 10
    print('500원 동전의 개수:',obaekwon)
    print('100원 동전의 개수:',baekwon)
    print('50원 동전의 개수:', oushipwon)
    print('10원 동전의 개수:',shipwon)

coin = get_integer('동전으로 교환하고자 하는 금액은?')
exchange(coin)