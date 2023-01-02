#Program perpindahan isi gelas. 
#Gelas A berisi Kopi.
#Gelas B berisi Teh.
#Pindahkan isi gelas A menjadi isi Teh dan gelas B menjadi isi Kopi.
print ( " Program Perpindahan Isi Gelas")
Gelas_A = 'Kopi'
Gelas_B = 'Teh'
print ("Kondisi Isi Gelas Awal")
print(f'Gelas_A={Gelas_A}, Gelas_B={Gelas_B}')
#variabel Gelas C sebagai bantuan.
Gelas_C = Gelas_A

#Proses pertukaran.
Gelas_A = Gelas_B
Gelas_B = Gelas_A
Gelas_B = Gelas_C
print("Kondisi Isi Gelas Akhir")
print(f'Gelas_A={Gelas_A}, Gelas_B={Gelas_B}')