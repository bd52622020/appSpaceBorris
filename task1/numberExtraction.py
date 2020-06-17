import re

file = open("phoneNumbers.txt","r").read()
newfile = open('results.txt',"w")
#edited = re.sub('*', '-', file) 
numbers = re.findall(r'\d{3}[-\.\*\,]\d{3}[-\.\*\,]\d{4}', file)


for number in numbers:
    number = re.sub(r'\D','-',number)
    newfile.write(number)
    newfile.write("\n")
    
newfile.close()



    
    