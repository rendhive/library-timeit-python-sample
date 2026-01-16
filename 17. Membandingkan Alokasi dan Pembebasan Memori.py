import timeit

def allocate_list():
    return [0] * 1000

execution_time = timeit.timeit(allocate_list, number=10000)
print(f"Waktu eksekusi alokasi list: {execution_time} detik")
# Fungsi: Mengukur waktu yang diperlukan untuk mengalokasikan larik.
# Kondisi: Saat Anda ingin menganalisis pengeluaran memori dalam aplikasi.