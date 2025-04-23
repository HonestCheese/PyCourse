class LettersCounter:
    def __init__(self, path):
        self.letters = {chr(i): 0 for i in range(1040, 1104)}
        self.path = path
        with open(self.path, mode='r', encoding='cp1251') as f:
            for line in f:
                for char in line:
                    if char in self.letters and char.isalpha():
                        self.letters[char] += 1

    def sorted_print(self, mode):
        if mode == "increase":
            print(f'+{"-" * 9}+{"-" * 9}+')
            print(f'|{'буква':^9}|{'частота':^9}|')
            print(f'+{"-" * 9}+{"-" * 9}+')
            sorted_letters = dict(sorted(self.letters.items(), key=lambda x: -x[1]))
            for letter in sorted_letters:
                print(f'|{letter:^9}|{sorted_letters[letter]:^9}|')
            print(f'+{"-" * 9}+{"-" * 9}+')
        if mode == "decrease":
            # summa = 0
            print(f'+{"-" * 9}+{"-" * 9}+')
            print(f'|{'буква':^9}|{'частота':^9}|')
            print(f'+{"-" * 9}+{"-" * 9}+')
            sorted_letters = dict(sorted(self.letters.items(), key=lambda x: x[1]))
            for letter in sorted_letters:
                print(f'|{letter:^9}|{sorted_letters[letter]:^9}|')
            print(f'+{"-" * 9}+{"-" * 9}+')
        if mode == "beauty":
            print(f'+{"-" * 9}+{"-" * 9}+')
            print(f'|{'буква':^9}|{'частота':^9}|')
            print(f'+{"-" * 9}+{"-" * 9}+')
            sorted_letters = dict(sorted(self.letters.items(), key=lambda x: x[0]))
            for letter in sorted_letters:
                print(f'|{letter:^9}|{sorted_letters[letter]:^9}|')
            print(f'+{"-" * 9}+{"-" * 9}+')
        if mode == "strange":
            print(f'+{"-" * 9}+{"-" * 9}+')
            print(f'|{'буква':^9}|{'частота':^9}|')
            print(f'+{"-" * 9}+{"-" * 9}+')
            sorted_letters = dict(sorted(self.letters.items(), key=lambda x: x[0], reverse= True))
            for letter in sorted_letters:
                print(f'|{letter:^9}|{sorted_letters[letter]:^9}|')
            print(f'+{"-" * 9}+{"-" * 9}+')


    def summa_bukv(self):
        summa = 0
        for letter in self.letters:
            summa += self.letters[letter]
        print(f'{summa:-^21}')


voina_i_mir = LettersCounter('python_snippets/voyna-i-mir.txt')
voina_i_mir.sorted_print(mode='strange')
voina_i_mir.summa_bukv()
