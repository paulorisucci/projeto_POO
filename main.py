from Campeonato import Campeonato
from Pais import Pais
from Praia import Praia
from Prancha import Prancha
from Surfista import Surfista
from random import randint


def encontre_surfista(nome, lst_surf):
    for i in lst_surf:
        if i.nome == nome:
            return i
    raise ValueError

def encontre_praia(nome, praias):
  for i in praias:
    if(i.nome == nome):
      return i
  raise ValueError

def encontre_campeonato(nome, lst_camps):
  for i in lst_camps:
    if(i.nome == nome):
      return i
  raise ValueError

campeonatos = list()
resp = ''

praia0 = Praia('The Wedge', 30)
praia1 = Praia('Hawai', 40)
praia2 = Praia('Bondi Beach', 60)
praias = [praia0, praia1, praia2]

EUA = Pais('Estados Unidos', 'Inglês', [praia0, praia1])
AUSTRALIA = Pais('Australia', 'Inglês', [praia2])
lst_paises = [EUA, AUSTRALIA]


pr1 = Prancha('Firewire', 2.1, 'Vermelho e branco', 1500, AUSTRALIA)
pr2 = Prancha('Lost', 2.34, "Azul e verde", 1430.0, EUA)

s1 = Surfista('Paulo Elias', 20, [pr1, pr2])
s2 = Surfista('Pedrinho', 19, [pr1])
lst_surfistas = [s1, s2]

cx = Campeonato('CAMPEONATO ANTERIOR', praia0, 10000, lst_surfistas, s2)
campeonatos.append(cx)

c1 = Campeonato('THE GREAT CHAMPIONSHIP OF SURF', praia1, 200000,lst_surfistas)
campeonatos.append(c1)


while resp != 'N' and resp != 'NÃO':

  print(f'2 surfistas irão se inscrever imediatamente : {lst_surfistas[0].nome} e {lst_surfistas[1].nome}')

  print('*' * 30)
  print(f'{c1}\n')
  flag = ''
  acabou = False

  while flag != '0':
    flag = input('''\nDigite a opção que deseja executar:
          1 - REGISTRAR CANDIDATO  
          2 - REALIZAR CAMPEONATO 
          3 - ESCOLHER REGISTRO DE SURFISTA
          4 - DINHEIRO TOTAL
          5 - PRAIAS COM MAIS CAMPEONATOS
          6 - PRANCHAS DOS SURFISTAS
          7 - MAIOR E MENOR IDADE
          8 - REGISTRO DE CAMPEONATOS
          0 - SAIR\n''')
          
    if (flag == '1'): #Cadastra um surfista
      if(acabou == False):  
        nome = input('Nome: ').title()
        idade = input('Idade: ')
        qtde_pranchas = int(input('Digite a quantidade de pranchas:'))
        lista_pranchas = []

        for i in range(qtde_pranchas):
          marca = input('Digite a marca: ').title()
          comprimento = float(input('Digite o comprimento: '))
          cor = input('Digite a cor: ').title()
          valor = float(input('Digite a valor: '))

          pr1 = Prancha(marca, comprimento, cor, valor, EUA)
          lista_pranchas.append(pr1)

        sx = Surfista(nome, idade, lista_pranchas, [c1])
        lst_surfistas.append(sx)
      else:
        print('O campeonato já acabou.')



    elif (flag == '2'): #Decide o campeão do campeonato atual
      if(acabou == False):
        
        res = randint(0, len(c1.surfistas) - 1)
        c1.campeao = c1.surfistas[res]

        print(f'''{'*' * 35}
CAMPEÃO MUNDIAL DE SURF: [{c1.campeao.nome}]
{'*' * 35}''')
        print(c1.registro_campeonato())
        acabou = True

      else:
        print('Este campeonato já acabou!')
        print('Resultado: ')
        print(c1.registro_campeonato())
    
    elif (flag == '3'): #escolhe o registro do surfista c1
      print('Digite o nome surfista que deseja ver:')
      for i in campeonatos[-1].surfistas: 
        print(f'# {i.nome}') 
      
      nome_surf = (input('')).title()
      s = encontre_surfista(nome_surf, lst_surfistas)
      print(s)
      print(s.str_campeonatos())

    elif (flag == '4'): #imprime o total ganho
      try:
        print('Digite o nome do surfista: ')
        for i in c1.surfistas:
          print(f'# {i.nome}')
        
        surfista = input().title()

        WIN = encontre_surfista(surfista, lst_surfistas)
        print(f'''{'*' * 35}
TOTAL GANHO POR {WIN.nome}:[R${WIN.total_ganho()}]
{'*' * 35}''')
      except:
        print('Nome inválido.')

    elif(flag == '5'): #Retorna as praias com o n de campeonatos maior
      qtde_camp = int(input('Quantidade de campeonatos: '))

      print(f'Praias com mais de {qtde_camp} campeonatos: \n')
      for pais in lst_paises:
        praias_mais_selecionadas = pais.praias_mais_selecionadas(qtde_camp)
        print(f'{praias_mais_selecionadas}')


    elif(flag == '6'): #Retorna as prancas de uma marca
      marca = input('Digite o nome da marca da prancha: ')

      for surfista in lst_surfistas:
        print(f'''Nome do surfista: {surfista.nome}
{surfista.pranchas_marca(marca)}''')

    elif(flag == '7'):
      print('###MAIOR E MENOR IDADE###')
      campeonatos_ganhos = ''
      string_resp = 'Nenhum campeonato foi ganho.'
      nome = input('Digite o nome do surfista: ')
      surfista = encontre_surfista(nome, lst_surfistas)

      for i in surfista.lst_campeonato:
        if(i.campeao == surfista):
          string_resp = string_resp.replace('Nenhum campeonato foi ganho.', '')
          campeonatos_ganhos += f'{i} '

      if(campeonatos_ganhos != ''):
        print(f'Escolha um campeonato ganho: ',campeonatos_ganhos)
        nome_camp = input()
        camp = encontre_campeonato(nome_camp, campeonatos)
        maior_idade = camp.maior_idade()
        menor_idade = camp.menor_idade()

        string_resp += f'''Maior idade: {maior_idade}
Menor idade: {menor_idade}'''
      print(string_resp)
    

    elif(flag == '8'):
      for i in range(len(campeonatos)):
        print(f'{i} - {campeonatos[i].nome}')

      escolha = int(input('\nDigite o número referente ao campeonato desejado: '))
      print(f'{campeonatos[escolha].registro_campeonato()}')


  resp = input('Deseja cadastrar um novo Campeonato? ').upper()
  
  if(resp == 'S'or resp == "SIM"):
    nome_camp = input('Digite o nome do campeonato: ').title()
    nome_praia = input(f'Digite em qual praia será realizado ({praia0.nome}, {praia1.nome}, {praia2.nome}:\n ').title()
    
    praia_camp = encontre_praia(nome_praia, praias)
    premio = float(input('Digite o prêmio: '))
    c1 = Campeonato(nome_camp, praia_camp, premio, lst_surfistas)
    campeonatos.append(c1)

print('Fim do programa.')