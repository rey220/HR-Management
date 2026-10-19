from tabulate import tabulate
import os

def show(db) :
    
   while True :
            
        os.system("cls" if os.name =="nt" else "clear")  
        print("SHOW DATA") 
        print()
        
        print("1. Lihat data berdasarkan nama lengkap karyawan")
        print("2. Lihat data berdasarkan keseluruhan")
        print()
        
        try :
            
            input_pilihan = int(input("Pilih No : "))
            
            if input_pilihan == 1 :
                
                if len(db) == 0 :
                    
                    print("Data tidak tersedia, Silahkan input data terlebih dahulu")
                    input("Tekan enter untuk melanjutkan....")
                    return
                
                else :
                    
                    input_nama_karyawan = input("Input nama lengkap karyawan : ")
                    
                    data = []
     
                    for item in db :
                        
                        if item["name"] == input_nama_karyawan :
                            
                            data.append([
                                item["id"],
                                item["name"],
                                item["employement_type"],
                                item["contract_start"],
                                item["contract_end"],
                                item["job_title"],
                                item["department"],
                                item["salary"]
                            ])
                        
                        title_rows = ["ID","Nama Karyawan","Status Karyawan","Awal Kontrak","Akhir Kontrak","Role Karyawan","Departement","Gaji"]
                        print(tabulate(data,title_rows,"fancy_grid"))
                        
        except ValueError :
            
            print("Input tidak valid! Gunakan bilangan bulat untuk menginput.")                
            input("Tekan enter untuk melanjutkan...")

                
               
                    
                
            
        
        
        
   
   
        
        
        
    
    