from src.validators.input_validators import *
from src.validators.input_checker import input_valid
from src.services.show_data import show_data_table
from src.helpers.show_helper import *
from tabulate import tabulate
import os
import time
import sys

TITLE_ROWS = ["ID","Nama Karyawan","Status Karyawan",
              "Awal Kontrak","Akhir Kontrak",
              "Role Karyawan","Departement","Gaji"]

def show_record_data(record) :
    
    data_record = []
    
    for i in record :
        
        show_data_table(data_record,i)
    
    print(tabulate(data_record,TITLE_ROWS,"fancy_grid"))    
        

def delete(db) :
    
    if len(db) == 0 :
        
        print()
        print("Data tidak tersedia, Silahkan input data terlebih dahulu")
        input("Tekan enter untuk melanjutkan....")
        return
    
    while True :
        
        os.system("cls" if os.name=="nt" else "clear")
        print("-"*30,"INFORMASI LENGKAP SEMUA KARYAWAN","-"*30)
        print()
        show_record_data(db)
        print()
        input_ID_delete = input_valid("Input ID yang akan dihapus : ",validator_input_name,"Kolom Input ID tidak Boleh Kosong!")
    
        get_data_ID = []
        data_pointer = False
        
        for item in db :
            
            if input_ID_delete.upper() == item["id"].upper() :
                
                data_pointer = True
                show_data_table(get_data_ID,item)
                break
              
        if data_pointer :
            
            os.system("cls" if os.name=="nt" else "clear")
            print(f"{"-"*40} Informasi Lengkap Karyawan ID : {input_ID_delete.upper()} {"-"*40}")
            print()
            print(tabulate(get_data_ID,TITLE_ROWS,"fancy_grid"))
            break
        
        else :    
            
            print()
            print(f"{input_ID_delete.upper()} tidak ditemukan!")
            input("Tekan Enter Untuk Menginput Kembali...")

    print()
    input_decision = input_valid("Apakah Anda Akan Menghapus Data ID Ini ? (Y/N) : ",validator_input_Y_N,"Input Y/N Untuk Melanjutkan\n")

    if input_decision.upper() == "Y" :
        
        for index,item_delete in enumerate(db) :
        
            if item_delete["id"] == input_ID_delete.upper() :
                
                del db[index]
                
                os.system("cls" if os.name=="nt" else "clear")
                data_nums =["20%","40%","60%","80%","100%"]
                delays = [0.3,0.3,0.3,0.3,0.3]
                
                for i,value in enumerate(data_nums) :
                    
                    for second_item in value :
                        
                        print(second_item,end="")
                        sys.stdout.flush()
                        
                    time.sleep(delays[i])
                    print("")
                
                print("")
                print("DATA BERHASIL DIHAPUS!!!")
                print("Lihat Perubahan di Fitur Lihat Data")
                break    
            
        input("Tekan Enter Untuk Kembali ke Menu Utama...")
        
    elif input_decision.upper() == "N" :
    
        input("Tekan Enter Untuk Kembali ke Menu Utama...")
        return
        
    else : 
        
        return None
    
  

    
                    
                
                
                
        
    

       
                    
                        
                        
                                
        
        
            
            
            
            
            
            
            