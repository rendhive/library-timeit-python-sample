import timeit

def process_a():
    return sum(range(100))

def process_b():
    return sum(range(1000))

execution_time = timeit.timeit(lambda: (process_a(), process_b()), number=10000)
print(f"Waktu eksekusi process_a dan process_b: {execution_time} detik")
# Fungsi: Mengukur waktu untuk menjalankan beberapa fungsi dalam satu pemanggilan.
# Kondisi: Ketika Anda ingin memeriksa kinerja saat menjalankan fungsi secara bersamaan.