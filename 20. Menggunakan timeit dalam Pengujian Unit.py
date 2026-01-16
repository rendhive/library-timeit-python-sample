import timeit

def run_tests():
    assert sum(range(100)) == 4950
    assert max(range(100)) == 99

execution_time = timeit.timeit(run_tests, number=10000)
print(f"Waktu eksekusi run_tests: {execution_time} detik")
# Fungsi: Mengukur waktu pengujian fungsi dengan assert statement.
# Kondisi: Ketika Anda ingin mengevaluasi efisiensi dari pengujian unit yang diimplementasikan.