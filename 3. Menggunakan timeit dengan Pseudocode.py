import timeit

# Mengukur waktu eksekusi kode dengan context string
execution_time = timeit.timeit("sum(range(100))", number=10000)
print(f"Waktu eksekusi kode: {execution_time} detik")
# Fungsi: Mengukur waktu untuk mengeksekusi kode langsung dalam bentuk string.
# Kondisi: Saat Anda ingin menjalankan snippet cepat tanpa membuat fungsi terpisah.