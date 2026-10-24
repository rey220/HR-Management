from tabulate import tabulate
import os

def show(db) :
    
   while True :
       
        os.system("cls" if os.name =="nt" else "clear")  
            
        print("SHOW DATA") 
        print()
        
        print("0. Kembali ke menu utama")
        print("1. Lihat data berdasarkan nama lengkap karyawan")
        print("2. Lihat data berdasarkan keseluruhan")
        print()
        
        try :
            
            input_pilihan = int(input("Pilih No : "))
            
            if input_pilihan == 0 :
                
                return
            
            elif input_pilihan == 1 :
                
                if len(db) == 0 :
                    
                    print("Data tidak tersedia, Silahkan input data terlebih dahulu")
                    input("Tekan enter untuk melanjutkan....")
                    continue
  
                input_nama_karyawan = input("Input nama lengkap karyawan : ").strip()
                
                data = []
                for item in db :
                    
                    if item["name"].strip().casefold() == input_nama_karyawan.casefold() :
                        
                        show_data_table(data,item)   
        
                if len(data) == 0 :
                    
                    print(f"Nama karyawan : {input_nama_karyawan} tidak ada.")
                    
                else :
                    
                    os.system("cls" if os.name =="nt" else "clear")
                    print(tabulate(data,TITLE_ROWS,"fancy_grid"))
                        
                input("Tekan enter untuk melanjutkan...")
                
            elif input_pilihan == 2 :
                
                if len(db) == 0 :
                    
                    print("Data tidak tersedia. Silahkan input data terlebih dahulu")
                    input("Tekan enter untuk melanjutkan...")
                    continue
                
                else :
                    
                    all_data = []
                    
                    for item in db :
                        
                        show_data_table(all_data,item)
                    
                    os.system("cls" if os.name =="nt" else "clear")
                    print(tabulate(all_data,TITLE_ROWS,"fancy_grid"))
                        
                input("Tekan enter untuk melanjutkan...")  
                        
            else : 
                
                print(f"Opsi no {input_pilihan} tidak tersedia. Silahkan input no yang tersedia.")
                input("Tekan enter untuk melanjutkan...")
                
        except ValueError :
        
            print("Input tidak valid! Gunakan bilangan bulat untuk menginput.")                
            input("Tekan enter untuk melanjutkan...")

         
TITLE_ROWS =  ["ID","Nama Karyawan","Status Karyawan","Awal Kontrak","Akhir Kontrak","Role Karyawan","Departement","Gaji"]

def show_data_table(records,items) :
    
    records.append([
        
        items["id"],
        items["name"].capitalize(),
        items["employement_type"].upper(),
        items["contract_start"],
        items["contract_end"],
        items["job_title"].capitalize(),
        items["department"].upper(),
        items["salary"]
        
    ])
    

    

        
                             
            
        
        
        
   
   
        
        
        
    
    