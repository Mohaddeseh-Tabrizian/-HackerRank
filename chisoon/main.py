

if __name__ == '__main__':
    num_lines = int(input())
    # exec is like a compiler in python and it will execute any command given to it with a string
    for _ in range(0, num_lines):
        command = str(input().rstrip())
        if ':=' in command:
            command = command.replace(':=', '=')
            exec(command)
        if 'print' in command:
            command = command.replace('print', '')
            print(eval(command))
