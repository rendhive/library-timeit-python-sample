import timeit

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

arr = [5, 2, 9, 1, 5, 6]

time_bubble = timeit.timeit(lambda: bubble_sort(arr), number=1000)
time_quick = timeit.timeit(lambda: quick_sort(arr), number=1000)

print(f"Waktu bubble_sort: {time_bubble} detik")
print(f"Waktu quick_sort: {time_quick} detik")
# Fungsi: Membandingkan dua algoritma pengurutan dalam hal kinerja.
# Kondisi: Ketika ingin mengukur dan membandingkan algoritma yang berbeda.