import getpass
import crypter
import os
import sys
from time import sleep
en_a_de=crypter.edcrypter()
class program():
    def encrypt(self,file_name,password):
        with open(file_name,"rb") as file:
            file_text=file.read()
            encrypted=en_a_de.encrypt(file_text,password)
        with open(file_name,"wb") as file:
            file.write(encrypted)
    def decrypt(self,file_name,password):
        with open(file_name,"rb") as file:
            file_text=file.read()
            decrypted=en_a_de.decrypt(file_text,password)
        with open(file_name,"wb") as file:
            file.write(decrypted)
kind=sys.argv[1]
if "-e" in kind:
    path=sys.argv[2]
    passs=getpass.getpass('password:')
    e_dcrypter=program()
    e_dcrypter.encrypt(path,passs)
    if "h" in kind:
        fhname=""
        index=0
        pathlist=path.split("/")
        for i in pathlist:
            index+=1
            if len(pathlist)==index:
                fhname+="."+i
                break
            fhname+=i+r"/"
        os.rename(path,fhname)
        print(f"file path changed to {fhname} and the file was hidden")
elif "-d" in kind:
    file_path=sys.argv[2]
    passs=getpass.getpass('password:')
    e_dcrypter=program()
    e_dcrypter.decrypt(file_path,passs)
    if "-et" in kind:
        sleep_time=int(kind.replace("-et",""))
        sleep(sleep_time)
        e_dcrypter.encrypt(file_path,passs)
