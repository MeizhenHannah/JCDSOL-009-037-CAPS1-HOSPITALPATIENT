### ID STUDENT : JCDSOL-009-037
### Nama : Meizhen Hannah Zahirah



### Data Initialization
Menu = ['1. Informasi Data Pasien',
        '2. Menambahkan Data Pasien',
        '3. Mengubah Data Pasien',
        '4. Menghapus Data Pasien',
        '5. Exit']
Pasien = [{'ID Pasien' : '081A', 'Nama' : 'Shiva', 'Gender' : 'Wanita', 'Telepon' :'909876', 'Kota' : 'Bekasi', 'Pembayaran Pasien' : 'Umum'},
{'ID Pasien' : '082A', 'Nama' : 'Almeraz', 'Gender' : 'Pria', 'Telepon' : '909875','Kota' : 'Bandung', 'Pembayaran Pasien' : 'Asuransi'}]

##### Main Menu
def Main_Menu():
        while True :
                print("\n=======Data Pasien Rumah Sakit Edelweiss=======\n")
                for i in Menu :
                        print (i)
                Opsi = input('Silakan Masukan kode Nomer [1-5]:')
                if Opsi == '1' :
                        Read_Data()
                elif Opsi == '2' :
                        Create_Data()
                elif Opsi == '3' :
                        Update_Data()
                elif Opsi == '4' :
                        Delete_Data()
                elif Opsi == '5' :
                        print('''Terimakasih''')
                        break
                else:
                        print('Maaf, Data yang Dimasukkan Tidak Ada') 



#### Read Data Function
def Read_Data():
        read = True
        while read != '3':
                print("\n++++++Report Data Pasien RS Edelweiss+++++\n")
                print("1. Informasi Seluruh Data Pasien")
                print("2. Informasi Data Tertentu")
                print("3. Kembali Ke Menu Utama")
                read = input("Silakan Pilih Sub Menu Read Data [1-3] : ")
                if read == '1':
                        if len(Pasien) != 0 :
                                print('Informasi Seluruh Data Pasien')
                                for i, value in enumerate(Pasien) :
                                        print(f"{i+1}.ID Pasien :{value['ID Pasien']},Nama : {value['Nama']}, Gender : {value['Gender']}, Telepon : {value['Telepon']}, Kota : {value['Kota']}, Pembayaran Pasien : {value['Pembayaran Pasien']}")
                        else :
                                print('Maaf, Tidak Ada Data')
                        continue
                elif read == '2':
                        if len(Pasien) != 0 :
                                PrimaryKey= input('Masukkan Primary ID :')
                                for i, value in enumerate(Pasien) :
                                        if PrimaryKey == value['ID Pasien']:
                                                print(f"{i+1}.ID Pasien :{value['ID Pasien']},Nama : {value['Nama']}, Gender : {value['Gender']}, Telepon : {value['Telepon']}, Kota : {value['Kota']}, Pembayaran Pasien : {value['Pembayaran Pasien']}")
                                                break
                                        elif i == len(Pasien) -1:
                                                print("Maaf,Tidak Ada Data")
                        else :
                                print('Maaf, Tidak Ada Data')
                        continue
                elif read == '3':
                        Main_Menu ()

