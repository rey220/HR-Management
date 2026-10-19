from src.services.create_data import create
from src.services.show_data import show
from src.resources.database_app import data_storage
import os


def main(data) :
    
    while True :
        
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
    
        try :
            
            print()
            input_user_choice = int(input("Input no tindakan : "))
            
            if input_user_choice == 1 :
                
                create()
            
            elif input_user_choice == 2 :

                show(data)
   
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
    
    data_db = data_storage
    main(data_db)
                