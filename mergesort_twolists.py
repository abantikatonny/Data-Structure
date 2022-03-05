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




if __name__ == "__main__":
    print(mergelist([5], [3, 7, 9, 90, 100, 1000, 1021]))
    print(mergesort([12, 8, 1, 9, 2, 0 ]))



