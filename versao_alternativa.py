import random
import math

def eh_coprimo(a, b):
    return math.gcd(a, b) == 1

def eh_primo(num):
    if num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True

#Opção[A - Criptografar mensagem/ B - Descriptografar mensagem]

#conversão de letra para número[A]
mensagem = input("Mensagem: ")

# Em vez de uma string gigante, vamos processar caractere por caractere
caracteres_para_criptografar = []
for crp in mensagem:
    caracteres_para_criptografar.append(ord(crp))

print("códigos dos caracteres:", caracteres_para_criptografar)

#Blocagem[A]
p = 0
q = 0
while True:
    p = random.randint(100, 1000)
    if eh_primo(p):
        break

while True:
    q = random.randint(100, 1000)
    if eh_primo(q) and q != p:
        break
        
n = p*q

#Gerando y
m = (p-1)*(q-1)
for candidato in range(3, 10):
    if eh_coprimo(candidato, m):
        y = candidato
        break
else:
    for candidato in range(3, m, 2):  # Testa todos os ímpares a partir de 3
        if eh_coprimo(candidato, m):
            y = candidato
            break

print("m: "+ str(m), "\ny:"+ str(y))
print("n:" + str(n))
#chavePublica = (n,y)

# Agora cada "bloco" é simplesmente um código de caractere
blocosASeremCriptografados = caracteres_para_criptografar
print("caracteres como números: " + str(blocosASeremCriptografados))

#Criptografar[A]
blocosCriptografados = []
for bloco in blocosASeremCriptografados:
    blocosCriptografados.append((int(bloco)**y) % n)

print("códigos criptografados: " + str(blocosCriptografados))
#Blocagem[B]

#Descriptografar[B]
d = pow(y, -1, m)  #chavePrivada = (n,d)
print("d: "+ str(d))
blocosDescriptografados = []
for bloco in blocosCriptografados:
    blocosDescriptografados.append((int(bloco)**d) % n)
print("códigos descriptografados: " + str(blocosDescriptografados))

#Conversão de número para Letra[B]
msgfinal = ""
for codigo in blocosDescriptografados:
    try:
        msgfinal += chr(int(codigo))
    except (ValueError, OverflowError):
        msgfinal += "?"

print("mensagem final: " + msgfinal)

# Verificação
print("\nVerificação:")
print("Original:", mensagem)
print("Final:   ", msgfinal)
print("Iguais:  ", mensagem == msgfinal)