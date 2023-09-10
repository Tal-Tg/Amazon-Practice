x = -12321321321


def reverse(x):
    reversed_num = 0
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    if reversed_num > 2**32:
        return 0;
    else:
        return reversed_num;

print(reverse(x))
