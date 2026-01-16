import timeit

def list_comprehension():
    return [x ** 2 for x in range(1000)]

execution_time = timeit.timeit(list_comprehension, number=10000)
print(f"Waktu eksekusi list comprehension: {execution_time} detik")
# Fungsi: Mengukur waktu untuk menyusun daftar menggunakan list comprehension.
# Kondisi: Ketika ingin membandingkan kinerja antara list comprehension dan loop tradisional.