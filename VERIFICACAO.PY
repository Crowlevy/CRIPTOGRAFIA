import hashlib
import os
'''SISTEMA DE VERIFICAÇÃO DE SENHAS UTILIZANDO O HASH E SALT PASSOWORD, ELE TEM UMA SENHA PRÉ ESTABELECIDA
   DESSA SENHA ELE TIRA O "SALT" DELA E GUARDA, APÓS ISSO É PEDIDO AO USUÁRIO A SENHA E SE COINCIDE COM 
   A QUE ESTÁ ARMAZENADA O SISTEMA PASSA '''

def saltSenha(senha):
    salt = os.urandom(16)
    saltPassword= salt+senha.encode("utf-8")
    sha256= hashlib.sha256()
    sha256.update(saltPassword)
    senhaHash= sha256.hexdigest()
    
    return senhaHash,salt.hex()
def verificarSenha(senha,senhaHash,salt):
    salBytes= bytes.fromhex(salt)
    saltPassword= salBytes+senha.encode("utf-8")
    sha256= hashlib.sha256() 
    sha256.update(saltPassword)
    senhaCompilado = sha256.hexdigest()
    return senhaCompilado == senhaHash

senhaSecreta='testeuiui'
senhaHash,salt=saltSenha(senhaSecreta)
print(f"SENHA ARMAZENADA:{senhaHash}")
print(f"SALT ARMAZENADO:{salt}")

tentativas = 3
while True:
    verificar= input("COLOQUE A SENHA PARA SER VERIFICADA: ")
    if verificarSenha(verificar,senhaHash,salt):
        print("É VÁLIDA")
    else:
        print("INVÁLIDA")
        tentativas-=1
        if tentativas==0:
            print("LIMITE EXCEDIDO, TENTE NOVAMENTE MAIS TARDE")
            break