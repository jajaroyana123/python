banyak_jenis= int(input("Masukan banyak jenis :"))
i = 0
jenis_potong=[]
harga=[]
banyak=[]
jumlah_harga=[]

# input data ayam potong
for i in range(banyak_jenis):
    kode_potong= input("Kode Potong [D/P/S]:")
    if kode_potong == "D" :
        jenis_potong.append("Dada ")
        harga.append(int(2500))
        banyak.append(int(input("Banyak :")))
        jumlah_harga.append( (harga[i]*banyak[i]))
    elif kode_potong == "P" :
        jenis_potong.append("Paha ")
        harga.append(int(2000))
        banyak.append(int(input("Banyak :")))
        jumlah_harga.append( (harga[i]*banyak[i]))
    elif kode_potong == "S" :
        jenis_potong.append("Sayap")
        harga.append(int(2500))
        banyak.append(int(input("Banyak :")))
        jumlah_harga.append( (harga[i]*banyak[i]))
    else :
        jenis_potong.append("Tidak di temukan")
        harga.append(int(0))
        banyak.append(int(input("Banyak :")))
        jumlah_harga.append( (harga[i]*banyak[i]))
    i = i+1

# proses perhitungan jumlah bayar
jumlah_bayar=0
for i in range(banyak_jenis):
    jumlah_bayar=jumlah_bayar+jumlah_harga[i]

# proses perhitungan persentasi pajak & jumlah bayar
pajak=jumlah_bayar*0.1
Total_bayar=jumlah_bayar-pajak

# output
print('-'*60)
print("{:^4}|{:^16}|{:^10}|{:^10}|{:^16}".format('No.','jenis potong','banyak','harga','jumlah harga'))
print('-'*60)
for i in range(banyak_jenis):
    print("{:>3}. {:<16} {:^10} {:^10}  Rp.{:^12}".format((i+1),jenis_potong[i],banyak[i],harga[i],jumlah_harga[i]))
print('-'*60)
print("{:>44}{:<3}{:^12}".format("Jumlah Bayar "," Rp.", jumlah_bayar))
print("{:>44}{:<3}{:^12}".format("Pajak 10% "," Rp.", pajak))
print("{:>44}{:<3}{:^12}".format("Total Bayar "," Rp.", Total_bayar))
print('-'*60)
