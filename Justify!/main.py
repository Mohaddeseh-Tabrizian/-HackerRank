def correct_formatting(txt):
    formatted_txt = []

    first_word_of_line = True
    for index, word in enumerate(txt):
        if first_word_of_line == True:
            formatted_txt.append(word.capitalize())
        else:
            formatted_txt.append(word.lower())

        if word[-1] in ['!', '?', '.']:
            first_word_of_line = True
        else:
            first_word_of_line = False

    return formatted_txt


def select_words_for_line(formatted_txt, w):
    line = []
    lines = []
    remaining_space_for_other_chars = w
    next_index = 0
    while next_index < len(formatted_txt):
        word = formatted_txt[next_index]
        if len(word) <= remaining_space_for_other_chars:
            line.append(word)
            remaining_space_for_other_chars -= (1 + len(word))
            next_index += 1
        else:
            lines.append(line.copy())
            line = []
            remaining_space_for_other_chars = w
    lines.append(line)

    return lines


def calculate_spaces_per_line(line, w):
    char_count = 0
    for word in line:
        char_count += len(word)

    return w - char_count


def distribute_spaces(num_spaces, positions):
    # Adding just one space for every space position.
    position_map = []
    if positions == 0:
        return [num_spaces]

    k = num_spaces // positions

    for i in range(0, positions):
        position_map.append(k)
    # Adding extra spaces.
    extra = num_spaces % positions
    front_pointer = 0
    back_pointer = positions - 1
    flag_front_turn = False

    for j in range(0, extra):
        if flag_front_turn:
            position_map[front_pointer] = k + 1
            front_pointer += 1
            flag_front_turn = False
        else:
            position_map[back_pointer] = k + 1
            back_pointer -= 1
            flag_front_turn = True

    return position_map


def print_text(lines, w):
    for index, line in enumerate(lines):
        num_spaces = calculate_spaces_per_line(line, w)
        position_map = distribute_spaces(num_spaces, len(line) - 1)
        print('|', end='')

        for index, word in enumerate(line):
            if index == len(line) - 1 and index != 0:
                space = ''
            else:
                space = position_map[index] * ' '
            print(word + space, end='')

        print('|')


if __name__ == '__main__':
    t = int(input())

    for _ in range(0, t):
        nw = list(map(int, input().split()))

        n = nw[0]
        w = nw[1]

        txt = input().rstrip().split()
        formatted_txt = correct_formatting(txt)
        lines = select_words_for_line(formatted_txt, w)
        print_text(lines, w)