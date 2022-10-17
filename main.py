import string


class My_Template(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+'

def run():
    # with open('example.txt', 'r') as text:
    #     text_string = text.read()
    #     print(string.capwords(text_string), '\n\n')

    ## Константы

    # print('Константа string.ascii_letters\n', string.ascii_letters, '\n\n')
    # print('Константа string.ascii_lowercase\n', string.ascii_lowercase, '\n\n')
    # print('Константа string.ascii_uppercase\n', string.ascii_uppercase, '\n\n')
    # print('Константа string.digits\n', string.digits, '\n\n')
    # print('Константа string.hexdigits\n', string.hexdigits, '\n\n')
    # print('Константа string.octdigits\n', string.octdigits, '\n\n')
    # print('Константа string.punctuation\n', string.punctuation, '\n\n')
    # print('Константа string.printable\n', string.printable, '\n\n')
    # print('Константа string.whitespace\n', string.whitespace, '\n\n')

    ## Шаблоны
    #
    # values = {'one': 'один', 'two': 'два'}
    #
    # temp_str = string.Template("""
    #     $one: первый пункт
    #     $two: второй пункт
    # """)
    #
    # print(temp_str.substitute(values))

    template_text = """
        Delimiter : %%
        Replaced  : %with_underscore
        Ignored   : %notunderscored 
    """

    d = {
        'with_underscore': 'replaced',
        'notunderscored': 'not replaced'
    }

    t = My_Template(template_text)
    print('With underscore:')
    print(t.safe_substitute(d))

    print('----------------')

    t2 = MyTemplate(template_text)
    print('Without underscore:')
    print(t2.safe_substitute(d))

if __name__ == '__main__':
    run()
