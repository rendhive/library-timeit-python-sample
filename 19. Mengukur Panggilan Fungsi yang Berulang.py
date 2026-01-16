import timeit

def repeat_string():
    return "Hello" * 100

execution_time = timeit.timeit(repeat_string, number=10000)
print(f"Waktu eksekusi repeat_string: {execution_time} detik")
# Fungsi: Mengukur waktu pengulangan string.
# Kondisi: Ketika Anda perlu memastikan kinerja operasi string yang sering digunakan.