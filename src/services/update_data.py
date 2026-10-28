from src.validators.input_validators import *
from src.validators.input_checker import input_valid
from src.services.show_data import show_data_table
from tabulate import tabulate
import os


TITLE_ROWS = ["ID","Nama Karyawan","Status Karyawan",
              "Awal Kontrak","Akhir Kontrak",
              "Role Karyawan","Departement","Gaji"]

def update(db) :

    if len(db) == 0 :
        
        print("Data tidak tersedia, Silahkan input data terlebih dahulu")
        input("Tekan enter untuk melanjutkan....")
        return
    
    while True :
        
        os.system("cls" if os.name=="nt" else "clear")
        print("-"*15,"UPDATE DATA","-"*15)
        print()

        input_ID = input_valid("Input ID Karyawan : ",validator_input_name,"Kolom input ID tidak boleh kosong!")
        
        for item in db :
            
            if input_ID.upper() in item["id"] :

                while True :

                    os.system("cls" if os.name=="nt" else "clear")
                    data_table =[]
                    show_data_table(data_table,item)
                    print()
                    print(f" INFORMASI DATA ID : {input_ID.upper()} ")                
                    print()
                    print(tabulate(data_table,TITLE_ROWS,"fancy_grid"))
                    print()
                    
                    menu_update = [[1,"Nama Karyawan"],
                                   [2,"Status Karyawan"],
                                   [3,"Awal Kontrak"],
                                   [4,"Akhir Kontrak"],
                                   [5,"Role Karyawan"],
                                   [6,"Departement"],
                                   [7,"Gaji"],
                                   [8,"Menu Utama"]
                                   ]
                    menu_header = ["No","Pilihan Update"]
                    print(tabulate(menu_update,menu_header,"fancy_grid"))
                    print()
                    
                    try :
                        
                        choose_option_num = int(input("Input No : ").strip())
                        
                        if choose_option_num == 1 :
                            
                            update_input_name = input_valid("Input Nama Lengkap Karyawan : ",validator_input_name,"Kolom input tidak boleh kosong!")
                            
                            data_flag = False
                            item["name"] = update_input_name
                            data_flag = True
                            
                            if data_flag :
                                
                                print()    
                                print("Nama berhasil diperbaharui")
                                input("Tekan enter untuk melanjutkan...")
                                continue
                                
                            else :
                                
                                print()    
                                print("Nama gagal diperbaharui")
                                input("Tekan enter untuk melanjutkan...")
                                continue
                            
                        elif choose_option_num == 8 :
                            
                            return
                        
                    except ValueError :
                        
                        print("Input tidak valid. Gunakan angka/bilangan bulat untuk menginput")
                        input("Tekan enter untuk melanjutkan")

            else :
                
                print(f"{input_ID.upper()} tidak ditemukan!")
                input("Tekan enter untuk kembali ke menu utama...")

        

            
        

                   

                
                
                
            
            
            
            
            
    
    
    
    