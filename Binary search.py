def linear_search(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] == target:
            return i
    return -1

def binary_search(num_list, target):
    left = 0
    right = len(num_list) - 1
    mid = 0

    while left <= right:
        mid = (left+right)//2
        mid_num = num_list[mid]

        if mid_num == target:
            return mid
        elif mid_num < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(num_list, target, left, right):
    if right < left:
        return -1
    mid = (left + right) // 2
    mid_num = num_list[mid]

    if mid_num == target:
        return mid
    elif mid_num < target:
        left = mid + 1
    else:
        right = mid - 1

    return binary_search_recursive(num_list, target, left, right)


if __name__ == "__main__":
    num_list = [2, 3, 7, 9, 22, 25]
    target = 0

    # print(linear_search(num_list, target))
    # print(binary_search(num_list, target))
    print(binary_search_recursive(num_list, target,0, len(num_list)- 1))