import timeit

def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)

execution_time = timeit.timeit(lambda: recursive_factorial(5), number=10000)
print(f"Waktu eksekusi recursive_factorial: {execution_time} detik")
# Fungsi: Mengukur waktu untuk memanggil fungsi rekursif.
# Kondisi: Ketika ingin mengukur performa rekursi.