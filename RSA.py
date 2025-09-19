import random

def eh_primo(num):
    if num % 2 == 0:
        return False
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True


#Opção[A - Criptografar mensagem/ B - Descriptografar mensagem]

mensagem = input("Mensagem: ")
novamsg = ""

for crp in mensagem:
    novamsg += (ord(crp))


#conversão de letra para número[A]
mensagem = input("Mensagem: ")
novamsg = ""

for crp in mensagem:
    novamsg += str(ord(crp))

#Blocagem[A]

p = 0
q = 0
while True:
    p = random.randint(1000, 100000)
    if eh_primo(p):
        break

while True:
    q = random.randint(1000, 100000)
    if eh_primo(q) and q != p:
        break
        
n = p*q
y = 3       #chavePublica = (n,y)

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
print(n)          
print(novamsg)
print(blocosASeremCriptografados)

#Criptografar[A]
blocosCriptografados = []
for bloco in blocosASeremCriptografados:
    blocosCriptografados.append((int(bloco)**y) % n)

#Blocagem[B]

#Descriptografar[B]

#Desblocar[B]

#Conversão de número para Letra[B]
