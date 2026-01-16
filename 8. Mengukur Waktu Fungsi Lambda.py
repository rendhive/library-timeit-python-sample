import timeit

lambda_function = lambda x: x * 2

execution_time = timeit.timeit(lambda: lambda_function(10), number=10000)
print(f"Waktu eksekusi lambda_function: {execution_time} detik")
# Fungsi: Mengukur waktu untuk menjalankan fungsi lambda.
# Kondisi: Ketika ingin menilai kinerja pemanggilan fungsi lambda.