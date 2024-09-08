#tugas tambahan : buat program batu gunting kertas
import random

anda = input('pilih satu :batu, gunting, kertas : ').lower()
komputer = random.choice(['batu','gunting','kertas'])
print('\nanda memilih',anda,'\nkomputer memilih',komputer)
if anda == 'batu' and komputer == 'kertas' :
    print('anda kalah')
elif anda == 'gunting' and komputer== 'batu':
    print ('anda kalah')
elif anda == 'kertas' and komputer == 'gunting':
    print ('anda kalah')
elif anda == 'batu' and komputer == 'gunting':
    print ('anda menang')
elif anda == 'gunting' and komputer == 'kertas':
    print ('anda menang')
elif anda == 'kertas' and komputer == 'batu':
    print ('anda menang')
elif anda == 'kertas' and komputer == 'kertas':
    print ('imbang')
elif anda == 'batu' and komputer == 'batu':
    print ('imbang')
elif anda == 'gunting' and komputer == 'gunting':
    print ('imbang')
else :
    print ('error! pilih opsi yang benar')