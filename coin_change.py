def change_coins3(M, c, v):
    """
    Convert some amount of money M into given denominations, using the
    smallest possible number of coins.
    :param M: The amount of money to be converted
    :param c: Array of the available denominations to use
    :param v: Array of the available number of denominations for each corresponding c_i

    :return: A list of d integers i1, i2, ... , id such that c1i1+c2i2+
··· + cdid = M, and i1 + i2 + ··· + id is as small as possible. d is length of c.
    """
    pass


def change_coins2(M, c):
    """
    Convert some amount of money M into given denominations, using the
    smallest possible number of coins.
    :param M: The amount of money to be converted
    :param c: Array of the available denominations to use

    :return: A list of d integers i1, i2, . . . , id such that c1i1+c2i2+
· · · + cdid = M, and i1 + i2 + · · · + id is as small as possible. d is length of c.
    """
    d = len(c)
    coin_count = [None] * (M + 1)
    coin_count[0] = [0] * d
    lookup = [None] * (M + 1)
    lookup[0] = 0
    # for m from 1 to M
    for m in range(1, M + 1):
        coin_count[m] = [0] * d
        lookup[m] = float("inf")
        # for each of the coins we have
        for i in range(d):
            # if the m we're changing is equal or more than the coin
            if m >= c[i]:
                cnt1 = lookup[m - c[i]] + 1
                cnt2 = lookup[m]
                if cnt1 <= cnt2:
                    lookup[m] = cnt1
                    for x in range(d):
                        coin_count[m][x] = coin_count[m - c[i]][x]
                    coin_count[m][i] += 1
                else:
                    lookup[m] = cnt2

                if i == d-1:
                    print("m: {}. cnt1: {}. cnt2: {}. lookup[m]: {}".format(m, cnt1, cnt2, lookup[m]))

    return coin_count[M], lookup[M]


def change_coins3(M, c):
    """
    Convert some amount of money M into given denominations, using the
    smallest possible number of coins.
    :param M: The amount of money to be converted
    :param c: Array of the available denominations to use

    :return: The smallest number of coins needed
    """
    d = len(c)
    lookup = [None] * (M+1)
    lookup[0] = 0
    # for m from 1 to M
    for m in range(1, M+1):
        lookup[m] = float("inf")
        # for each of the coins we have
        for i in range(d):
            # if the coin is equal or smaller than the m we're changing
            if c[i] <= m:
                """
                Suppose you need to make change for 77 cents and the only coin denominations 
                available are 1, 3, and 7 cents. The best combination for 77 cents will
                be one (the minimum) of the following:
                • the best combination for 77 − 1 = 76 cents, plus a 1-cent coin;
                • the best combination for 77 − 3 = 74 cents, plus a 3-cent coin;
                • the best combination for 77 − 7 = 70 cents, plus a 7-cent coin.
                """
                cnt1 = lookup[m-c[i]] + 1
                cnt2 = lookup[m]
                print("m: {}. cnt1: {}. cnt2: {}".format(m, cnt1, cnt2))
                lookup[m] = min(cnt1, cnt2)
    # our answer
    return lookup[M]


if __name__ == "__main__":
    coin_count, n = change_coins2(19, [5, 1, 7, 3])
    print(n)
    print(coin_count)
    # n = change_coins3(11, [10, 5, 3, 1])
    # n = change_coins3(19, [5, 1, 3, 7])
    # print(n)
