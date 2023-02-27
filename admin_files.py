import os

path_transfer = os.getcwd()+'/transfer-files/transfer-files.py'

def clearScr():
    os.system('clear')
    
clearScr():
  
apache_ip = input("""

                  Introduzca su IP
                  
                  >  """)

with open(""+ path_transfer +", "rt")as f:
    x = f.read()

with open(""+ path_transfer +", "wt")
  x = x.replace("apache_ip", ""+ apache_ip +"")
  f.write(x)
                  
          
os.system('start service apache2')
os.system('cp "+ path_transfer +" " /var/www/html/"')

         
              
