import timeit

setup_code = '''
import math
def calculate():
    return [math.sqrt(i) for i in range(100)]
'''

execution_time = timeit.timeit("calculate()", setup=setup_code, number=10000)
print(f"Waktu eksekusi calculate(): {execution_time} detik")
# Fungsi: Mengukur waktu eksekusi kode yang didefinisikan dalam blok setup.
# Kondisi: Ketika Anda ingin menyediakan setup environment untuk pengujian.