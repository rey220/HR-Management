from src.services.create_data import create
import os


def main() :
    
    os.system("cls" if os.name == "nt" else "clear")
    
    print()
    print("-"*30,"Selamat Datang di Program : ","-"*30)
    print("-"*33,"Manajemen Karyawan","-"*33)
    print()
    
    print("Fitur yang tersedia : ")
    print()
    print("1. CREATE : Membuat data")
    print("2. READ   : Melihat data")
    print("3. UPDATE : Memperbaharui data")
    print("4. DELETE : Menghapus Data")
    print("5. Keluar Program")
    print()
    
    while True :
        
        try :
            
            print()
            input_user_choice = int(input("Input no tindakan : "))
            
            if input_user_choice == 1 :
                
                create()
                
                main()
                continue
            
            elif input_user_choice == 5 :
                
                os.system("cls" if os.name == "nt" else "clear")
                print("Program dimatikan.")
                exit()
                break
                
        except ValueError :
            
            print()
            print("Format input tidak valid. Gunakan angka untuk menginput.")
            input("Tekan enter untuk menginput kembali...")
            
    
if __name__ == "__main__" :
    
    main()