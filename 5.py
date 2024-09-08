siswa={'a':100,'b':70,'c':85,'d':90,'e':60}
user = input('nama siswa : ').lower()
if user in siswa:
  if siswa[user] >= 70:
    print('selamat anda lulus dengan nilai',siswa[user])
  else:
    print('maaf anda belum lulus')
else :
  print('isi nama yang bener')