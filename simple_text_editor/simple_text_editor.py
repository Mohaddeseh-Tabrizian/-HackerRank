
if __name__ == '__main__':
    operation_numbers = int(input())
    current_string = ''
    states = []
    for _ in range(operation_numbers):
        arg = input().strip().split(' ')
        if arg[0] == '1':
            states.append(current_string)
            current_string += arg[1]
        elif arg[0] == '2':
            states.append(current_string)
            deleted = current_string[-int(arg[1]):]
            current_string = current_string[:-int(arg[1])]
        elif arg[0] == '3':
            print(current_string[int(arg[1]) - 1])
        elif arg[0] == '4':
            current_string = states.pop()
