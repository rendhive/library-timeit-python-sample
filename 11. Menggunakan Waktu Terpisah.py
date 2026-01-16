import timeit

def function_one():
    return [x * 2 for x in range(1000)]

def function_two():
    return [x + 1 for x in range(1000)]

time_one = timeit.timeit(function_one, number=10000)
time_two = timeit.timeit(function_two, number=10000)

print(f"Waktu function_one: {time_one} detik")
print(f"Waktu function_two: {time_two} detik")
# Fungsi: Membandingkan waktu eksekusi antara dua fungsi yang berbeda.
# Kondisi: Ketika ingin mengetahui fungsi mana yang lebih efisien.