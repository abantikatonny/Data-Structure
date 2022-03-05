def mergelist(a, b):
    ia, ib = 0, 0
    res = []

    while ia < len(a) and ib < len(b):
        if a[ia] < b[ib]:
            res.append(a[ia])
            ia += 1
        else:
            res.append(b[ib])
            ib += 1

    for val in range(ia, len(a)):
        res.append(a[val])

    for val in range(ib, len(b)):
        res.append(b[val])

    return res


def mergesort(inputlist):
    if len(inputlist) <= 1:
        return inputlist
    else:
        mid = len(inputlist) // 2
        left = mergesort(inputlist[:mid])
        right = mergesort(inputlist[mid:])

    return mergelist(left, right)


def merge_k_lists(kl):
    if len(kl) == 1:
        return kl

    while len(kl) > 1:
        res = []

        limit = len(kl)
        if len(kl) % 2 == 1:
            limit = len(kl) - 1

        for i in range(0, limit, 2):
            res.append((mergelist(kl[i], kl[i+1])))
            # print("ppp", res)
            if len(kl) % 2 == 1:
                res.append(kl[-1])

        kl = [j for j in res]


        print(kl)
    return kl







if __name__ == "__main__":
    # print(mergelist([5], [3, 7, 9, 90, 100, 1000, 1021]))
    # print(mergesort([12, 8, 1, 9, 2, 0 ]))


    """
    kl = [
        [1,2,3,4,5,6, 10],
        [2,4,6,8, 11],
        [3,5,7,8,9, 12],
        [1,1,2,3,4,8,10],
        [1,10,20,30,40],
        [2, 20, 30, 41, 59]
    ]
    """
    kl = [
        [1, 2, 3],
        [2, 5, 6, 9],
        [3, 5, 7, 8, 9, 12],
        [1, 1, 2, 3, 4, 8, 100],
        # [1, 10, 20, 30, 40],
        # [2, 20, 30, 41, 59]
    ]
    print(merge_k_lists(kl))


