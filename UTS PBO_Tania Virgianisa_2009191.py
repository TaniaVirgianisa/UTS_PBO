print('Selamat Datang di Aplikasi Pencatatan Uang Digital') 
restart=('Y')
chances = 3 
saldo = 2500.67
while chances >= 0:
    pin = int(input( 'Masukan 6 Digit Pin Anda: '))
    if pin == (654321): 
        print('Anda Memasukan PIN dengan benar')
        print('Silahkan Tekan 1 Untuk Informasi Saldo Anda')
        print('Silahkan Tekan 2 Untuk Transaksi Penarikan Uang') 
        print('Silahkan Tekan 3 Untuk Transaksi Mengisi Saldo')
        print('Silahkan Tekan 4 Untuk Mengambil Kartu')
        while restart not in ('n', 'TIDAK', 'tidak', 'N'): 
            option = int(input('Apa transaksi yang ingin Anda Pilih?: ')) 
            if option == 1:
                print('Saldo Anda adalah Rp',saldo)
                restart=input('Apakah Anda ingin Kembali? ')
                if restart in ('n', 'TIDAK', 'tidak', 'N' ):
                    print('Terima Kasih')
                    break 
                elif option == 2:
                    option2= ('y') 
                    penarikan = float(input('Berapa banyak yang ingin Anda tarik? 10,20,40,60,80,100 for other enter 1: '))
                    if penarikan in [10, 20, 40, 60, 80, 100]: 
                        saldo = saldo - penarikan 
                        print('\nSaldo Anda Sekarang Rp',saldo) 
                        restart = input('Apakah Anda ingin kembali?')
                        if restart in ('n', 'TIDAK', 'tidak', 'N'): 
                            print('Terima Kasih')
                            break 
                        elif penarikan != [10, 20, 40, 60, 80, 100]:
                            print('Jumlah Tidak Valid, Silahkan Coba Lagi\n') 
                            restart = ('y')
                        elif penarikan == 1: 
                                penarikan= float(input('Silahkan Masukan Jumlah yang Diinginkan: '))
                                
                        elif option == 3:
                            pemasukan = float(input('Berapa Jumlah Uang yang ingin Anda Masukan?'))
                            saldo= saldo + pemasukan
                            print ('\nSaldo Anda sekarang Rp',saldo) 
                            restart=input('Apakah Anda ingin kembali?')
                            if restart in ('n', 'TIDAK', 'tidak', 'N'): 
                                print('Terima Kasih')
                                break
                            elif option == 4:
                                print( 'Mohon tunggu sebentar kartu anda akan dikeluarkan...\n')
                                print('Terima Kasih Telah Melakukan Transaksi')
                                break
                            else:
                                print('Masukan nomor yang benar. \n')
                                restart = ('y') 
                    elif pin != ('654321'): 
                                    print('Pin Anda Salah')
                                    chances = chances - 1 
                                    if chances == 0:
                                        print('\nTidak dapat mencoba lagi')
                                        break