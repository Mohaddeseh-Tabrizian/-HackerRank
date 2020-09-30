

def how_many_wrong_answers(actual_string, persons_string, n):
    num_of_wrong_gusses = 0
    for i in range(0, n):
        if actual_string[i] != persons_string[i]:
            num_of_wrong_gusses += 1
    return num_of_wrong_gusses


if __name__ == '__main__':
    n = int(input())
    actual_string = input()
    persons_string = input()
    print(how_many_wrong_answers(actual_string, persons_string, n))
