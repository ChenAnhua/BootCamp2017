def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
                       "digits differ by 2 or more: ")
    if len(step_1) != 3:
        raise ValueError('not a 3-digit number')
    step_2 = input("Enter the reverse of the first number, obtained "
                       "by reading it backwards: ")
    if step_2 != 1/step_1:
        raise ValueError('Not the reverse of first number')

    step_3 = input("Enter the positive difference of these numbers: ")
    if step_3 != abs(step_1 - step_2):
        raise ValueError('Not the positive difference of first two numbers')

    step_4 = input("Enter the reverse of the previous result: ")
    if step_4 != 1/step_3:
        raise ValueError('Not the reverse of the third number')

    print str(step_3) + " + " + str(step_4) + " = 1089 (ta-da!)"




class ContentFilter():
    def __init__(self, file_name):
        if type(file_name) != str:
            raise TypeError('File nameis not a string.')
        self.file_name = file_name
        with open(file_name, 'r') as f:
            self.contents = f.read()

    def uniform(self, file_name, case, mode = 'w'):
        if mode not in ['w', 'a']:
            raise ValueError('Mode is wrong.')
        if case == 'upper':
            with open(file_name, mode) as f:
                f.write(self.contents.upper())
        elif case == 'lower':
            with open(file_name, mode) as f:
                f.write(self.contents.lower())
        else:
            raise ValueError('Case is specified wrongfully')

    def reverse(self, file_name, unit = 'line', mode = 'w'):
        if mode not in ['w', 'a']:
            raise ValueError('Mode is wrong.')
        if unit == 'line':
            content_list = self.contents.split("\n")
            content_list = content_list[::-1]
            with open(file_name, mode) as f:
                f.writelines(content_list)
        elif unit == 'words':
            content_list = self.contents.split('\n')
            content_list = [line[::-1] for lin in content_list]
            with open(file_name, mode) as f:
                f.writelines(content_list)
        else:
            raise ValueError('Wrong Unit specified.')

    def transpose(self, file_name, mode = 'w'):
        if mode not in ['w', 'a']:
            raise ValueError('Mode is wrong.')
        content_list = self.contents.split('\n')
        content_list = [line.split() for line in content_list]
        content_array = np.array(content_list).T
        content_list = content_array.tolist()
        content_list = [' '.join(line_list) for line_list in content_list]
        with open(file_name, mode) as f:
            f.writelines(content_list)

    def __str__(self):
        num_letter = len(re.findall('[a-zA-z]', self.contents))
        num_digit  = len(re.findall('\d', self.contents))
        num_white  = len(re.findall('\w', self.contents))
        string     = 'Source file: \t{}\nTotal character:\t{}\nAlphabetic '\
                     'characters:\t{}\nNUmerical characters:t{}\n'\
                     'withespace characters:\t{}\n'\
                     'Number of lines:\t{}'.format(self.file_name, \
                                                   len(self.contents),
                                                   num_letter, num_digit, num_white,
                                                   len(self.contents.split('\n')))
return string
