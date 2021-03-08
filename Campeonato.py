from Surfista import Surfista
from Prancha import Prancha
from Praia import Praia
from Pais import Pais

class Campeonato:
  def __init__(self, nome_campeonato, praia, premio, surfistas = [], campeao = None):
    self._nome_do_campeonato = nome_campeonato
    self._praia = praia
    self._premio = premio
    self._surfistas = surfistas 
    self._praia.add_camp()
    self.registro_participantes()
    self._campeao = campeao
    if(self._campeao != None):
        self._campeao.add_premio(self._premio)

  def registro_participantes(self):
    for surfista in self._surfistas:
      surfista.add_campeonato(self)

  @property
  def nome(self):
      return self._nome_do_campeonato
  @nome.setter
  def nome(self, novo_campeonato):
    self._nome_do_campeonato = novo_campeonato

  @property
  def campeao(self):
      return self._campeao
  @campeao.setter
  def campeao(self, novo_campeao):
      self._campeao = novo_campeao
      self._campeao.add_premio(self._premio)

  @property
  def praia(self):
      return self._praia
  @praia.setter
  def praia(self, nova_praia):
      self._praia = nova_praia

  @property
  def premio(self):
      return self._premio
  @premio.setter
  def premio(self, novo_premio):
      self._premio = novo_premio

  @property
  def surfistas(self):
      return self._surfistas
  @surfistas.setter
  def surfistas(self, novos_surfistas):
      self._surfistas = novos_surfistas

  def adicionar_surfista(self, novo_surfista):
      self._surfistas.append(novo_surfista)
      novo_surfista.add_campeonato(self)


  def menor_idade(self):
    menor = self._surfistas[0].idade

    for i in self._surfistas:
      if(i.idade < menor):
          menor = i.idade
    return menor

  def maior_idade(self):
    
    maior = self._surfistas[0].idade

    for i in self._surfistas:
        if(i.idade > maior):
            maior = i.idade
    return maior
  
  def registro_campeonato(self):
    nomes = '['
    for i in range(len(self._surfistas)):
        if i != len(self._surfistas)-1:
          nomes += f'{self._surfistas[i].nome},'
        else:
          nomes += f'{self._surfistas[i].nome}'   
    nomes += ']'
    return f'''
NOME: {self._nome_do_campeonato}
PRAIA: {self._praia.nome}
PRÊMIO: {self._premio}
PARTICIPANTES: {nomes}
CAMPEÃO: {self._campeao.nome} 
-----------------------------'''

  def __str__(self):
    return f'''{self._nome_do_campeonato}'''