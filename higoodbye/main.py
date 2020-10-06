

def salam_khodafez(bacheha):
    for index, bache in enumerate(bacheha):
        reversed_bacheha = bacheha[::-1]
        for i in range(reversed_bacheha.index(bache) + 1, len(bacheha)):
            print(bache + ': '+ 'salam' + ' ' + reversed_bacheha[i] + '!')

    for index, bache in enumerate(bacheha):
        print(bache + ': '+ 'khodafez bacheha!')
        for i in range(index + 1, n):
            print(bacheha[i] + ': '+ 'khodafez ' + bache + '!')


if __name__ == '__main__':
    n = int(input())
    bacheha = list(map(str, input().rstrip().split()))
    salam_khodafez(bacheha)
