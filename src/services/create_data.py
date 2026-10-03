from src.validators.input_validators import *
from src.resources.database_app import data_storage
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

def create() :
    
    os.system("cls" if os.name == "nt" else "clear")
    print("MEMBUAT DATA")
    print()
    
    while True :
    
        input_name = input("Input nama karyawan : ")

        if not input_name.strip() :
            
            validators_input_name(input_name)
            continue
        
        else :
            
            break    

    while True :
        
        input_employement_type = input("Input status karyawan (KONTRAK/TETAP) : ")
        
        if not input_employement_type.strip() : 
            
            validator_input_status(input_employement_type)
            continue
        
        else :
            
            break
        
    while True :    
    
        input_contract_start = input("Input awal kontrak (tanggal/bulan/tahun) : ")
        
        if not input_contract_start.strip() :
            
            validator_input_contract_start(input_contract_start)
            continue
            
        else :
            
            break
    
    while True :        
            
        input_contract_end = input("Input akhir kontrak (tanggal/bulan/tahun) : ")
        
        if not input_contract_end.strip() :
            
            validator_input_contract_end(input_contract_end)
            continue
            
        else :
            
            break
        
    while True :
    
        input_job_title = input("Input role karyawan : ")
        
        if not input_job_title.strip() :
            
            validator_input_job(input_job_title)
            continue
            
        else :
            
            break
        
    while True :
        
        input_department = input("Input departement : ")
        
        if not input_department.strip() :
            
            validator_input_department(input_department)
            continue
            
        else :
            
            break
        
    while True :
    
        input_salary_raw = input("Input gaji karyawan : ")

        if not validator_input_salary(input_salary_raw) :
            
            print("Error: Input harus berupa angka bulat saja (tanpa titik/koma/huruf)!")
            input("Tekan enter untuk menginput kembali...")
            continue
        
        input_salary = int(input_salary_raw.strip())
        break
               
    create_data_employees = {
        "id" : generate_employee_id(),
        "name" : input_name,
        "employement_type" : input_employement_type,
        "contract_start" : input_contract_start,
        "contract_end" : input_contract_end,
        "job_title" : input_job_title,
        "department" : input_department,
        "salary" : input_salary
    }
    
    list_for_show_data = []
    
    list_for_show_data.append(create_data_employees)
    table_rows = []    
    for item in list_for_show_data :
        
        table_rows.append([
            item["id"],
            item["name"].capitalize(),
            item["employement_type"].upper(),
            item["contract_start"],
            item["contract_end"],
            item["job_title"].capitalize(),
            item["department"].upper(),
            item["salary"]
            ])
    
    print()   
    title_rows = ["ID","Nama Karyawan","Status Karyawan","Awal Kontrak","Akhir Kontrak","Role Karyawan","Departement","Gaji"]
    os.system("cls" if os.name == "nt" else "clear")
    print(tabulate(table_rows,title_rows,"fancy_grid"))
    
    input_validator_user = input("Apakah data di atas sudah valid ? (Y/N) : ").upper()
    show_message_success(input_validator_user,create_data_employees)

def show_message_success(validator,data) :

    while True :
    
        if validator == "Y" :
            
            os.system("cls" if os.name == "nt" else "clear")
            
            data_storage.append(data)
            data_nums = ["20%","40%","60%","80%","100%"]
            delay_nums =  [1.5,1.5,1.5,1.5,1.5]
            
            for index,value in enumerate(data_nums) :
                
                for second_item in value :
                    
                    print(second_item,end="")
                    sys.stdout.flush()
                    
                time.sleep(delay_nums[index])
                print('')
            
            print("DATA BERHASIL DITAMBAHKAN!!!")
            input("Tekan enter kembali ke menu utama... ")
            return
        
        elif validator == "N" :
            
            print("Silahkan input kembali data dengan benar ")
            continue
        
        else : 
            
            print("Format input tidak valid. Gunakan format teks untuk menginput")
            input("Tekan enter untuk melanjutkan...")
            continue


    
                        
        

        
        
    
    
    
    
    
    
