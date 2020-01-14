def bsearch(lst, value):
    lo, hi = 0, len(lst)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] < value:
            lo = mid + 1
        elif lst[mid] > value:
            hi = mid - 1
        else:
            return mid
    return -1


lst = [5, 8, 11, 13, 19, 25, 36]
print(bsearch(lst, 6))
print(bsearch(lst, 13))
print(bsearch(lst, 8))
