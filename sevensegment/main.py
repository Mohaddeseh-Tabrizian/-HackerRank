

def led(adade_elmi):
    tedade_cheragh = 0
    minus_zero = 0
    for index, digit in enumerate(adade_elmi):
        e_index = adade_elmi.index('e')
        if digit == '0':
            tedade_cheragh += 6
        elif digit == '1':
            tedade_cheragh += 2
        elif digit == '2':
            tedade_cheragh += 5
        elif digit == '3':
            tedade_cheragh += 5
        elif digit == '4':
            tedade_cheragh += 4
        elif digit == '5':
            tedade_cheragh += 5
        elif digit == '6':
            tedade_cheragh += 6
        elif digit == '7':
            tedade_cheragh += 3
        elif digit == '8':
            tedade_cheragh += 7
        elif digit == '9':
            tedade_cheragh += 6
        elif digit == '.':
            for j in range(index + 1, e_index):
                minus_zero += 1

        if digit == 'e':
            zeros = ''
            for i in range(index + 1, len(adade_elmi)):
                zeros = zeros + adade_elmi[i]
            break

    total_zeroes = int(zeros) - minus_zero
    tedade_cheragh += 6 * total_zeroes
    return tedade_cheragh

if __name__ == '__main__':
    adade_elmi = list(map(str, input()))
    print(led(adade_elmi))
