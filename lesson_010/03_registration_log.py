import re


class NotNameError(Exception):
    def __init__(self, name):
        self.message = f'Not a name: {name}'
        super().__init__(self.message)


class AgeError(Exception):
    def __init__(self, age):
        self.message = f'Incorrect age: {age}'
        super().__init__(self.message)


class NotEmailError(Exception):
    def __init__(self, email):
        self.message = f'Not an email: {email}'
        super().__init__(self.message)


with open('registrations.txt', 'r') as file, open('registration_good.log', 'w') as good, open('registration_bad.log',
                                                                                              'w') as bad:
    for line in file:
        try:
            if not line[:-1]:
                raise ValueError("Nothing given")
            parts = re.split(' ', line)
            if len(parts) == 3:
                parts[2] = parts[2][:-1]
            if len(parts) == 2:
                raise ValueError("Only 2 given")
            if len(parts) == 1:
                raise ValueError("Only 1 given")
            if not (parts[0].isalpha()):  # NAME ERROR
                raise NotNameError(parts[0])
            if '@' not in parts[1] or '.' not in parts[1]:  # EMAIL ERROR
                raise NotEmailError(parts[1])
            if parts[2].isdigit() and not (10 < int(parts[2]) < 99):  # AGE ERROR
                raise AgeError(parts[2])
            good.write(line)
        except ValueError as arg:
            print(f'Missing: {arg}')
            bad.write(line)
        except NotEmailError as arg:
            print(arg)
            bad.write(line)
        except NotNameError as arg:
            print(arg)
            bad.write(line)
        except AgeError as arg:
            print(arg)
            bad.write(line)
