awal =int(input("masukan saldo awal : "))
sisa = awal
while(True):
    pengeluaran = int(input("masukan pengeluaran hari ini : "))
    if pengeluaran == -1 :
     print("sisa saldo = ", sisa)
    break
sisa = sisa - pengeluaran
if sisa < 0:
    print("saldo tidak cukup")
    print("sisa saldo", sisa+pengeluaran)
    
