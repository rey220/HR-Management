def validators_input_name(name) : 
    
    if not name.strip()  :
        
        print("Kolom input nama tidak boleh kosong!")
        input("Tekan enter untuk menginput kembali...")    

def validator_input_status(status)     :
        
    if status not in ["kontrak","tetap"] :
        
        print("Jenis kepigawaian tidak valid.")
        input("Tekan enter untuk menginput kembali...")
            
def validator_input_contract_start(contract_start) :
    
    if not contract_start.strip() :
        
        print("Kolom input kontrak tidak boleh kosong!")
        input("Tekan enter untuk menginput kembali...")
    
def validator_input_contract_end(contract_end) :
    
    if not contract_end.strip() :
        
        print("Kolom input kontrak tidak boleh kosong!")
        input("Tekan enter untuk menginput kembali...")
    
def validator_input_job(role) :
    
    if not role.strip() :
        
        print("Kolom input role tidak boleh kosong!")
        input("Tekan enter untuk menginput kembali...")
    
def validator_input_department(department) :

    if not department.strip() :
        
        print("Kolom input department tidak boleh kosong!")
        input("Tekan enter untuk menginput kembali...")
    
def validator_input_salary(salary) :

    if not salary.strip() :
        
        print("Kolom input gaji tidak boleh kosong!")
        input("Tekan enter untuk menginput kembali...")