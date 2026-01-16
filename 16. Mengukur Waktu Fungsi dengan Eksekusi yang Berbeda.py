import timeit

def complex_function():
    total = sum([i * 2 for i in range(1000)])
    return total

time_taken = timeit.timeit("complex_function()", globals=globals(), number=5000)
print(f"Waktu eksekusi complex_function: {time_taken} detik")
# Fungsi: Mengukur waktu eksekusi fungsi kompleks.
# Kondisi: Ketika ingin mengetahui respons dan batas waktu dari fungsi yang memiliki pemrosesan lebih berat.