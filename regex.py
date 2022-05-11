import re 

def validate(result):
 pattern = re.compile("[A-Z]{2}\d{2}[A-Z]{1}\d{4}")
 if(re.match(pattern,result)):
     return True 
 else:
     return False