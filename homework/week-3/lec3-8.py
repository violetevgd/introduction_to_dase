import random
def select_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr


def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


list1 = [random.randint(0, 1000000) for _ in range(0, 10)]
list2 = [random.randint(0, 1000000) for _ in range(0, 100)]
list3 = [random.randint(0, 1000000) for _ in range(0, 1000)]

print(list1)
print(merge_sort(list1))

#由于分治算法时间复杂度只有nlogn，在长度较大的情况下时间较快，而选择排序时间复杂度为n^2,在长度较大的情况下时间较慢