import timeit

def loop_function():
    total = 0
    for i in range(1000):
        total += i
    return total

execution_time = timeit.timeit(loop_function, number=10000)
print(f"Waktu eksekusi loop_function: {execution_time} detik")
# Fungsi: Mengukur waktu untuk menjalankan loop dalam sebuah fungsi.
# Kondisi: Ketika ingin mengevaluasi kinerja kode dengan loop.