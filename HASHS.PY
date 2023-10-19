import hashlib 

def converteHash(text):
    sha256= hashlib.sha256()
    sha256.update(text.encode("utf-8"))
    return sha256.hexdigest()

userText= input("COLOQUE UM TEXTO PARA SER CRIPTOGRAFADO: ")
hashText= converteHash(userText)
print(f"SEU TEXTO CRIPTOGRAFO:{hashText}")