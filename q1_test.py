def square_digits(num):
    num = str(num)
    n1 = int(num[0])
    n2 = int(num[-1])

    n1 = n1 ** 2
    n2 = n2 ** 2

    num = str(n1) + num[1:-1] + str(n2)

    return int(num)


def test_q1():
    assert square_digits(9119) == 811181
