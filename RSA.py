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

# Geração de chaves RSA [A]

# Geração do número primo P
p = 0
while True:
    p = random.randint(100, 1000)
    if eh_primo(p):
        break

# Geração do número primo Q
q = 0
while True:
    q = random.randint(100, 1000)
    if eh_primo(q) and q != p:
        break

# Cálculo de N
n = p * q

# Gerando expoente público Y
"""
Gera um y que seja coprimo de m. Para deixar o código mais otimizado, tentei
pegar o menor y possível entre 3 e 9. Se não achar, vai para o próximo impar
até achar.
"""
m = (p-1) * (q-1)
for candidato in range(3, 10):
    if eh_coprimo(candidato, m):
        y = candidato
        break
    else:
        for candidato in range(9, m, 2):  
            if eh_coprimo(candidato, m):
                y = candidato
                break

print("p: " + str(p))
print("q: " + str(q))
print("n:" + str(n))
print("m: " + str(m))
print("y: " + str(y))
#chavePublica = (n,y)


# Blocagem [A]
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

print("mensagem em Unicode: " + novamsg)
print("em blocos: " + str(blocosASeremCriptografados))

# Criptografar [A]
blocosCriptografados = []
for bloco in blocosASeremCriptografados:
    blocosCriptografados.append((int(bloco)**y) % n)

print("blocos criptografados: " + str(blocosCriptografados))


# PARTE B - DESCRIPTOGRAFAR MENSAGEM

# Geração da chave privada [B]
"""
A função pow(y, -1, m) calcula o inverso modular de y módulo
m, ou seja, encontra d tal que (y*d) % m == 1
"""
d = pow(y, -1, m)  #chavePrivada = (n,d)
print("d: " + str(d))


# Descriptografar [B]
"""
Aplica-se a formula pra descriptografar os blocos
"""
blocosDescriptografados = []
for bloco in blocosCriptografados:
    blocosDescriptografados.append((int(bloco)**d) % n)

print("blocos descriptografados: " + str(blocosDescriptografados))


# Reorganiza os blocos já descriptografados em uma única mensagem[B]
msgDescriptografada = ""
for bloco in blocosDescriptografados:
    msgDescriptografada += str(bloco)
    #msgDescriptografada = chr(msgDescriptografada)
print("mensagem descriptografada: " + msgDescriptografada)

# Conversão final para caracteres
"""
Em blocos de 2 caracteres, converte cada bloco para o caractere correspondente
"""
msgfinal = ""
for num in range(0, len(msgDescriptografada), 2):
    num = msgDescriptografada[num:num+2]
    msgfinal += chr(int(num))

print("mensagem final: " + msgfinal)