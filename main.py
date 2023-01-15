# import fire
a = 2


class Tt:
    pass


def test():
    def test2():
        pass
    aabc = 1
    for i in range(4):
        if i == aabc:
            print(f"i is {i} now")
            continue
        if i == aabc + 1:
            print(f"i is {i} now")  # todo: Please fix this problem later.
            continue
    print("done!")


if __name__ == '__main__':
    test()
