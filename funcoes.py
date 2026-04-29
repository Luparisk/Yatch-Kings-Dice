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
    sla = []
    check = {}
    for i in lista:
        if i not in check:
            check[i] = 1
            sla.append(i)
        else:
            check[i] += 1
            sla.append(i)

    sortsla = sorted(sla)

    soma = 0
    for num in lista:
        soma += num

    if sortsla[0] == sortsla[1] == sortsla[2] and sortsla[3] == sortsla[4]:
        return soma
    elif sortsla[0] == sortsla[1] and sortsla[2] == sortsla[3] == sortsla[4]:
        return soma
    else:
        return 0
