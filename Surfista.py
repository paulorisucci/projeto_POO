from Prancha import Prancha

class Surfista:
    def __init__(self,nome, idade, pranchas = [], campeonatos = [],total_ganho = 0):
        self._nome = nome #String
        self._idade = idade #int
        self._campeonatos = campeonatos #litaCampeonatos
        self._pranchas = pranchas #listaPranchas
        self._total_ganho = total_ganho #float

    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
    @property
    def lst_campeonato(self):
        return self._campeonatos
    @property
    def total_ganho(self):
      return self._total_ganho
    @property
    def pranchas(self):
        return self._pranchas

    @nome.setter
    def nome(self, novo):
        self._nome = novo
    @idade.setter
    def idade(self, novo):
        self._idade = novo
    @lst_campeonato.setter
    def lst_campeonato(self, campeonatos):
        self._campeonatos = campeonatos
    @total_ganho.setter
    def total_ganho(self, novo_total):
        return self._total_ganho
    @pranchas.setter
    def pranchas(self, novas_pranchas):
      self._pranchas = novas_pranchas

    def add_campeonato(self, c):
        if c not in self._campeonatos:
            self._campeonatos.append(c)

    def add_premio(self, premio):
      self._total_ganho += premio

    def pranchas_marca(self, marca):
        list_p = 'Nenhuma'
        for i in self._pranchas:
            if i.marca == marca:
                list_p = list_p.replace('Nenhuma', '')
                list_p += '--------------------------\n' 
                list_p += f'{i}'        
        return list_p

    def total_ganho(self):
        return self._total_ganho

    def str_campeonatos(self):
      nome = '\nCAMPEONATOS DISPUTADOS:\n'
      for i in self._campeonatos:
        if(i.campeao == self):
            nome += f'- {i.nome} *\n'
        else:
            nome += f'- {i.nome}\n'
      return nome

    def add_prancha(self,p):
        if p not in self._pranchas:
            self._pranchas.append(p)

    def __str__(self):
        prancha = ''
        for i in self._pranchas:
            prancha += f'# {i.marca} #'

        return f'''NOME: {self._nome}
IDADE: {self._idade} anos
PRANCHA(S): 
{prancha}'''