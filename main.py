#======Bibliotecas======#
import random
import time
import os

#======Funções======#

#====Montando as Tabelas====#

#==Função Para montar as tabelas mostradas==#

def MontarTabelaMostrada():
    LinhaLetras = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    TabelaMostrada = [[ColunasNaoAbertasSimbolo] * Cols for i in range(rows)]
    for i in range(len(TabelaMostrada)):
        for m in range(len(TabelaMostrada)):
            if i == 0:
                if m == 0:
                    TabelaMostrada[i][m] = " "
                else:
                    TabelaMostrada[i][m] = m
                continue

            if m == 0:
                TabelaMostrada[i][m] = LinhaLetras[i]
    return TabelaMostrada

#==Função principal para montar as tabelas verdadeiras==#
    
def MontarTabelaVerdadeira():
    navioSimbolo = "N"
    JogadorTabela = [[ColunasNaoAbertasSimbolo] * Cols for i in range(rows)]  #Criando A Tabela do jogador
    LinhaLetras = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I","J"]  #Essa é a linha que conterá as lestras
    for i in range(len(JogadorTabela)): # Repetição para inserir o número das colunas
        if i == 0:
            for k in range(len(JogadorTabela[i])):
                if k == 0:
                    JogadorTabela[i][k] = " "
                else:
                    JogadorTabela[i][k] = f"{k}"
            continue
        JogadorTabela[i][0] = LinhaLetras[i]

    cont = 0  #serve para verificar se a quantidade de navios posta na tabela condiz com a quantidade pedida pelo o usuário
    while cont < Navios:  #com essa repetição, o programa irá pecorrer a lista até conseguir inserir todos os barcos que o usuário pediu
        i = random.randint(1, 10)
        j = random.randint(1, 10)

        #==Condições para que seja inserido um navio com a distância de um bloco do outro.

        if JogadorTabela[i][j] != navioSimbolo:  #caso a lacuna não possua navio inserido

            if i == len(JogadorTabela[0]) - 1:  #Caso seja a última linha da tabela

                if j == len(JogadorTabela[0]) - 1:  #Caso seja a última linha e a útima coluna da tabela
                    if JogadorTabela[i - 1][j - 1] != navioSimbolo and JogadorTabela[i][ j - 1] != navioSimbolo and JogadorTabela[i - 1][j] != navioSimbolo:
                        cont += 1
                        JogadorTabela[i][j] = navioSimbolo  #não foi encontrado um navio nas proximidades da coluna [10][10], então será feito um novo teste.

                    elif JogadorTabela[i - 1][j - 1] != navioSimbolo and JogadorTabela[i][ j - 1] != navioSimbolo and JogadorTabela[ i -1][j] != navioSimbolo and JogadorTabela[ i -1][j + 1] != navioSimbolo and JogadorTabela[i][j + 1] != navioSimbolo:
                        cont += 1
                        JogadorTabela[i][ j] = navioSimbolo  # não foi encontrado um navio nas proximidades da coluna [10][j]

            elif j == len(JogadorTabela[0]) - 1:  #Caso seja a última coluna da tabela [i][10]. PS: se for a lacuna [10][10], o programa cairá na primeira condicao

                if JogadorTabela[i - 1][j - 1] != navioSimbolo and JogadorTabela[i][j - 1] != navioSimbolo and JogadorTabela[i + 1][j - 1] != navioSimbolo and JogadorTabela[i -1][j] != navioSimbolo and JogadorTabela[i + 1][j] != navioSimbolo:
                    cont += 1
                    JogadorTabela[i][j] = navioSimbolo  # não foi encontrado um navio nas proximidades da coluna [j][10]

            elif i < len(JogadorTabela[0]) - 1 and j < len(JogadorTabela) - 1:  # Isso é para as lacunas que não são as últimas, ou seja, nem i nem j são iguais a 10

                if JogadorTabela[i - 1][j - 1] != navioSimbolo and JogadorTabela[i][j - 1] != navioSimbolo and JogadorTabela[i + 1][j - 1] != navioSimbolo and JogadorTabela[i -1][j] != navioSimbolo and JogadorTabela[i + 1][j] != navioSimbolo and JogadorTabela[i - 1][j +1] != navioSimbolo and JogadorTabela[i][j +1] != navioSimbolo and JogadorTabela[i + 1][j + 1] != navioSimbolo:
                        cont += 1
                        JogadorTabela[i][j] = navioSimbolo  #não foi encontrado navios próximos de [i][j]
    return JogadorTabela

#==Função para mostrar a tabela==#

def MostrarTabela(NomeDoJogadorTabela, JogadorTabela, NomeDoJogadorTurno=None): # O Default, é para ser usado caso a função não receba o nome de um jogador
    
    #print(f"{('='*45):^50}")
    print(f"Tabela de {NomeDoJogadorTabela}")
    
    for i in range(len(JogadorTabela)):
        for j in range(len(JogadorTabela[i])):
            print(f' {JogadorTabela[i][j]:^5}', end="|")
        print()
    
    if NomeDoJogadorTurno!=None: #Caso foi inserido o nome de um jogador
        print("Turno de ", NomeDoJogadorTurno)

