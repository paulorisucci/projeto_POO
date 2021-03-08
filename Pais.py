from Praia import Praia

class Pais:
  def __init__(self, nome, lingua, praias = []):
    self._nome = nome #string
    self._lingua = lingua #string
    self._praias = praias #listaPraia
    self._registro_pais()


  @property
  def nome(self):
    return self._nome
  @property
  def lingua(self):
    return self._lingua
  @property
  def praia(self):
    return self._praias

  @nome.setter
  def nome(self, novo):
    self._nome = novo
  @lingua.setter
  def lingua(self, novo):
    self._lingua = novo
  @praia.setter
  def praias(self, praias):
    self._praias = praias
    self._registro_pais()

  def _registro_pais(self):
    for praia in self._praias:
      praia.pais = self

  def praias_mais_selecionadas(self, quantidade):
    list=f'{self._nome}: nenhuma\n'
    for praia in self._praias:
      if praia.num_campeonatos >= quantidade:
        list = list.replace('nenhuma', '')
        list += '---------------------\n'
        list += f'{praia}'
    return list

  def add_praia(self,p):
    if p not in self._praias:
      self._praias.append(p)

  def __str__(self):
    nomes = ''
    for i in self._praias:
      nomes += f'#{i.nome}'

    return f'''NOME: {self._nome}
LINGUA: {self._lingua}
PRAIAS(S): {nomes}
'''