from src.validators.input_validators import *
from src.validators.input_checker import input_valid
from src.services.show_data import show_data_table
from src.resources.database_app import data_storage
from tabulate import tabulate
import os


TITLE_ROWS = ["ID","Nama Karyawan","Status Karyawan",
              "Awal Kontrak","Akhir Kontrak",
              "Role Karyawan","Departement","Gaji"]

def update(db) :

    if len(db) == 0 :
        
        print("Data tidak tersedia, Silahkan input data terlebih dahulu")
        input("Tekan enter untuk melanjutkan....")
    
    os.system("cls" if os.name=="nt" else "clear")
    print("-"*15,"UPDATE DATA","-"*15)
    print()
    
    while True :
    
        try :

            input_ID = input_valid("Input ID Karyawan : ",validator_input_name,"Kolom input ID tidak boleh kosong!")
            
            data_table = []       
            
            for item in db :
                
                if item["id"] == input_ID.upper().strip() :
                
                    show_data_table(data_table,item)
                    print()
                    print(tabulate(data_table,TITLE_ROWS,"fancy_grid"))
                    print()
                    
                    while True :
                    
                        # os.system("cls" if os.name=="nt" else "clear")
                        print("Update : ")
                        print()
                        print("1. Nama Karyawan")
                        print("2. Status Karyawan")
                        print("3. Awal Kontrak")
                        print("4. Akhir Kontrak")
                        print("5. Role Karyawan")
                        print("6. Departement")
                        print("7. Gaji")
                        print("8. Menu utama")
                        print()
                        
                        try :
                            
                            input_num = int(input("Input No : ").strip())
                            
                            if input_num == 1 :
                                
                                input_nama_update = input_valid("Input Nama Karyawan : ",validator_input_name,"Kolom input nama tidak boleh kosong!")
                                
                                flag_data = False
                                item["name"] = input_nama_update
                                flag_data = True
    
                                if flag_data :
                                    
                                    print()
                                    print("Nama berhasil diperbaharui!")
                                    print()
                                    
                                else :
                                    
                                    print("Nama gagal diperbaharui.")
                            
                            elif input_num == 8 :
                                
                                return    
                                
                        except ValueError :
                            
                            print("Momok")
                    
                
            if len(data_table) == 0 :
                
                print(f"Data dengan ID : {input_ID} tidak ditemukan")
                input("Tekan enter untuk menginput kembali...")
                continue
                
            # else :
                
            #     os.system("cls" if os.name=="nt" else "clear")
            #     print()
            #     print(f"DATA KARYAWAN ID : {input_ID.upper()}")
            #     print()
            #     print(tabulate(data_table,TITLE_ROWS,"fancy_grid"))
            #     print()
                
        except ValueError :
            
            print("Momok")
        

            
        

                   

                
                
                
            
            
            
            
            
    
    
    
    