#### Create Data Function
def Create_Data():
        create = True
        while create != '2':
                print("\n++++++Create Data Pasien RS Edelweiss+++++\n")
                print("1.Tambah Data Pasien")
                print("2.Kembali ke Menu Utama")
                create = input("Silakan Pilih Sub Menu Create Data [1-2] :")
                if create == '1':
                        if len(Pasien) != 0 :
                                PrimaryKey= input('Masukkan Primary ID :')
                                for i, value in enumerate(Pasien) :
                                        if PrimaryKey == value['ID Pasien']:
                                                print('Sudah Ada Data')
                                                break
                                else :
                                        Namabaru = input('Masukan Input Pasien Baru:')
                                        Genderbaru = input('Masukan Input Gender Baru:')
                                        Teleponbaru = input('Masukan Input Telepon Baru:')
                                        Kotabaru = input('Masukan Input Kota Baru:')
                                        Pembayaranbaru = input('Masukan Input Pembayaran Baru:')
                                        while True :
                                                savedata = input('Apakah Data akan Disimpan? (Y/N):')
                                                if savedata == 'Y' :
                                                        Pasien.append({'ID Pasien':PrimaryKey,'Nama':Namabaru,'Gender':Genderbaru,'Telepon':Teleponbaru,'Kota':Kotabaru,'Pembayaran Pasien':Pembayaranbaru})
                                                        print('Data Sudah Tersimpan')
                                                        break
                                                elif savedata == 'N':
                                                        break
                elif create == '2':
                        Main_Menu()

#### Update Data Function
def Update_Data():
        update = True
        while update != '2':
                print("\n++++++Update Data Pasien RS Edelweiss+++++\n")
                print("1.Update Data Pasien")
                print("2.Kembali ke Menu Utama")
                update = input("Silakan Pilih Sub Menu Update Data [1-2] :")
                if update == '1':
                        PrimaryKey= input('Masukkan Primary ID :')
                        for i, value in enumerate(Pasien) :
                                if PrimaryKey == value ['ID Pasien']:
                                        print(f"{i+1}.ID Pasien :{value['ID Pasien']},Nama : {value['Nama']}, Gender : {value['Gender']}, Telepon : {value['Telepon']}, Kota : {value['Kota']}, Pembayaran Pasien : {value['Pembayaran Pasien']}")
                                        while True :
                                                updatestatus = input('Apakah Lanjut Update? (Y/N)')
                                                if updatestatus == 'Y' :
                                                        updatekolom = input('Masukkan Kolom yang Akan Diupdate (ID Pasien/Nama/Gender/Telepon/Kota/Pembayaran Pasien):')
                                                        updatevalue = input('Masukkan Nilai Baru : ')
                                                        while True:
                                                                updatefix = input('Apakah Data Akan Di Update? (Y/N)')
                                                                if updatefix == 'Y':
                                                                        Pasien[i].update({updatekolom : updatevalue})
                                                                        print('Data Sudah Terupdate')
                                                                        break
                                                                elif updatefix == 'N':
                                                                       break
                                                        break
                                                elif updatestatus == 'N':
                                                        print('Data Tidak Terupdate')
                                                        break
                                        break
                                else:
                                        continue                     
                        else :
                                print('Data yang Anda Cari Tidak Ada')
                elif update == '2':
                        Main_Menu()

#### Delete Data Function
def Delete_Data():
        delete = True
        while delete != '2':
                print("\n++++++Delete Data Pasien RS Edelweiss+++++\n")
                print("1.Delete Data Pasien")
                print("2.Kembali ke Menu Utama")
                delete = input("Silakan Pilih Sub Menu Delete Data [1-2] :")
                if delete == '1':
                        PrimaryKey= input('Masukkan Primary ID :')
                        for i, value in enumerate(Pasien) :
                                if PrimaryKey == value ['ID Pasien']:
                                        print(f"{i+1}.ID Pasien :{value['ID Pasien']},Nama : {value['Nama']}, Gender : {value['Gender']}, Telepon : {value['Telepon']}, Kota : {value['Kota']}, Pembayaran Pasien : {value['Pembayaran Pasien']}")
                                        while True :
                                                deletestatus = input('Apakah Lanjut Delete Data? (Y/N)')
                                                if deletestatus == 'Y' :
                                                        Pasien.pop(i)
                                                        print('Data Deleted')
                                                        break
                                                elif deletestatus == 'N' :
                                                        print('Data Tidak Di Delete')
                                                        break
                                        break
                                else:
                                        continue
                        else:
                                print('Data yang Anda Cari Tidak Ada')                             
                elif delete == '2':
                        Main_Menu() 
Main_Menu() #Untuk menjalankan fungsi Menu