#====Função para escolher a coluna====#

def EscolherColuna():  #O jogador1 ou o jogador2 escolherá a coluna desejada
    colunasPosiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #são 10 colunas possíveis

    ColunaEscolhida = int(input("Digite o número de uma COLUNA => "))  # O jogador digita uma coluna

    while ColunaEscolhida not in colunasPosiveis and colunasPosiveis.count(ColunaEscolhida) <= 0:  # caso a coluna não esteja entre 1 e 10
        ColunaEscolhida = int(input("Tu não sabe contar? Escreva um número de 1 a 10 => "))

    IndiceColunaEscolhida = colunasPosiveis.index(ColunaEscolhida) + 1  #por começar no 0, a coluna escolhida deve ser somada com 1
    return IndiceColunaEscolhida  # a coluna escolhida é retornada


#====Função para escolher a Linha====#

def EscolherLinha():
    LinhasPossiveis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J']  # as linhas que o usuário pode escolher vão de A-J
    LinhaEscolhida = str.upper(input("\nDigite a letra de uma LINHA => "))  #O jogador escolhe uma linha

    while LinhaEscolhida not in LinhasPossiveis and LinhasPossiveis.count(LinhaEscolhida) <= 0:  # caso o jogador escreva algo que não seja A-J
        LinhaEscolhida = str.upper(input("Tu não conhece o alfabeto? Escreva uma letra do A ao J => "))

    IndiceLinhaEscolhida = LinhasPossiveis.index(LinhaEscolhida) + 1  #por começar no 0, a linha escolhida deve ser somada com 1
    return IndiceLinhaEscolhida  # a linha escolhida é retornada


#====Função para inserir Água ou Fogo ====#
def InserirSimboloNaTabela(TabelaVerdadeira, Coluna, Linha):
    #==Símbolos para quando uma coluna for escolhida==#
    TiroNaAguaSimbolo = "A"
    TiroNoNavioSimbolo = "F"
    navioSimbolo = "N"
    if TabelaVerdadeira[Linha][Coluna] == navioSimbolo:  # caso tenha um navio na posição escolhida pelo usuário

        print("ACERTOU O NAVIO!")  #Uma mensagem avisando que ele acertou
        time.sleep(3)
        return TiroNoNavioSimbolo

    # caso ele tenha errado o navio
    print("~~~ Água ~~~")  #Uma mensagem avisando que não ele acertou

    time.sleep(3)
    return TiroNaAguaSimbolo


#====Função que irá fazer as modificações na tabela mostrada aos usuários ====#
def MarcarAguaOuFogoNaTabelaMostrada(TabelaMostrada, TabelaVerdadeira):

    while True:
        Linha = EscolherLinha() #função que pede para o usuário escolher uma linha
        Coluna = EscolherColuna() # função que pede para o usuário escolher uma coluna
        print("\n")
        certeza = str.lower(input("Confirma a escolha? (s/n)  \n")) #caso o usuario queira refazer a sua escolha de linha

        while certeza != "s" and certeza != "n": # se o usuário escrever algo diferente de s ou n
            certeza = str.lower(input("Por favor, digite 's' ou 'n':  \n"))

        if certeza == 's': #o jogador confirma sua escolha
            break
        
    print("=="*45)
    TabelaMostrada[Linha][Coluna] = InserirSimboloNaTabela(TabelaVerdadeira, Coluna, Linha) #a tabela  receberá o resultado da funçao, se deve inserir o "F" ou "A" 
    if TabelaMostrada[Linha][Coluna] == "F": # caso um návio tenha sido atigindo
        return True 
    return False # caso a água tenha sido atingida

#====Função que verifica se um jogador venceu ====#
def DefinirVitoria(JogadorNome,TabelaComFogo,NavioQuantidade): # Ela recebe a tabela que é mostrada e a quantidade de navios em jogo
    TiroNoNavioSimbolo='F' # símbolo do navio acertado
    NaviosAcertados=0 # Contador de navios acertados
    for i in range(len(TabelaComFogo)): # irá verificar a quantidade de 'F'
        for j in range(len(TabelaComFogo[i])):
            if TabelaComFogo[i][j] == TiroNoNavioSimbolo and j !=0: # Um F foi achado
                NaviosAcertados+=1
    
    print(JogadorNome," Acertou:", NaviosAcertados, " de um total de: ", NavioQuantidade) 
    print('=='*45)
    if  NaviosAcertados==NavioQuantidade: # Se o jogador conseguiu acertar todos os barcos da tabela adversária. 
        return True

