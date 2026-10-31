from src.validators.input_validators import *
from src.validators.input_checker import input_valid
from src.services.show_data import show_data_table
from src.helpers.show_helper import *
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
            
            if input_ID.upper() == item["id"] :

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
                    print()
                    print()
                    print(f"|{"-"*120}|")
                    print()
                    print()
                    print(tabulate(menu_update,menu_header,"fancy_grid"))
                    print()
                    
                    try :
                        
                        choose_option_num = int(input("Input No : ").strip())
                        
                        update_name(choose_option_num,item)
                        update_contract_status(choose_option_num,item)
                        update_contract_start(choose_option_num,item)
                        update_contract_end(choose_option_num,item)
                        update_role_status(choose_option_num,item)
                        update_division(choose_option_num,item)
                        update_salary(choose_option_num,item)
 
                        if choose_option_num == 8 :
                            
                            return
                        
                    except ValueError :
                        
                        print("Input tidak valid. Gunakan angka/bilangan bulat untuk menginput")
                        input("Tekan enter untuk melanjutkan")

        print_ID_unavailable(input_ID,item)
        return
  

            
        

                   

                
                
                
            
            
            
            
            
    
    
    
    