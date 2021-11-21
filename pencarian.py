myList = [1,5,10,15,20,25,30,2,6,8,9] # Example List
cari = int(input("Masukkan Angka Yang Anda Cari : ")) # angka yang ingin dicari

#fungsi
def searchNumber(List,search):
    counter = 0
    while counter != len(myList):
        if myList[counter] == search:
            result = counter
        counter += 1
    return result

#pemangilan Fungsi
hasil = searchNumber(myList,cari)
if cari not in myList:
    print("Number Not Found !!!")
else:
    print('Number %s in index %s'% (cari,hasil))
