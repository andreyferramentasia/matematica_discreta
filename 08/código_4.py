from math import gcd

#Mensagem precisa ser menor que n: com 11 e 13, n = 143
p = 11
q = 13
n = p*q
fi = (p-1)*(q-1)

e_c = [x for x in range(2, fi) if gcd(x, fi) == 1][0]
d_dc = 1
while (e_c * d_dc) % fi != 1:
    d_dc += 1

tabela = {
    'a':21,
    'b':22,
    'c':23,
    'd':24,
    'e':25,
    'f':26
}
tabela_inversa = {v: k for k, v in tabela.items()}

frase = 'ae'

def frase_to_n(frase):
  return [tabela.get(letra) for letra in frase]

def n_to_frase(numeros):
  return ''.join([tabela_inversa.get(m) for m in numeros])

def criptografar(frase_n):
  lc = [(m**e_c) % n for m in frase_n]
  return lc
def descriptografar(cifra):
  ld = [(c**d_dc) % n for c in cifra]
  return ld

cifra = criptografar(frase_to_n(frase))
print(cifra)
print(descriptografar(cifra))
print(n_to_frase(descriptografar(cifra)))
