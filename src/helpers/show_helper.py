from src.validators.input_validators import *
from src.validators.input_checker import input_valid
from src.validators.validator_update_feature import *

def print_ID_unavailable(input_id,data) :
    
    if input_id != data["id"] :
        
        print()
        print()
        print(f"{input_id.upper()} tidak ditemukan!")
        input("Tekan enter untuk kembali ke menu utama...")
        
def update_name(input_num,data) :
    
    if input_num == 1 :
        
        update_name = input_valid("Input Nama Lengkap Karyawan : ",validator_input_name,"Kolom input tidak boleh kosong!").capitalize()                      
        data_pointer = False
        data["name"] = update_name
        
        data_pointer = True
        print_data_name_update(data_pointer)
        
def update_contract_status(input_num,data) :
    
    if input_num == 2 :
        
        update_contract_status = input_valid("Input status karyawan (KONTRAK/TETAP/MAGANG) : ",validator_input_status,"Jenis kepigawaian tidak valid!")
        
        if update_contract_status.upper() == "KONTRAK" :
            
            update_contract_start = input_valid("Input awal kontrak (tanggal/bulan/tahun) : ",validator_input_contract_start,"Kolom input awal kontrak tidak boleh kosong!")
            update_contract_end = input_valid("Input akhir kontrak (tanggal/bulan/tahun) : ",validator_input_contract_end,"Kolom input awal kontrak tidak boleh kosong!") 
            
            data_pointer = False
            data["employement_type"] = update_contract_status
            data["contract_start"] = update_contract_start
            data["contract_end"] = update_contract_end
            
            data_pointer = True
            print_data_contract_status_update(data_pointer)
        
        elif update_contract_status.upper() == "MAGANG" :
            
            update_contract_start = input_valid("Input awal kontrak (tanggal/bulan/tahun) : ",validator_input_contract_start,"Kolom input awal kontrak tidak boleh kosong!")
            update_contract_end = input_valid("Input akhir kontrak (tanggal/bulan/tahun) : ",validator_input_contract_end,"Kolom input awal kontrak tidak boleh kosong!") 
            
            data_pointer = False
            data["employement_type"] = update_contract_status
            data["contract_start"] = update_contract_start
            data["contract_end"] = update_contract_end
            
            data_pointer = True
            print_data_contract_status_update(data_pointer)

        elif update_contract_status.upper() == "TETAP" :
            
            data_pointer = False
            data["employement_type"] = update_contract_status
            data["contract_start"] = "-"
            data["contract_end"] = "-"
            
            data_pointer = True
            print_data_contract_status_update(data_pointer)

def update_contract_start(input_num,data) :
    
    if input_num == 3 :
        
        update_new_contract_start = input_valid("Input awal kontrak (tanggal/bulan/tahun) : ",validator_input_contract_start,"Kolom input awal kontrak tidak boleh kosong!")
        data_pointer = False
        data["contract_start"] = update_new_contract_start            
        
        data_pointer = True
        print_new_contract_start(data_pointer)
               
def update_contract_end(input_num,data) :
    
    if input_num == 4 :
        
        update_new_contract_end = input_valid("Input akhir kontrak (tanggal/bulan/tahun) : ",validator_input_contract_end,"Kolom input akhir kontrak tidak boleh kosong!")
        data_pointer = False
        data["contract_end"] = update_new_contract_end            
        
        data_pointer = True
        print_new_contract_end(data_pointer)
        
def update_role_status(input_num,data) :
    
    if input_num == 5 :
        
        update_new_role = input_valid("Input role karyawan : ",validator_input_job,"Kolom input role tidak boleh kosong!").capitalize()
        data_pointer = False
        data["job_title"] = update_new_role
        
        data_pointer = True
        print_new_employee_role(data_pointer)
        
def update_division(input_num,data) :
    
    if input_num == 6 :
        
        update_new_division = input_valid("Input departement : ",validator_input_department,"Kolom input departement tidak boleh kosong!").capitalize()
        data_pointer = False
        data["department"]  = update_new_division
        
        data_pointer = True
        print_new_employee_division(data_pointer)
        
def update_salary(input_num,data) :
    
    if input_num == 7 :
        
        update_salary = input_valid("Input gaji karyawan : ",validator_input_salary,"Error: Gaji harus berupa angka bulat!")
        new_salary = int(update_salary)
        data_pointer = False
        
        data["salary"] = new_salary
        data_pointer = True
        print_new_employee_salary(data_pointer)
        

            