#======Variáveis======#
#====Simbolos Na tabela====#
ColunasNaoAbertasSimbolo = "~"

#====Para a criação das tabelas do jogador1 e jogador2 ====#
#==Número de Linhas e Colunas==#
Cols = 11  #São 10 colunas (1-10) com adição de uma coluna que servirá para indicar o núnmero da linha
rows = 11  # São 10 linhas (A-J) com adição de uma linha que servirá para indicar a letra da coluna

#==Quantidade de barcos

limite = 10  #Referente a quantidade de barcos permitidos

#======Entradas======#

#====Nomes====#
#==Interação com o usuário==#

Jogador1Nome= input("Digite o nome do jogador 1: \n")
print("=="*45)
Jogador2Nome= input("Digite o nome do jogador 2: \n")
print("=="*45)

#==Interação Com o usuário

Navios = int(
    input(f"Digite a quantidade de navios que cada frota possuirá (limite de {limite} barcos): \n"))

while Navios > limite or Navios <= 0:
    Navios = int(input(f"Você digitou um valor não permitido! Por favor, digite de 0 até {limite}! \n"))

#====Criando as tabelas com as Funções====#
Jogador1TabelaVerdadeira = MontarTabelaVerdadeira()  #Criando a Tabela que conterá os navios do Jogador 1
Jogador2TabelaVerdadeira = MontarTabelaVerdadeira()  #Criando a Tabela que conterá os navios do Jogador 2
Jogador1TabelaMostrada = MontarTabelaMostrada()  #Criando a Tabela que será mostrada ao Jogador 1
Jogador2TabelaMostrada = MontarTabelaMostrada()  #Criando a Tabela que será mostrada ao Jogador 2

#====Mostrando as tabelas====#
DesejaMostrarTabela= input(f"Deseja mostrar as tabelas criadas de {Jogador1Nome} e {Jogador2Nome} ? (s/n) \n")
while str.lower(DesejaMostrarTabela) not in 'sn':
    DesejaMostrarTabela= input(f"Não entendi... \n Deseja mostrar as tabelas criadas de {Jogador1Nome} e {Jogador2Nome}? (s/n) \n")

if DesejaMostrarTabela =='s':
    MostrarTabela(Jogador1Nome,Jogador1TabelaVerdadeira)  #função que mostrará as tabelas
    time.sleep(4)

    MostrarTabela(Jogador2Nome, Jogador2TabelaVerdadeira)  #função que mostrará as tabelas
    time.sleep(4)

if DesejaMostrarTabela=='n':
    time.sleep(4)
    os.system("clear")



#======Variáveis ======#
rodada=0 #contador de rodadas já passadas
navioSimbolo = "N" #símbolo dos navios
TiroNoNavioSimbolo = "F" #símbolo de que um navio foi acertado

vencedor=None # Variável que vai englobar o nome do jogador  que conseguiu acertar todos os barcos
jogarVez=True # Boleano fica melhor para decidir entre dois jogadores, se for True, jogador 1 joga, se não, Jogador 2 joga. Nota2: Fica melhor nada, dificultou ainda mais a minha vida

while DefinirVitoria(Jogador1Nome,Jogador2TabelaMostrada, Navios)!= True and DefinirVitoria(Jogador2Nome,Jogador1TabelaMostrada, Navios)!= True : # o loop só será encerrado se um dos jogadores conseguir acertar todos os navios do outro jogador 
    
    print(f"\n{rodada+1}º Tiro")
    print("=="*45)
    
    if jogarVez==True: # Jogador 1 jogará sempre que jogarVez for True
        
        MostrarTabela(Jogador2Nome,Jogador2TabelaMostrada,Jogador1Nome)
        time.sleep(1)
        print("\nPreparar... \nApontar...")
        time.sleep(2)
        jogarVez= MarcarAguaOuFogoNaTabelaMostrada(Jogador2TabelaMostrada, Jogador2TabelaVerdadeira)#Caso tenha acertado um navio, o valor que deve ser retornado será True se o contrário, será False.
        vencedor=Jogador1Nome # Não é preciso testar se ele acertou todos os navios, se esse jogador acertou todos os navios, ele sairá do loop, se não, o while irá continuar até que um novo vencedor surja 
        
             
    else: 
        
        MostrarTabela(Jogador1Nome,Jogador1TabelaMostrada,Jogador2Nome)
        print("\nPreparar... \nApontar...")
        time.sleep(2)
        jogarVez= not MarcarAguaOuFogoNaTabelaMostrada(Jogador1TabelaMostrada, Jogador1TabelaVerdadeira) #Caso tenha acertado um navio, o valor que deve ser retornado será True caso o contrário, será False. Por ser booleano, podemos inverter o valor retornado da função
        vencedor=Jogador2Nome
    
    rodada+=1
    
print(f'{vencedor}, você foi o vencedor da BATALHA NAVAL!!!')
