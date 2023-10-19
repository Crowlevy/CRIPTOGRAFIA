import hashlib
import os

def passwordSalt(senha):
    salt = os.urandom(16)
    saltSenha = salt + senha.encode('utf-8')
    sha256=hashlib.sha256()
    sha256.update(saltSenha)
    senhaHash=sha256.hexdigest()
    
    return senhaHash,salt.hex()

userSenha = input("COLOQUE A SENHA: ")
senhaHash,salt= passwordSalt(userSenha)
print(f"SUA SENHA:{senhaHash}")
print(f"O SALT DELA:{salt}")
