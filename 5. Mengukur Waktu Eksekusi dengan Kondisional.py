import timeit

def conditional_function(n):
    if n < 10:
        return n
    else:
        return n * 2

execution_time = timeit.timeit("conditional_function(5)", globals=globals(), number=10000)
print(f"Waktu eksekusi conditional_function: {execution_time} detik")
# Fungsi: Mengukur waktu menjalankan fungsi dengan kondisi.
# Kondisi: Ketika ingin menilai kinerja fungsi bersyarat.