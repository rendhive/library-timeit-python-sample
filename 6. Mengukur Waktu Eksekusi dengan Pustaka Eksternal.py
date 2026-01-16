import timeit
import math

def sqrt_function():
    return [math.sqrt(i) for i in range(1000)]

execution_time = timeit.timeit(sqrt_function, number=10000)
print(f"Waktu eksekusi sqrt_function: {execution_time} detik")
# Fungsi: Mengukur waktu untuk menghitung akar kuadrat dari sekumpulan angka.
# Kondisi: Ketika menggunakan pustaka eksternal dan ingin mengukur waktu eksekusi.