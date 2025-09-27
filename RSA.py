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
novamsg = ""

for crp in mensagem:
    novamsg += str(ord(crp))


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
#chavePublica = (n,y)

blocosASeremCriptografados = []
i = 0
while i < len(novamsg):
    for j in range(len(novamsg), i, -1):
        bloco = novamsg[i:j]
        if int(bloco) < n:
            blocosASeremCriptografados.append(bloco)
            i = j
            break
    else:
        blocosASeremCriptografados.append(novamsg[i])
        i += 1
print("n:" + str(n))          
print("mensagem: " + novamsg)
print("em blocos: " + str(blocosASeremCriptografados))

#Criptografar[A]
blocosCriptografados = []
for bloco in blocosASeremCriptografados:
    blocosCriptografados.append((int(bloco)**y) % n)

print("blocos criptografados: " + str(blocosCriptografados))
#Blocagem[B]

#Descriptografar[B]

d = pow(y, -1, m)  #chavePrivada = (n,d)
print("d: "+ str(d))
blocosDescriptografados = []
for bloco in blocosCriptografados:
    blocosDescriptografados.append((int(bloco)**d) % n)
print("blocos descriptografados: " + str(blocosDescriptografados))

#Conversão de número para Letra[B]
msgDescriptografada = ""
for bloco in blocosDescriptografados:
    msgDescriptografada += str(bloco)
    #msgDescriptografada = chr(msgDescriptografada)

print("mensagem descriptografada: " + msgDescriptografada)
msgfinal = ""
for num in range(0, len(msgDescriptografada), 2):
    num = msgDescriptografada[num:num+2]
    msgfinal += chr(int(num))
print("mensagem final: " + msgfinal)




