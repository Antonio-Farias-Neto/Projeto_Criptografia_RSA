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

#Blocagem[A]

p = 0
q = 0
while True:
    p = random.randint(1000, 1000000)
    if eh_primo(p):
        break

while True:
    q = random.randint(1000, 1000000)
    if eh_primo(q) and q != p:
        break

n = p*q
y = 3
chavePublica = (n,y)


#Criptografar[A]

#Blocagem[B]

#Descriptografar[B]

#Desblocar[B]

#Conversão de número para Letra[B]


