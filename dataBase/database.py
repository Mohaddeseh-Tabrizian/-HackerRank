

def pattern_match(email_id):
    static_pattern = '@gmail.com'
    if email_id.endswith(static_pattern):
        return True
    else:
        return False


if __name__ == '__main__':
    N = int(input())

    firstNames_matched = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if pattern_match(emailID):
            firstNames_matched.append(firstName)
    sorted_list = sorted(firstNames_matched)
    for name in sorted_list:
        print(name)
