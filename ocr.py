import easyocr
import os
import remove
from insert import insert
import find_date 
import regex

class ocr:

    def image_to_text():
     try:

        reader = easyocr.Reader(['en'])

        # result = reader.readtext("crop/crop.jpg",paragraph="False")
        result = reader.readtext("crop4.jpg",paragraph="True")
        print(result[0][1])
        # Write-Overwrites
        file1 = open("ocr.txt","w")#write mode
        file1.write(f"{result[0][1]} \n")
        file1.close()
        result =  result[0][1].replace(" ", "")
        date,time  = find_date.date_time()
        remove.remove()
        if(regex.validate(result)):
            insert.connect_insert("sqlite/data.db",result,date,time)
            return result
        
       
     
     except Exception as e:
         print(e)



