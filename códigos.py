# 1. Conjectura, contraexemplo e prova

# %%

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# %%
resultado = 1

for i in range(1, 4):
    resultado = resultado * i
print(resultado)
# %%

def fatorial(n):
    resultado = 1
    for i in range(1,n+1):
        resultado = resultado * i
    return resultado

def potencia (n):
    return n**2

# %%

for n in range(10):

    print(fatorial(n), potencia(n))

# %%
# 2. Demonstração por exaustão

for n in range(1, 20 + 1):
    print(n)


# %%
for n in range(1, 200 + 1):
    if n % 6 == 0:
        print(n, n % 3 == 0)
# %%

def eh_par(n):
    return n % 2 == 0

def verificar_soma(m, n):
    return eh_par(m + n)

verificar_soma(15, 4)
# %%

for i in range(1, 20 + 1):
    print(i, not eh_par(i), not eh_par(i**2))
# %%

for i in range(1, 20 + 1):
    if not eh_par(i):
        print(i, not eh_par(i), not eh_par(i**2))

# %%

esta_na_agua = True
esta_pegando_fogo = False

contradicao = esta_na_agua and esta_pegando_fogo 
# contradicao = False

if contradicao:
    print("Contradição!")
    print("não é possível estar na água e pegando fogo ao mesmo tempo")
else:
    print("É possível")
# %%
