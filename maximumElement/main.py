class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)

        if self.max_stack == [] or value > self.max_stack[-1]:
            self.max_stack.append(value)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.stack.pop()
        self.max_stack.pop()

    def print(self):
        print(self.max_stack[-1])


if __name__ == '__main__':
    num_testcases = int(input())
    stack = Stack()
    for i in range(0, num_testcases):
        line = list(input().rstrip().split())
        if line[0] == '1':
            stack.push(int(line[1]))
        elif line[0] == '2':
            stack.pop()
        else:
            stack.print()
