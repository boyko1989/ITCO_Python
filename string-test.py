import string


def run():
    with open('example.txt', 'r') as text:
        s = text.read()
        # print(s)

        strn = string.Formatter()
        print(s)
        s_str = list(strn.parse(s))  # string.Formatter().parse(s)

        print(s_str)
        # print(s_str[0][0] + ' ты ' + s_str[1][0])

        you = 'ты'

        print(s.format(you))

    print('----------------')

    mylist = iter(["apple", "banana", "cherry"])
    x = next(mylist)
    print(x)
    x = next(mylist)
    print(x)
    x = next(mylist)
    print(x)

    # s = "{foo} spam eggs {bar}"
    # string.Formatter().parse(s)
    # s_lst = list(string.Formatter().parse(s))
    # print(s_lst)
    # # print(s_lst[0][1])
    # # print(s_lst[1][1])


if __name__ == '__main__':
    run()
