def rolar_dados(n):
    import random
    lista = []
    i = 0
    while n> i:
        x = random.randint(1,6)
        i += 1
        lista.append(x)
    return lista
def guardar_dado(rol, guard, ind):
    x = rol[ind]
    guard.append(x)
    del rol[ind]
    saida = [rol, guard]
    return saida
def remover_dado(rol, guard, ind):
    rol.append(guard[ind])
    del guard[ind]
    resp = [rol, guard]
    return resp
def calcula_pontos_regra_simples(lista):
    chave = {1: 0,
             2: 0,
             3: 0,
             4: 0,
             5: 0,
             6: 0}
    for i in lista:
        if i in chave:
            chave[i] +=i
    return chave
def calcula_pontos_soma(lista):
    soma = 0
    for i in lista:
        soma +=i
    return soma
def calcula_pontos_sequencia_baixa(lista):
    lista2 = []
    for i in range(1,7):
        if i in lista:
            lista2.append(i)
    senha = ''
    for i in lista2:
        senha += f'{i}'
    saida = 0
    if '1234' in senha or '2345' in senha or '3456' in senha:
        saida = 15
    return saida
def calcula_pontos_sequencia_alta(lista):
    lista2 = []
    for i in range(1,7):
        if i in lista:
            lista2.append(i)
    senha = ''
    for i in lista2:
        senha += f'{i}'
    saida = 0
    if '12345' in senha or '23456' in senha:
        saida = 30
    return saida
def calcula_pontos_full_house(lista):
    contagem = {}

    # conta quantas vezes cada número aparece
    for num in lista:
        if num not in contagem:
            contagem[num] = 1
        else:
            contagem[num] += 1

    # pega só as quantidades
    valores = list(contagem.values())
    valores.sort()

    # soma manual
    soma = 0
    for num in lista:
        soma += num

    # verifica se é full house
    if valores == [2, 3]:
        return soma
    else:
        return 0 
def calcula_pontos_quadra(lista):
    contagem = {}

    for num in lista:
        if num not in contagem:
            contagem[num] = 1
        else:
            contagem[num] += 1

    soma = 0
    for num in lista:
        soma += num

    if any(qtd >= 4 for qtd in contagem.values()):
        return soma
    else:
        return 0

def calcula_pontos_quina(lista):
    contagem = {}

    for num in lista:
        if num not in contagem:
            contagem[num] = 1
        else:
            contagem[num] += 1

    if any(qtd >= 5 for qtd in contagem.values()):
        return 50
    else:
        return 0
def calcula_pontos_regra_avancada(lista):
    cinco_iguais = calcula_pontos_quina(lista)
    full_house = calcula_pontos_full_house(lista)
    quadra = calcula_pontos_quadra(lista)
    sequencia_baixa = calcula_pontos_sequencia_baixa(lista)
    sequencia_alta = calcula_pontos_sequencia_alta(lista)
    soma = calcula_pontos_soma(lista)

    resultado = {
        'cinco_iguais': cinco_iguais,
        'full_house': full_house,
        'quadra': quadra,
        'sem_combinacao': soma,
        'sequencia_alta': sequencia_alta,
        'sequencia_baixa': sequencia_baixa
    }

    return resultado
