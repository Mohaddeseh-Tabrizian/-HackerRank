# Write your code here


class Calculator:
    def power(self, number, topowerof):
        if number < 0 or topowerof < 0:
            raise Exception('n and p should be non-negative')
        else:
            return pow(number, topowerof)


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

