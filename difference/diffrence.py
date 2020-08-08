class Difference:

    def __init__(self, a):
        self.__elements = a
        maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        n = len(self.__elements)
        diffrences = []

        for i in range(0, n):
            j = i + 1
            while j < n:
                diffrence = abs(self.__elements[i] - self.__elements[j])
                diffrences.append(diffrence)
                j += 1

        self.maximumDifference = max(diffrences)
        return self.maximumDifference


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
