import random
from timeit import default_timer
import copy


def bubble_sort(alist):
    n = len(alist)
    for i in range(n-1):
        is_already_sorted = False
        for j in range(n-i-1):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                is_already_sorted = True
        if not is_already_sorted:
            break
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    bubble_sort(alist)
    print("新列表为：%s" % alist)

# 快速排序

def quick_sort(L):
    return q_sort(L,0,len(L)-1)

def q_sort(L,left,right):
    if left < right:
        base_index = partition(L,left,right)
        q_sort(L,left,base_index-1)
        q_sort(L,base_index+1,right)
    return L

def partition(L,left,right):
    base = L[left]
    while left < right:
        while left < right and L[right] >= base:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= base:
            left += 1
        L[right] = L[left]
    L[left] = base
    return left

random.seed(42)
L = []
for i in range(10000):
    L.append(random.randint(0, 100))
L2 = copy.deepcopy(L)

time_start_quicksort = default_timer()
quick_sort(L)
time_end_quicksort = default_timer()
time_elpase = time_end_quicksort - time_start_quicksort
print(f"quick sort - L: with time {time_elpase}")


time_start_bubble = default_timer()
bubble_sort(L2)
time_end_bubble = default_timer()
time_elpase = time_end_bubble - time_start_bubble
print(f"bubble sort - L: with time {time_elpase}")
