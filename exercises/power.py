def power(base, exponent):
    if (exponent == 0):
        return 1
    elif (exponent < 0):
        return power(base, exponent + 1) * (1 / base)
    else:
        return power(base, exponent - 1) * base

if __name__ == '__main__':
    positive = []
    for x in range(11):
        ans = power(2,x)
        print(ans)
        positive.append(ans)

    negative = []
    for x in reversed(range(-10, 1)):
        ans = power(2,x)
        print(ans)
        negative.append(ans)

    for x in range(11):
        print(positive[x] * negative[x])
    