import timeit

def simple_function():
    return sum(range(100))

# Mengukur waktu eksekusi fungsi
execution_time = timeit.timeit(simple_function, number=10000)
print(f"Waktu eksekusi simple_function: {execution_time} detik")
# Fungsi: Mengukur waktu yang dibutuhkan untuk menjalankan fungsi sebanyak 10.000 kali.
# Kondisi: Ketika Anda ingin mengukur kinerja fungsi sederhana.