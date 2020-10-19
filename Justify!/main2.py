class Text:
    def __init__(self, word_list, char_limit):
        self.word_list = word_list
        self.char_limit = char_limit
        self.last_index = -1
        self.end_of_line_chars = ['.', '!', '?']

    def get_lines(self):
        words_to_arrange = len(self.word_list)

        lines = []
        while words_to_arrange > 0:
            line = self.get_line()
            lines.append(line)
            words_to_arrange -= len(line)

        return lines

    def get_line(self):
        remaining_chars = self.char_limit
        words = []
        while True:
            next_index = self.last_index + 1
            if next_index == len(self.word_list):
                break

            next_word = self.word_list[next_index]
            next_word_char_count = len(next_word)
            if next_word_char_count <= remaining_chars:
                words.append(next_word)
                self.last_index = next_index

                remaining_chars -= (1 + next_word_char_count)
            else:
                break

        return words

    def calculate_spaces_per_line(self, line):
        char_count = 0
        for word in line:
            char_count += len(word)

        return self.char_limit - char_count

    def distribute_spaces(self, num_spaces, positions):
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
        flag_front_turn = True

        for j in range(0, extra):
            position_map[front_pointer] = k + 1
            if flag_front_turn:
                front_pointer += 1
                flag_front_turn = False
            else:
                back_pointer -= 1
                flag_front_turn = True

        return position_map

    def correct_formatting(self, word, previous_word):
        if previous_word is None or previous_word[-1] in self.end_of_line_chars:
            word = word.capitalize()
        else:
            word = word.lower()

        return word

    def println(self, line, previous_word):
        beginning_of_line = True
        num_spaces = self.calculate_spaces_per_line(line)
        positions = len(line) - 1
        spaces_map = self.distribute_spaces(num_spaces, positions)
        for index, word in enumerate(line):
            word = self.correct_formatting(word, previous_word)
            if beginning_of_line:
                print('|' + word, end='')
                beginning_of_line = False
            else:
                print(word, end='')

            if index == positions and index != 0:
                space = ''
            else:
                space = spaces_map[index] * ' '
            print(space, end='')

            if index == positions:
                print('|')

            previous_word = word

    def justify(self):
        previous_word = None
        lines = self.get_lines()
        for line in lines:
            self.println(line, previous_word)
            previous_word = line[-1]


if __name__ == '__main__':
    t = int(input())

    test_cases = []
    for i in range(0, t):
        counts = list(map(int, input().rstrip().split()))
        word_list = input().rstrip().split()

        test_cases.append({
            'word_count': counts[0],
            'char_limit': counts[1],
            'word_list': word_list
        })

    for test_case in test_cases:
        text = Text(test_case['word_list'], test_case['char_limit'])
        text.justify()