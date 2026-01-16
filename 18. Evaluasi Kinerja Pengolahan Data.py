import timeit

def data_manipulation():
    data = [i for i in range(1000)]
    return [x + 5 for x in data]

execution_time = timeit.timeit(data_manipulation, number=10000)
print(f"Waktu eksekusi data_manipulation: {execution_time} detik")
# Fungsi: Mengukur waktu untuk pemrosesan data di dalam list.
# Kondisi: Ketika Anda ingin memberikan analisis performa untuk pengolahan data yang intensif.