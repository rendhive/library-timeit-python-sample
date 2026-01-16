import timeit

def precise_function():
    return sum([x * 0.1 for x in range(1000)])

execution_time = timeit.timeit(precise_function, number=10000)
print(f"Waktu eksekusi precise_function: {execution_time:.5f} detik")
# Fungsi: Mengukur waktu eksekusi dengan presisi desimal terbatas.
# Kondisi: Ketika ingin menampilkan waktu eksekusi dengan format tertentu.