from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
class edcrypter():
    def password(self,password_p):
        password_provided = password_p
        password = password_provided.encode()
        salt = b'salt_'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(password))
    def encrypt(self,file_text_e,password_e):
        f = Fernet(self.password(password_e))
        token = f.encrypt(file_text_e)
        return token
    def decrypt(self,file_text_d,password_d):
        decrypt=Fernet(self.password(password_d))
        decrypted=decrypt.decrypt(file_text_d)
        return decrypted
