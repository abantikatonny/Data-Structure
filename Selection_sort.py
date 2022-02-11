def selection_sort(L):
    for i in range(len(L) - 1):
        #set the min index
        min_idx = i
        for j in range(i+1, len(L) - 1):
            if L[j] < L[min_idx]:
                min_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]

L = [3, 1, 7, 26, 1, 90]
selection_sort(L)
print(L)


