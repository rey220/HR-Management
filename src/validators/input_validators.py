def validator_input_name(name) : 
    
    return bool(name.strip())
    
def validator_input_status(status)     :
        
    return status.strip().upper() in ["KONTRAK","TETAP","MAGANG"]
            
def validator_input_contract_start(contract_start) :
    
   return bool(contract_start.strip())
    
def validator_input_contract_end(contract_end) :
    
    return bool(contract_end.strip())
    
def validator_input_job(role) :
    
    return bool(role.strip())
    
def validator_input_department(department) :

    return bool(department.strip())
        
def validator_input_salary(salary_raw) :
    
    text = salary_raw.strip()
    
    if not text :
        
        return False
    
    if not text.isdigit() :
        
        return False
    
    return True

    