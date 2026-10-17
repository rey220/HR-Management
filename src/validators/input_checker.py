def input_valid(prompt,validator,error_msg) :
    
    while True :
        
        prompt_value = input(prompt)
        
        if validator(prompt_value) :
            
            return prompt_value.strip()
        
        print(error_msg)
        input("Tekan enter untuk menginput kembali...")