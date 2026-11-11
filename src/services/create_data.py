from src.validators.input_validators import *
from src.validators.input_checker import input_valid
from src.resources.database_app import data_storage
from src.services.show_data import show_data_table
from tabulate import tabulate
import os
import time
import sys


"""
    Fungsi yang digunakan untuk membuat/generate ID unik secara otomatis setiap ada pembuatan data
"""
def make_employee_id(prefix="ID-K",start_num=1) :
    
    num_now = start_num
    
    def generate_text() :
        
        nonlocal num_now
        new_id = f"{prefix}{num_now:03d}"
        num_now += 1
        return new_id
    
    return generate_text

generate_employee_id = make_employee_id()


def input_all_data(*spesification) :
    
    hasil = {}
    
    for key,prompt,validator,err_msg in spesification :
        
        hasil[key] = input_valid(prompt,validator,err_msg)
        
    return hasil

def create() :
    
    while True :
        
        os.system("cls" if os.name == "nt" else "clear")
        print("MEMBUAT DATA")
        print()
        
        data_awal = input_all_data(("name","Input nama karyawan : ",validator_input_name,"Kolom input nama tidak boleh kosong!"),
                                   ("employement_type","Input status karyawan (KONTRAK/TETAP/MAGANG) : ",validator_input_status,"Jenis kepigawaian tidak valid!"))
        
        if data_awal["employement_type"].upper() == "TETAP" :
            
            data_kontrak = {"contract_start" : "-",
                            "contract_end" : "-"}
            
        else :
            
            data_kontrak = input_all_data(("contract_start","Input awal kontrak (tanggal/bulan/tahun) : ",validator_input_contract_start,"Kolom input awal kontrak tidak boleh kosong!"),
                                          ("contract_end","Input akhir kontrak (tanggal/bulan/tahun) : ",validator_input_contract_end,"Kolom input akhir kontrak tidak boleh kosong!"))
                                   
        data_lanjutan = input_all_data(("job_title","Input role karyawan : ",validator_input_job,"Kolom input role tidak boleh kosong!"),
                                       ("department","Input departement : ",validator_input_department,"Kolom input departement tidak boleh kosong!"),
                                       ("salary","Input gaji karyawan : ",validator_input_salary,"Error: Gaji harus berupa angka bulat!"))                                   
                                   
        data_lanjutan["salary"] = int(data_lanjutan["salary"])
        
        create_data_employeed = {"id": generate_employee_id(),
                                **data_awal,
                                **data_kontrak,
                                **data_lanjutan}        
        list_for_show_data = []
        
        list_for_show_data.append(create_data_employeed)
        table_rows = []    
        for item in list_for_show_data :
            
            show_data_table(table_rows,item)    
        
        print()   
        title_rows = ["ID","Nama Karyawan","Status Karyawan","Awal Kontrak","Akhir Kontrak","Role Karyawan","Departement","Gaji"]
        os.system("cls" if os.name == "nt" else "clear")
        print(tabulate(table_rows,title_rows,"fancy_grid"))
        print()
        
        input_validator_user = input_valid("Apakah Anda Akan Menghapus Data ID Ini ? (Y/N) : ",
                                           validator_input_Y_N,
                                           "Input Tidak Valid. Gunakan Y/N Untuk Melanjutkan\n")
            
        if input_validator_user.upper() == "Y" :
            
            show_message_success(input_validator_user,create_data_employeed)
            break
        
        elif input_validator_user.upper() == "N" :
            
            print("Silahkan input data kembali dengan benar")
            input("Tekan enter untuk melanjutkan...")
            
def show_message_success(validator,data) :
    
    if validator.upper() == "Y" :
        
        os.system("cls" if os.name == "nt" else "clear")
        
        data_storage.append(data)
        data_nums = ["20%","40%","60%","80%","100%"]
        delay_nums =  [0.8,0.8,0.8,0.8,0.8]
        
        for index,value in enumerate(data_nums) :
            
            for second_item in value :
                
                print(second_item,end="")
                sys.stdout.flush()
                
            time.sleep(delay_nums[index])
            print('')
        
        print("DATA BERHASIL DITAMBAHKAN!!!")
        input("Tekan enter kembali ke menu utama... ")
     
        


    
                        
        

        
        
    
    
    
    
    
    
