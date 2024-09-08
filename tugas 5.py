n = 100000
a = 60*60*24
hari = n // a
b = a*hari
c = n-b
z = 60*60
jam = c // z
d = jam*z
e = c - d
menit = e // 60
detik = n % 60
print(hari,"hari")
print(jam,"jam")
print(menit,"menit")
print(detik,"detik")