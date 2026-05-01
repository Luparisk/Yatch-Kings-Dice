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

def faz_jogada(dados, categoria, cartela_de_pontos):
    # calcula tudo uma vez
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancados = calcula_pontos_regra_avancada(dados)

    # verifica se é regra simples (categoria "1" até "6")
    if categoria.isdigit():
        categoria_int = int(categoria)
        cartela_de_pontos['regra_simples'][categoria_int] = pontos_simples[categoria_int]
    else:
        # regra avançada
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]

    return cartela_de_pontos
from funcoes import (rolar_dados,guardar_dado,remover_dado,faz_jogada,imprime_cartela)


def eh_inteiro_nao_negativo(s):
    if len(s) == 0:
        return False
    for c in s:
        if c < "0" or c > "9":
            return False
    return True
#C

def cartela_vazia():
    return {"regra_simples": {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},"regra_avancada": {"sem_combinacao": -1,"quadra": -1,"full_house": -1,"sequencia_baixa": -1,"sequencia_alta": -1, "cinco_iguais": -1}}
#O

def linha_ja_preenchida(cartela, combinacao):
    if eh_inteiro_nao_negativo(combinacao):
        n = int(combinacao)
        if n in cartela["regra_simples"]:
            return cartela["regra_simples"][n] != -1
        return False
    if combinacao in cartela["regra_avancada"]:
        return cartela["regra_avancada"][combinacao] != -1
    return False
#S

def combinacao_existe(cartela, combinacao):
    if eh_inteiro_nao_negativo(combinacao):
        return int(combinacao) in cartela["regra_simples"]
    return combinacao in cartela["regra_avancada"]


def mostrar_dados(rolados, guardados):
    print(f"Dados rolados: {rolados}")
    print(f"Dados guardados: {guardados}")
#E

def calcula_pontuacao_total(cartela):
    soma_simples = 0
    for v in cartela["regra_simples"].values():
        if v != -1:
            soma_simples += v
    soma_avancada = 0
    for v in cartela["regra_avancada"].values():
        if v != -1:
            soma_avancada += v
    bonus = 35 if soma_simples >= 63 else 0
    return soma_simples + soma_avancada + bonus
def jogo():
    cartela = cartela_vazia()
    imprime_cartela(cartela)

    for jogada in range(12):
        dados_rolados = rolar_dados(5)
        dados_guardados = []
        rerrolagens_usadas = 0
        jogada_feita = False
        mostrar_status = True

        while not jogada_feita:
            if mostrar_status:
                mostrar_dados(dados_rolados, dados_guardados)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            mostrar_status = True
            opcao = input()

            if opcao == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                g = input()
                if eh_inteiro_nao_negativo(g) and 0 <= int(g) < len(dados_rolados):
                    resultado = guardar_dado(dados_rolados, dados_guardados, int(g))
                    dados_rolados = resultado[0]
                    dados_guardados = resultado[1]

            elif opcao == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                g = input()
                if eh_inteiro_nao_negativo(g) and 0 <= int(g) < len(dados_guardados):
                    resultado = remover_dado(dados_rolados, dados_guardados, int(g))
                    dados_rolados = resultado[0]
                    dados_guardados = resultado[1]

            elif opcao == "3":
                if rerrolagens_usadas >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    n_para_rolar = 5 - len(dados_guardados)
                    dados_rolados = rolar_dados(n_para_rolar)
                    rerrolagens_usadas += 1

            elif opcao == "4":
                imprime_cartela(cartela)

            elif opcao == "0":
                todos_dados = dados_rolados + dados_guardados
                print("Digite a combinação desejada:")
                escolha_valida = False
                while not escolha_valida:
                    combinacao = input()
                    if not combinacao_existe(cartela, combinacao):
                        print("Combinação inválida. Tente novamente.")
                    elif linha_ja_preenchida(cartela, combinacao):
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(todos_dados, combinacao, cartela)
                        escolha_valida = True
                        jogada_feita = True

            else:
                print("Opção inválida. Tente novamente.")
                mostrar_status = False

    imprime_cartela(cartela)
    pontuacao = calcula_pontuacao_total(cartela)
    print(f"Pontuação total: {pontuacao}")


jogo()
