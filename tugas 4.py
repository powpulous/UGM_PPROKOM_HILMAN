banyak_data = int(input("masukan jumlah banyak data : "))
total = 0
for i in range(banyak_data):
    data = float(input(f"Masukkan data ke-{i+1}: ")) 
    total = total + data
rata_rata = total / banyak_data
print("Rata-rata dari", banyak_data ,"data adalah:",rata_rata)